好的，這是一份為您的 GitHub 專案 `ai-agent-test` 設計的專業 README.md 文件。這份文件以繁體中文撰寫，詳細介紹了您的 Multi-Agent 自動化工具及其功能，並說明瞭如何設定與執行。

---

# AI 多代理自動化部署與程式碼生成工具
## 目標專案：1-100 質數生成器

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Gemini API](https://img.shields.io/badge/Google%20Gemini-API-orange?logo=google)
![GitHub Actions](https://img.shields.io/badge/GitHub-Deployment-brightgreen?logo=github)
![License](https://img.shields.io/badge/License-MIT-green) <!-- 假設使用 MIT 許可證 -->

---

## 🚀 專案簡介

這是一個創新的 Multi-Agent 自動化工具 `agent_deploy.py`，旨在簡化從想法到 GitHub 部署的整個開發流程。它融合了大型語言模型 (LLM) 的智慧與自動化腳本的力量，實現了**程式碼撰寫、文件生成及 GitHub 部署**的全自動化。

目前，此工具已配置並成功生成一個 Python 腳本 (`generated_app.py`)，用於找出 1 到 100 之間的質數，並已將其連同自動生成的 `README.md` 部署到本 GitHub 儲存庫。這個專案本身就是 `agent_deploy.py` 成功運作的一個實例！

---

## ✨ 主要特色

`agent_deploy.py` 腳本具備以下強大功能：

*   **🔍 智慧模型探測**: 自動偵測並使用您 API Key 下可用的最新 Gemini 模型 (例如 Gemini Flash)。
*   **📝 程式碼自動生成**: 根據給定的任務描述（例如「撰寫一個 Python 腳本，輸出 1 到 100 之間的質數」），利用 Gemini 模型自動撰寫 Python 程式碼。
*   **📖 文件自動生成**: 根據生成的程式碼內容和專案目標，自動撰寫專業且符合規範的 `README.md` 文件。
*   **🚀 GitHub 自動部署**: 自動將生成的程式碼 (`generated_app.py`) 和文件 (`README.md`)，連同 `agent_deploy.py` 本身，提交並推送到指定的 GitHub 儲存庫 (`bradzhan2023/ai-agent-test`)。
*   **🔄 全自動化工作流程**: 從指令到部署，實現端到端的開發自動化，大幅提升開發效率。

---

## 🎯 當前任務目標 (由 `agent_deploy.py` 執行)

本專案的當前任務是生成一個名為 `generated_app.py` 的 Python 腳本，該腳本能夠找出並輸出 1 到 100 之間的所有質數。

### `generated_app.py` 範例輸出：

當您執行 `python generated_app.py` 時，預期會看到類似以下的輸出：

```
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```

---

## 🛠️ 環境設定與執行

要執行 `agent_deploy.py` 腳本並體驗其自動化功能，請遵循以下步驟：

### 1. 前置條件

*   **Python**: 建議使用 Python 3.8 或更高版本。
*   **Git**: 確保您的系統已安裝 Git。
*   **GitHub 儲存庫**: 您需要一個 GitHub 帳戶，並且對 `https://github.com/bradzhan2023/ai-agent-test` 儲存庫擁有寫入權限，或者您可以將 `agent_deploy.py` 檔案中的 `GITHUB_USER` 和 `GITHUB_REPO` 修改為您自己的儲存庫。

### 2. 克隆儲存庫

首先，將此 GitHub 儲存庫克隆到您的本地機器：

```bash
git clone https://github.com/bradzhan2023/ai-agent-test.git
cd ai-agent-test
```

### 3. 安裝依賴項

本專案需要安裝 `requests` 和 `GitPython` 庫。請透過 `pip` 安裝：

```bash
pip install requests GitPython
```

### 4. 設定環境變數 (重要！)

為了安全地連接到 Gemini API 和 GitHub，您必須設定以下環境變數。**請勿將您的 API 金鑰或 Token 硬編碼在程式碼中。**

*   **`GEMINI_API_KEY`**: 您的 Google Gemini API 金鑰。
    *   如何獲取：請訪問 [Google AI Studio](https://aistudio.google.com/app/apikey) 獲取您的 API 金鑰。
*   **`GITHUB_TOKEN`**: 您的 GitHub 個人存取權杖 (Personal Access Token, PAT)。
    *   如何獲取：
        1.  登入 GitHub。
        2.  進入 `Settings` -> `Developer settings` -> `Personal access tokens` -> `Tokens (classic)`。
        3.  點擊 `Generate new token`。
        4.  給予一個描述性名稱 (例如 "AI Agent Deploy")。
        5.  **重要：** 授予權杖 `repo` 範圍的權限，這將允許其讀寫您的儲存庫。
        6.  生成權杖後，請務必複製它，因為您將無法再次看到它。

在 Linux/macOS 終端機中設定環境變數：

```bash
export GEMINI_API_KEY="您的_Gemini_API_金鑰"
export GITHUB_TOKEN="您的_GitHub_個人存取權杖"
```

在 Windows 命令提示字元中設定環境變數：

```cmd
set GEMINI_API_KEY="您的_Gemini_API_金鑰"
set GITHUB_TOKEN="您的_GitHub_個人存取權杖"
```

在 Windows PowerShell 中設定環境變數：

```powershell
$env:GEMINI_API_KEY="您的_Gemini_API_金鑰"
$env:GITHUB_TOKEN="您的_GitHub_個人存取權杖"
```

### 5. 執行 `agent_deploy.py` 腳本

設定好環境變數後，您就可以執行 `agent_deploy.py` 了：

```bash
python agent_deploy.py
```

當腳本執行時，您將在終端機中看到代理的工作流程：

1.  自動探測可用的 Gemini 模型。
2.  `[Developer]` 代理將根據任務 (找出 1 到 100 的質數) 撰寫 `generated_app.py` 的程式碼。
3.  `[Document]` 代理將根據生成的程式碼內容自動生成一份新的 `README.md`。
4.  `[Release Agent]` 代理將把 `generated_app.py`、新生成的 `README.md` 以及 `agent_deploy.py` 本身提交並推送到 GitHub 儲存庫。

**注意：** 每次執行 `agent_deploy.py`，它都會嘗試更新 `generated_app.py` 和 `README.md`，並將所有變更推送到 GitHub。

---

## ⚙️ 腳本結構與工作流程 (`agent_deploy.py`)

`agent_deploy.py` 腳本主要包含以下模組化功能：

*   **配置區域**: 安全地從環境變數讀取 API 金鑰和 GitHub 認證資訊。
*   **`get_available_model()`**: 負責探測 Gemini API，找出最新且可用的模型 ID。
*   **`call_gemini_api()`**: 封裝了對 Gemini API 的呼叫邏輯，用於生成文本（程式碼和文件）。
*   **`github_release_agent()`**: 負責將生成的檔案寫入本地，並使用 `GitPython` 庫執行 Git 操作（新增、提交、推送）到 GitHub 儲存庫。
*   **主執行流程 (`if __name__ == "__main__":`)**:
    *   定義當前任務 (`my_task`)。
    *   呼叫 `get_available_model()`。
    *   呼叫 `call_gemini_api()` 以生成程式碼 (`clean_code`)。
    *   讀取 `agent_deploy.py` 內容，並再次呼叫 `call_gemini_api()` 以生成 `README.md` (`readme_md`)。
    *   最後，呼叫 `github_release_agent()` 將所有檔案部署到 GitHub。

---

## 🤝 貢獻

歡迎任何形式的貢獻！如果您有任何建議、功能請求或發現錯誤，請隨時開立 Issue 或提交 Pull Request。

---

## 📄 許可證

本專案採用 MIT 許可證。詳情請參閱 `LICENSE` 檔案。(請在您的實際專案中添加一個 `LICENSE` 文件)

---