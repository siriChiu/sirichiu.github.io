---
title: 自我成長型 SWQA Agent：基於 Harness Engineering 的閉環品質保證系統
slug: self-growing-swqa-agent
date: 2026-05-11
categories:
- 專業技術
tags:
- SWQA
- AI Agent
- Harness Engineering
- Automation
- Gitea
- Closed-loop QA
- Testing
- CI/CD

thumbnailImagePosition: left
thumbnailImage: /postImg/swqa-agent/thumbnail.png
---

本專案是一套仍在持續演進中的 **自我成長型 SWQA agent**。它以 Harness Engineering 的思維設計，將測試案例、heartbeat 排程、Gitea issue、wiki 狀態頁、測試證據與失敗回顧整合成一個可追蹤、可重現、可逐步擴充的 closed-loop QA 系統。

<!--more-->

不同於只會定期執行腳本的傳統測試排程，這個系統的核心目標是讓 QA agent 具備「先同步、再測試、再回饋」的能力。Hermes agent 負責理解測試脈絡與決策，heartbeat 則負責週期性推進流程；每一輪都會先同步 live issue 狀態，再根據 `TEST_ITEMS.md` 與 runner registry 選出本輪 scope，最後把結果回寫到本地文件、issue 鏡像與測試總表。

---

## 📋 專案摘要 (Abstract)

這套 SWQA agent 的設計目標是建立一個可長期運作的品質保證迴路：

1. **測試項目可治理：** 以 `TEST_ITEMS.md` 作為唯一測試 inventory，避免 scope 來自零散文件或口頭記憶。
2. **Issue 狀態可同步：** Gitea issue 是 live source，每輪 heartbeat 先同步最新留言、open / closed 狀態與更新時間。
3. **測試證據可保存：** PASS 保存本地 evidence；FAIL 才更新 issue、狀態頁與 wiki。
4. **失敗能推動成長：** 對 FAIL case 做六色帽回顧，決定 `no_change`、`update_existing_tc` 或 `add_new_tc`。
5. **報告能直接回答「測了什麼」：** `Test status (Siri).md` 與 wiki 必須是整體測試總表，不只是 action log。

目前專案仍在進行中，重點放在 workflow、資料契約、狀態機與文件化規範的建立，後續會逐步接上 runner、Gitea sync adapter、wiki publisher 與 scheduler。

---

## 🛑 問題與挑戰 (The Problem)

在軟體品質保證流程中，最容易失控的不是「沒有測試」，而是測試資訊分散在太多地方：測試案例在文件裡、腳本在 repo 裡、失敗在 issue 裡、結論在留言裡、最新狀態又可能在 wiki 或口頭同步中。

這會造成幾個典型問題：

1. **Scope 不清楚：** 本輪到底跑了哪些 case？全部 inventory 有多少？哪些只是 prepared for retest？
2. **Issue 追蹤失真：** 已修正或已關閉的 issue，如果沒有先同步狀態，agent 可能重複追蹤同一條 defect。
3. **PASS / FAIL 證據不一致：** PASS 如果沒有保存本地證據，後續很難判斷是否真的驗證過。
4. **失敗不會成長成新測試：** 若 FAIL 只停在 issue filing，沒有回頭補強 test case，下一輪仍可能漏掉邊界條件。
5. **狀態頁像流水帳：** 工程師打開 status page 時，應該一眼看出 inventory total、run scope、executed count 與每個 case 的測試方法。

因此，我把這個專案定義成一個 behaviour harness，而不是單純的 cron runner。它的目的不是把腳本包起來而已，而是把測試輸入、感測資料、推論結果與回饋決策固定成一個可長期維護的閉環。

---

## 🛠️ 技術深度剖析 (Technical Deep Dive)

### 1. Harness Engineering 對齊

這個系統用 Harness Engineering 來拆解 QA agent 的責任邊界：

| Harness 元件 | 對應設計 |
| --- | --- |
| Feedforward guides | `README.md`、`TEST_ITEMS.md`、`TEST_CASE/<TC_ID>/README.md`、runner registry、測試計畫文件 |
| Computational sensors | `help_test.sh`、`diagnostic_test.sh`、`mb_test.sh`、`vm_test.sh`、`mcinfo_test.sh` 及其 stdout、rc、logs |
| Inferential sensors | `Test status (Siri).md`、`ISSUE_DOCS/*`、Gitea issue triage、六色帽回顧 |
| Maintainability sensors | `go test ./...`、`golangci-lint run`、boundary / validation tests、format gate |
| Steering loop | FAIL 後先更新 issue / status / case 文件，再決定是否新增或更新 test case |
| Harnessability | 固定 case template、runner registry、evidence 目錄與狀態輸出 |

這樣的設計讓 agent 不只會「執行」，也能知道自己是根據哪些 guide 做決策、從哪些 sensor 取得證據，以及何時該停止並要求人工確認。

### 2. Closed-loop Heartbeat 流程

每一輪 heartbeat 都遵循固定狀態機：

`Idle -> Syncing -> Selecting -> Executing -> Triaging -> Filing/Updating -> Publishing -> Retrospecting -> Done/Abort`

![Self-growing SWQA agent closed-loop heartbeat flow](/postImg/swqa-agent/closed-loop-flow.svg)

流程中的關鍵原則是 **先同步，再測試**。Gitea issue 頁面是 live 的，因此 heartbeat 不能直接沿用舊的 local snapshot。它必須先抓取最新留言、@mention、狀態、更新時間與關閉結論，寫入 `ISSUE_DOCS/<gitea_issue_id>.md`，再判斷是否仍列入 active tracking。

