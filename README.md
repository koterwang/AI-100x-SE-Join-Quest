# 水球軟體學院BDDxAI自動開發 的測試練習

本專案為「水球軟體學院」AI 驅動 BDD（行為驅動開發）自動化開發流程的實作練習，主題為中國象棋規則驗證。

---

## 專案特色
- 以 BDD（Behave）描述所有棋子移動、勝負等規則，確保規則正確性。
- 所有邏輯集中於 `src/Chess.py`，步驟定義於 `features/steps/chess_steps.py`。
- 每個 scenario 皆經過紅燈（fail）→ 綠燈（pass）循環，並逐步重構至完整象棋規則。
- 支援紅黑雙方、所有棋子、勝負情境，並可自動驗證所有規則。

---

## 開發環境
- **Python 3.11**
- **Behave**（行為驅動測試框架）
- **IDE：Cursor**（AI 輔助開發）
- 作業系統：Windows 10

---

## 專案結構
```
trial_chess/
  ├── src/
  │   └── Chess.py         # 象棋規則主程式
  ├── features/
  │   ├── chess.feature    # BDD 規則描述
  │   └── steps/
  │       └── chess_steps.py # BDD 步驟定義
  └── README.md
```

---

## 如何執行測試
1. 安裝依賴：
   ```sh
   pip install behave
   ```
2. 在專案根目錄執行：
   ```sh
   behave
   ```
3. 可用 `--tags` 執行特定 scenario，例如：
   ```sh
   behave --tags=Rook
   ```

---

## 主要技術說明
- **Python**：負責所有象棋規則與邏輯實作。
- **Behave**：以 Gherkin 語法撰寫 feature，確保每個規則皆有自動化測試。
- **Cursor IDE**：AI 輔助程式撰寫與重構，大幅提升開發效率。

---

## 聯絡/貢獻
歡迎 fork、star 或提出 issue 討論。

---

> 本專案為 AI 驅動 BDD 實作範例，適合軟體測試、AI 輔助開發、規則驗證等主題學習參考。 