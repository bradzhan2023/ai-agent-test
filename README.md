好的，身為技術文件專家，這是一份為您的 GitHub 專案 `agent_deploy.py` 撰寫的專業 `README.md` 文件。

---

# 🚀 AI Workflow 自動化部署工具

## 專案簡介

本專案的核心是一個創新的 Python 腳本 `agent_deploy.py`，它實現了一個**多代理 (Multi-Agent) 自動化工作流程**。此工具旨在簡化從概念到 GitHub 部署的整個軟體開發生命週期。它能夠自動與 Google Gemini 模型互動，執行任務探測、程式碼生成、文件撰寫，最終將所有成果自動發布到 GitHub 儲存庫。

無論您是想快速原型開發、自動化日常編程任務，或是實驗 AI 驅動的開發流程，`agent_deploy.py` 都能作為您的智慧助理，將創意轉化為實際部署的程式碼和文件。

**本次示範任務為：撰寫一個 Python 腳本，實作一個快速排序，然後測試。**

## ✨ 主要特色

*   **🤖 自動化 AI 模型探測**
    *   智慧探測您的 `GEMINI_API_KEY` 所能存取的最新的 Gemini 模型版本 (如 `gemini-pro-flash` 等)。
*   **✍️ 程式碼自動生成**
    *   根據您提供的任務描述，呼叫 Gemini API 自動生成符合需求的 Python 程式碼。
*   **📖 文件自動生成**
    *   作為一個「文件專家」代理，它能分析生成的程式碼和專案目標，自動撰寫專業的 `README.md` 文件，讓您的專案始終保持良好文檔。
*   **🚀 GitHub 自動部署**
    *   整合 GitPython 庫，實現生成檔案 (程式碼、文件) 的自動提交 (commit) 與推送 (push) 到指定的 GitHub 儲存庫，無需手動操作。
*   **🔒 安全的環境變數管理**
    *   所有敏感資訊 (API Key, GitHub Token) 都透過環境變數安全讀取，避免硬編碼。
*   **🔄 自我部署能力**
    *   這個工具本身也是它自己工作流程的證明，它能夠管理並部署由其自身生成的內容，展現了高度的自動化和彈性。

## 🛠️ 環境設定與執行

在執行 `agent_deploy.py` 之前，您需要設定必要的環境變數並安裝相關依賴。

### 前置準備

1.  **Python 3.x**: 確保您的系統已安裝 Python 3.6 或更高版本。
2.  **Git**: 確保您的系統已安裝 Git 版本控制工具。
3.  **GitHub 儲存庫**: 您需要一個公開或私有的 GitHub 儲存庫，用於接收自動部署的內容。
    *   目前腳本中硬編碼的儲存庫為 `bradzhan2023/ai-agent-test`，您可以自行修改 `GITHUB_USER` 和 `GITHUB_REPO` 變數來指定您的儲存庫。

### 步驟 1: 安裝依賴

首先，複製本專案到您的本機，並安裝所需的 Python 套件：

```bash
# 複製專案
git clone [您的 GitHub 專案 URL]
cd [您的專案目錄]

# 安裝 Python 依賴
pip install requests GitPython
```

### 步驟 2: 設定環境變數

此腳本依賴於兩個重要的環境變數來進行認證和操作：

*   `GEMINI_API_KEY`: 您的 Google Gemini API Key。
*   `GITHUB_TOKEN`: 您的 GitHub 個人存取令牌 (Personal Access Token, PAT)。

請按照以下說明設定這些變數：

#### 獲取 Google Gemini API Key

1.  前往 [Google AI Studio](https://aistudio.google.com/app/apikey) 建立或取得您的 API Key。

#### 獲取 GitHub Personal Access Token (PAT)

1.  登入您的 GitHub 帳戶。
2.  前往 **Settings** -> **Developer settings** -> **Personal access tokens** -> **Tokens (classic)**。
3.  點擊 **Generate new token**。
4.  為您的 Token 命名 (例如：`ai-agent-deploy`)。
5.  在 **Select scopes** 區塊，您需要勾選 **`repo`** 相關的所有權限 (或至少 `repo` 的所有子選項，以確保讀寫權限)。
6.  點擊 **Generate token**。
7.  **務必立即複製生成的令牌！** 它只會顯示一次。

#### 在終端機設定環境變數

在執行腳本的終端機中，請執行以下命令設定環境變數：

```bash
export GEMINI_API_KEY="您的_實際_GEMINI_API_KEY"
export GITHUB_TOKEN="您的_實際_GITHUB_PAT_令牌"

# 您也可以修改腳本中的 GITHUB_USER 和 GITHUB_REPO 變數
# 或者在這裡設定為環境變數，讓腳本去讀取 (需要修改腳本讀取方式)
# export GITHUB_USER="您的_GitHub_使用者名稱"
# export GITHUB_REPO="您的_目標_儲存庫名稱"
```

**重要提示：** 這些變數只會在當前終端機會話中有效。如果您開啟新的終端機或重新啟動電腦，需要重新設定。為了長期使用，您可以將它們添加到您的 shell 配置檔案 (如 `~/.bashrc`, `~/.zshrc` 或 `~/.profile`) 中。

### 步驟 3: 執行腳本

環境變數設定完畢後，您就可以執行 `agent_deploy.py` 腳本了：

```bash
python agent_deploy.py
```

#### 腳本執行流程預期

1.  腳本會首先檢查 `GEMINI_API_KEY` 和 `GITHUB_TOKEN` 是否已設定。
2.  它會自動探測您的 API Key 可用的 Gemini 模型。
3.  **Developer Agent (開發者代理)**：根據內定義的 `my_task` (例如："寫一個 Python 腳本，實作一個快速排序，然後測試")，呼叫 Gemini API 生成程式碼，並將其保存為 `generated_app.py`。
4.  **Document Agent (文件代理)**：分析 `agent_deploy.py` 本身的內容和專案目標，呼叫 Gemini API 自動生成一份描述該工具的 `README.md`，並將其保存到專案根目錄。
5.  **Release Agent (發布代理)**：
    *   將 `generated_app.py`, `agent_deploy.py` 和新的 `README.md` 添加到 Git 暫存區。
    *   提交所有更改到本地儲存庫。
    *   將提交的內容推送到您指定的 GitHub 儲存庫的 `main` 分支。
6.  您將會在終端機看到各階段的輸出信息，最終確認部署是否成功。

## 檔案結構

```
.
├── agent_deploy.py       # 核心的多代理自動化部署腳本
├── generated_app.py      # 由 Gemini 自動生成的應用程式程式碼 (例如：快速排序)
└── README.md             # 本專案的說明文件 (也可能由 agent_deploy.py 重新生成)
```

## ⚠️ 注意事項

*   請確保您的 GitHub PAT 擁有足夠的權限 (`repo` 範圍) 才能進行推送操作。
*   `agent_deploy.py` 中的 `GITHUB_USER` 和 `GITHUB_REPO` 目前是硬編碼的。在生產環境或實際應用中，建議將它們也作為環境變數進行管理，或通過命令行參數傳入。
*   每次執行 `agent_deploy.py` 都會覆蓋 `generated_app.py` 和 `README.md`。請在執行前確保您了解這一點。
*   AI 生成的內容可能不總是完美的，需要人工審查和調整。

## 🤝 貢獻

歡迎任何形式的貢獻！如果您有任何改進建議、Bug 報告或新功能想法，請隨時提交 Issue 或 Pull Request。

## 📜 授權條款

本專案採用 MIT 授權條款。詳情請見 [LICENSE](LICENSE) 檔案。

---