完成同步後，agent 才會讀取 `TEST_ITEMS.md`，透過 `TEST_CASE/runner-registry.yaml` 與 `scripts/qa_case_lookup.py` 決定本輪 runner。解析 scope 時只看測試案例表格欄位，不把 status page 或 issue mirror 當成 scope source，避免把報告內容誤判成測試清單。

### 3. 固定資料契約 (Data Contract)

為了讓系統可重現、可查詢、可維護，專案定義了固定輸入與輸出：

| 路徑 | 角色 |
| --- | --- |
| `TEST_ITEMS.md` | 全部 test case 的 inventory，也是 scope selection 的唯一來源 |
| `TEST_CASE/<TC_ID>/README.md` | 單一 test case 的方法、前置條件、預期結果 |
| `TEST_CASE/<TC_ID>/related-docs.md` | 可選的相關文件與參考連結 |
| `ISSUE_DOCS/<gitea_issue_id>.md` | Gitea issue 鏡像，只同步資訊，不寫成已執行動作 |
| `Test status (Siri).md` | 工程師可讀的整體測試總表 |
| `.qa/issue_state_snapshot.json` | issue 狀態快照 |
| `.qa/heartbeat_runs/heartbeat_latest.json` | 最新 heartbeat run 摘要 |
| `.qa/side_channel_issues.jsonl` | side channel 異常與去重來源 |

其中 `Test status (Siri).md` 是人類閱讀的核心輸出。它不能只列出「本輪做了什麼」，而要列出 `TEST_ITEMS.md` 的全部 case，並把 inventory total、run scope、executed count 分開呈現，避免把本輪執行數誤讀成全量測試數。

### 4. PASS / FAIL 與證據策略

本系統採用 fail-driven 但 evidence-first 的策略：

* **PASS：** 保存本地 evidence、case 結果與 run summary；如果相關 issue 已 closed / fixed / resolved，只做最後同步並移出 active tracking。
* **FAIL：** 更新本地 case 文件、issue 鏡像、`Test status (Siri).md` 與 wiki；必要時觸發六色帽回顧。
* **Evidence 順序固定：** `TEST_CASE` -> 測試相關文件 -> 測試腳本複本與產生檔案 -> heartbeat log。
* **Wiki fallback：** 若 Gitea wiki 不可寫，local `Test status (Siri).md` 作為 canonical 版本，並在 run summary 記錄 `wiki_synced=false`。

這個設計讓 PASS 與 FAIL 都有可追溯資料，但又避免把內部 `.qa` 路徑、run id、cron 細節或 agent 指令寫進 issue / wiki。

### 5. Gate 與風險控制

heartbeat 執行過程中有四個 gate：

1. **Pre-flight gate：** 必要檔案、權限、連線、evidence 目錄或 runner 資源未滿足時，阻擋進入執行。
2. **Revision gate：** 證據不足、失敗描述不完整、或 triage 不足以 filing 時，補正後重試，最多 3 輪。
3. **Escalation gate：** 寫入邊界不清、新失敗模式、跨 case 影響或需要人類決策時，停止並請確認。
4. **Abort gate：** 關鍵依賴失效、不可逆風險、或證據不足到不能判斷時，立即停止並保留現場。

這些 gate 讓 agent 保持自動化能力，同時避免在資訊不足時做過度推論或危險寫入。

### 6. 六色帽回顧與自我成長

這個專案的「自我成長」不是讓 agent 任意修改測試，而是讓 FAIL case 經過結構化回顧後，才決定如何擴充 test suite。

每個 FAIL 都會做 White / Red / Black / Yellow / Green / Blue 分析，最後只能產生三種結論：

* `no_change`：既有測試已足夠，不修改 `TEST_ITEMS.md`。
* `update_existing_tc`：更新既有 test case 文件與 `TEST_ITEMS.md`。
* `add_new_tc`：新增 test case 資料夾，更新 `TEST_ITEMS.md`，並納入下次 heartbeat。

這讓系統能從實際失敗中擴充正向、反向、邊界與異常測試，而不是只累積 defect tickets。

---

## 📊 目前成果與下一步 (Current Progress)

目前已完成的是整體流程設計與規格化：包含固定目錄、issue sync 規則、scope selection 規則、heartbeat 狀態機、PASS / FAIL 行為、evidence 順序、status page 要求、wiki fallback、gate 設計與六色帽回顧策略。

接下來的工程化方向包含：

1. 實作 heartbeat runner 與 scheduler，預設每 12 小時一輪，P0 每輪必跑，P1 / P2 視資源與時窗執行。
2. 建立 Gitea issue / wiki sync adapter，確保 issue mirror 只做資訊同步，不混入 agent 內部流程。
3. 完成 `TEST_CASE/runner-registry.yaml` 與 `scripts/qa_case_lookup.py` 的 runner lookup。
4. 產出可讀的 `Test status (Siri).md`，讓工程師能直接看到每個 case 的方法、輸出摘要與結果摘要。
5. 在 closed-loop QA 穩定後，再評估是否開放 remediation mode。

這個專案對我來說最重要的價值，是把 SWQA 從「定期跑腳本」推進到「可觀測、可回饋、可演進」的品質工程系統。它不只是 automation，而是一個能把失敗轉化成下一輪測試資產的 behaviour harness。
