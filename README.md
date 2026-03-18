好的，這是一份為您的專案編寫的 `README.md`，內容包含了專案簡介、如何執行、增量開發特色，並特別提及了這次新增的『快速排序』函數。

```markdown
# AI 增量開發代理 (AI Incremental Development Agent)

這是一個基於 AI 的自動化開發代理，旨在實現 Python 應用程式的增量開發和自動部署。它利用 Google Gemini 模型來生成、修改和優化代碼，並透過 Git 自動將更新同步到 GitHub 儲存庫。這個代理的核心功能是能夠理解現有代碼，並在此基礎上逐步添加新功能，大大提升開發效率和專案管理。

## ✨ 特色

*   **AI 驅動代碼生成與修改**：利用 Gemini 模型根據任務描述生成新的 Python 代碼，或在現有代碼基礎上進行修改。
*   **增量開發支援**：代理能夠讀取 `generated_app.py` 中的現有代碼，並在不破壞舊功能的前提下，增量地添加新功能。
*   **自動化 GitHub 部署**：每次成功執行後，代理會自動將更新後的代碼 (`generated_app.py`)、代理腳本本身 (`agent_deploy.py`) 和 `README.md` 推送到指定的 GitHub 儲存庫。
*   **自動 README 更新**：能夠根據最新的任務和專案狀態自動更新 `README.md` 文件。

## 🛠️ 前置條件

在執行此代理之前，請確保您的系統已安裝以下軟體和庫：

*   **Python 3.x**
*   **pip** (Python 套件管理器)
*   **Git** (版本控制系統，用於與 GitHub 互動)
*   **Python 庫**：
    ```bash
    pip install requests GitPython
    ```

## ⚙️ 設定環境變數

您需要設定以下環境變數，以便代理能夠正確地與 Google Gemini API 和 GitHub 互動：

1.  **`GEMINI_API_KEY`**：您的 Google Gemini API 金鑰。
    *   獲取方式：[Google AI Studio](https://makersuite.google.com/app/apikey)
2.  **`GITHUB_TOKEN`**：您的 GitHub 個人訪問令牌 (Personal Access Token, PAT)。需要 `repo` 權限。
    *   獲取方式：[GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens)
3.  **`GITHUB_USER`**：您的 GitHub 用戶名 (例如: `bradzhan2023`)。
4.  **`GITHUB_REPO`**：您希望部署代碼的 GitHub 儲存庫名稱 (例如: `ai-agent-test`)。

**範例 (`.bashrc` 或 `.zshrc`):**
```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
export GITHUB_TOKEN="YOUR_GITHUB_PAT_HERE"
export GITHUB_USER="bradzhan2023" # 請替換為您的 GitHub 用戶名
export GITHUB_REPO="ai-agent-test" # 請替換為您的儲存庫名稱
```
設定完成後，請記得執行 `source ~/.bashrc` 或 `source ~/.zshrc` 使其生效。

## 🚀 如何執行

1.  **克隆專案 (如果尚未克隆):**
    ```bash
    git clone https://github.com/bradzhan2023/ai-agent-test.git # 請替換為您的實際 repo URL
    cd ai-agent-test
    ```
    (如果專案已存在於本地，只需進入該目錄即可。)

2.  **執行代理腳本:**
    ```bash
    python agent_deploy.py
    ```

**如何指定任務:**
您可以打開 `agent_deploy.py` 檔案，在 `if __name__ == "__main__":` 區塊中找到 `my_task` 變數，並修改其值來指定您希望 AI 代理執行的任務。

```python
# agent_deploy.py 檔案內部
if __name__ == "__main__":
    # --- 你可以隨時修改這裡的任務內容 ---
    my_task = "新增一個計算質數的函數" # 修改這裡的任務
    # ...
```

## 💡 『增量開發』特色

本專案最核心的亮點是其對『增量開發』的強大支援。這意味著：

1.  **理解現有代碼**：當您第二次或之後執行 `agent_deploy.py` 時，它會自動讀取 `generated_app.py` 中已存在的代碼。
2.  **智能合併與新增**：AI 代理（透過 `developer_agent_incremental` 函數）會分析您提供的最新任務，並在保留所有舊功能的前提下，將新功能智能地整合到現有代碼中。它會嘗試避免衝突，並生成一個包含所有功能（舊有和新增）的完整代碼文件。
3.  **無縫迭代**：您無需手動合併代碼或擔心覆蓋之前的開發成果。只需修改 `my_task` 變數，代理就會處理其餘部分，使開發流程更加流暢和高效。
4.  **持續演進**：專案可以像樂高積木一樣，不斷地疊加新的功能，每一次迭代都基於前一次的成果，實現真正的持續開發和演進。

## 🆕 本次 AI 代理已完成的任務：

本次執行中，AI 代理被指示執行以下任務：`新增一個泡沫排序 (Quick Sort) 的函數`。

根據此任務，AI 代理會分析 `generated_app.py` 中的現有代碼（如果存在），並在其基礎上添加一個名為 `quick_sort` 的函數。以下是預期會被生成或修改到 `generated_app.py` 中的代碼片段：

```python
def quick_sort(arr):
    """
    使用快速排序 (Quick Sort) 算法對列表進行排序。
    這個函數會遞迴地將列表分割成較小和較大的子列表，然後進行合併。
    """
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2] # 選擇中間元素作為基準點
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# 示例用法 (此部分可能不會直接生成在 generated_app.py 中，但可用於測試)
# if __name__ == "__main__":
#     my_list = [3, 6, 8, 10, 1, 2, 1]
#     sorted_list = quick_sort(my_list)
#     print(f"原始列表: {my_list}")
#     print(f"排序後列表: {sorted_list}") # 輸出: [1, 1, 2, 3, 6, 8, 10]
```
這個 `quick_sort` 函數採用了經典的快速排序遞迴實現，能夠高效地對數字列表進行排序。AI 代理將會確保此函數與專案中的其他功能兼容，並被整合到 `generated_app.py` 中。
```