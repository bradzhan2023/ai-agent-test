import os
import requests
import json
from git import Repo

# ================= 配置區域 (安全變數讀取) =================
# 注意：執行前請先在終端機執行 export 設定這些變數
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = "bradzhan2023"
GITHUB_REPO = "ai-agent-test"

# 檔案清單
APP_FILE = "generated_app.py"
AGENT_FILE = "agent_deploy.py"
README_FILE = "README.md"

# 檢查環境變數是否已設定
if not GEMINI_API_KEY or not GITHUB_TOKEN:
    print("❌ 錯誤：請先在終端機設定環境變數！")
    print("指令範例：")
    print('  export GEMINI_API_KEY="你的_KEY"')
    print('  export GITHUB_TOKEN="你的_TOKEN"')
    exit(1)

# 認證用的 URL (動態組合，不寫死在檔案內)
GITHUB_REPO_URL = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git"
# =========================================================

def get_available_model():
    """自動探測 API Key 可用的最新模型 ID"""
    for version in ["v1", "v1beta"]:
        url = f"https://generativelanguage.googleapis.com/{version}/models?key={GEMINI_API_KEY}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                models = response.json().get('models', [])
                for m in models:
                    if 'flash' in m['name'] and 'generateContent' in m.get('supportedGenerationMethods', []):
                        return m['name'], version
        except: continue
    raise Exception("無法獲取可用模型，請檢查 API Key 權限。")

def call_gemini_api(prompt, model_id, api_ver):
    url = f"https://generativelanguage.googleapis.com/{api_ver}/{model_id}:generateContent?key={GEMINI_API_KEY}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    return f"Error: {response.text}"

def github_release_agent(task_name, app_code, readme_content):
    print(f"🚀 [Release Agent] 正在同步檔案至 GitHub...")
    
    # 1. 寫入生成的檔案
    with open(APP_FILE, "w", encoding="utf-8") as f: f.write(app_code)
    with open(README_FILE, "w", encoding="utf-8") as f: f.write(readme_content)

    try:
        repo = Repo(".")
        # 確保遠端 URL 更新
        if 'origin' in [r.name for r in repo.remotes]:
            repo.remote('origin').set_url(GITHUB_REPO_URL)
        else:
            repo.create_remote('origin', GITHUB_REPO_URL)

        # 2. 加入所有檔案 (包含腳本、生成的 app、以及 README)
        repo.index.add([APP_FILE, AGENT_FILE, README_FILE])
        
        commit_msg = f"AI Workflow Update: {task_name}\n\n- Updated documentation\n- Self-uploaded agent script"
        repo.index.commit(commit_msg)
        
        # 3. 推送至 main 分支
        repo.git.push(GITHUB_REPO_URL, 'main')
        print(f"✅ 成功！現在 GitHub 已包含代碼與自動生成的 README。")
    except Exception as e:
        print(f"❌ Git 操作失敗: {e}")

if __name__ == "__main__":
    my_task = "寫一個 Python 腳本，實作一個快速排序，然後測試"
    
    try:
        model_id, api_ver = get_available_model()
        
        # Step 1: 撰寫代碼
        print(f"🤖 [Developer] 正在撰寫任務...")
        code = call_gemini_api(f"{my_task}。請只輸出程式碼。", model_id, api_ver)
        clean_code = code.replace("```python", "").replace("```", "").strip()
        
        # Step 2: 撰寫 README (讀取腳本內容進行分析)
        print(f"📖 [Document] 正在根據腳本內容生成 README...")
        with open(AGENT_FILE, "r", encoding="utf-8") as f:
            script_content = f.read()
        
        doc_prompt = f"""
        你是一個技術文件專家。請為這個 GitHub 專案寫一份專業的 README.md。
        專案目標：{my_task}
        腳本功能：這個 `agent_deploy.py` 是一個 Multi-Agent 自動化工具，
        具備自動探測 Gemini 模型、撰寫代碼、自動生成文件並部署到 GitHub 的功能。
        請用繁體中文撰寫，包含專案簡介、特色、以及如何設定環境變數執行。
        
        腳本內容參考：
        {script_content}
        """
        readme_md = call_gemini_api(doc_prompt, model_id, api_ver)
        
        # Step 3: 一鍵發布
        github_release_agent(my_task, clean_code, readme_md)

    except Exception as e:
        print(f"💥 錯誤: {e}")