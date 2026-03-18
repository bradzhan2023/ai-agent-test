import os
import requests
import json
from git import Repo

# ================= 配置區域 =================
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USER = "bradzhan2023"
GITHUB_REPO = "ai-agent-test"

APP_FILE = "generated_app.py"
AGENT_FILE = "agent_deploy.py"
README_FILE = "README.md"

if not GEMINI_API_KEY or not GITHUB_TOKEN:
    print("❌ 錯誤：請先執行 export 設定環境變數！")
    exit(1)

GITHUB_REPO_URL = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git"
# ===========================================

def get_available_model():
    """探測可用模型清單"""
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
    raise Exception("無法獲取模型")

def call_gemini_api(prompt, model_id, api_ver):
    url = f"https://generativelanguage.googleapis.com/{api_ver}/{model_id}:generateContent?key={GEMINI_API_KEY}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, headers={'Content-Type': 'application/json'}, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    raise Exception(f"API Error: {response.text}")

def developer_agent_incremental(task, model_id, api_ver):
    """【核心功能】讀取舊代碼並進行增量修改"""
    existing_code = ""
    if os.path.exists(APP_FILE):
        with open(APP_FILE, "r", encoding="utf-8") as f:
            existing_code = f.read()
    
    if existing_code:
        print(f"🔄 偵測到現有代碼，正在進行『增量修改』...")
        prompt = f"""
        你是一個資深 Python 工程師。
        目前檔案內容如下：
        ---
        {existing_code}
        ---
        請在保留上述所有功能的前提下，新增以下功能：{task}。
        要求：
        1. 輸出完整的、合併後的代碼。
        2. 確保舊功能與新功能不會衝突。
        3. 只輸出 Python 代碼，不要有 markdown 標籤或說明。
        """
    else:
        print(f"🆕 尚未有現有代碼，正在建立新功能...")
        prompt = f"任務：{task}。請直接輸出 Python 代碼，不要包含 markdown 標籤。"
    
    code = call_gemini_api(prompt, model_id, api_ver)
    return code.replace("```python", "").replace("```", "").strip()

def github_release_agent(task_name, app_code, readme_content):
    print(f"🚀 [Release Agent] 同步所有檔案至 GitHub...")
    with open(APP_FILE, "w", encoding="utf-8") as f: f.write(app_code)
    with open(README_FILE, "w", encoding="utf-8") as f: f.write(readme_content)

    try:
        repo = Repo(".")
        if 'origin' in [r.name for r in repo.remotes]:
            repo.remote('origin').set_url(GITHUB_REPO_URL)
        else:
            repo.create_remote('origin', GITHUB_REPO_URL)

        repo.index.add([APP_FILE, AGENT_FILE, README_FILE])
        commit_msg = f"AI Update: {task_name}\n\nIncremental update by AI Agent."
        repo.index.commit(commit_msg)
        repo.git.push(GITHUB_REPO_URL, 'main')
        print(f"✅ 部署成功！")
    except Exception as e:
        print(f"❌ Git 失敗: {e}")

if __name__ == "__main__":
    # --- 你可以隨時修改這裡的任務內容 ---
    # 第一次執行可以是 "寫一個計算質數的函數"
    # 第二次執行可以是 "新增一個快速排序 (Quick Sort) 的函數"
    my_task = "新增一個泡沫排序 (Quick Sort) 的函數"
    
    try:
        model_id, api_ver = get_available_model()
        
        # Step 1: 增量開發
        clean_code = developer_agent_incremental(my_task, model_id, api_ver)
        
        # Step 2: 生成說明文件 (分析腳本與新功能)
        print(f"📖 [Document] 更新 README...")
        with open(AGENT_FILE, "r", encoding="utf-8") as f: script_content = f.read()
        doc_prompt = f"請為此專案寫 README.md。內容包含專案簡介、如何執行、以及這份代碼支援『增量開發』的特色。任務：{my_task}。腳本參考：\n{script_content}"
        readme_md = call_gemini_api(doc_prompt, model_id, api_ver)
        
        # Step 3: 發布
        github_release_agent(my_task, clean_code, readme_md)

    except Exception as e:
        print(f"💥 錯誤: {e}")