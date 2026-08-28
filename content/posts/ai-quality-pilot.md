---
title: "AI Quality Pilot：Deterministic-first 的 AI 軟體品質保證閉環系統"
slug: ai-quality-pilot
date: 2026-08-28T00:00:00+08:00
aliases:
- /self-growing-swqa-agent/
categories:
- 專業技術
tags:
- Python
- SWQA
- AI Agent
- Test Automation
- Hermes
- Gitea
- Redmine
- Graph Engineering
- BDD
- CI/CD
- Open Source

thumbnailImagePosition: left
thumbnailImage: /postImg/ai-quality-pilot/thumbnail.png
---

**AI Quality Pilot** 是我在 **研華科技（Advantech）** 任職期間設計與開發的 AI 軟體品質保證專案。它把 Hermes 對話式 agent 與 deterministic QA engine 結合，將 issue 同步、測試案例產生、執行、證據、報告、Wiki 與修復 PR handoff 串成一個有安全閘門、可追蹤且可持續成長的閉環。

<!--more-->

![AI Quality Pilot 專案識別圖](/postImg/ai-quality-pilot/logo.svg)

> 🔗 **GitHub：** [siriChiu/quality-assurance-AI-system-testing](https://github.com/siriChiu/quality-assurance-AI-system-testing)<br>
> 🏢 **專案背景：** 研華科技（Advantech）工作期間開發<br>
> 🧰 **技術：** Python 3.10+、Hermes dynamic skill、Redmine/Gitea MCP、Pytest、BDD、Task Graph、Knowledge Graph<br>
> 📄 **授權：** MIT

本文介紹的是公開 GitHub 版本的通用架構，不包含公司內部主機、帳號、測試資料、客戶資訊或實驗室拓撲。

---

## 📋 專案摘要

AI Quality Pilot 的核心不是「讓 LLM 自由操作測試工具」，而是讓 AI 負責理解上下文與協助整理內容，所有測試真實性、狀態轉移、證據驗證與遠端寫入，仍由 deterministic engine 決定。

主要能力包含：

1. **Repo-agnostic SWQA：** 可套用到不同產品 repository，產品專屬 case、runner、rules 與 evidence 放在 host-project overlay，不污染工具本身。
2. **Issue-driven testing：** 同步 Redmine/Gitea issue，建立 canonical mapping，串起 issue ID、case ID、evidence 與 PR。
3. **Executable case generation：** 支援初始掃描、持續成長與 Redmine-linked test case，並以結構化 oracle 判定結果。
4. **Evidence-first reporting：** 保存 contract hash、stdout/stderr、assertion 結果、執行時間與報告，避免只有一句「測試通過」。
5. **Gated close loop：** Issue、Wiki、review comment 與 PR handoff 都必須經過 deterministic write gate；不可逆操作保留 human gate。
6. **Graph Engineering：** 同時使用 Task Graph 管理 agent 如何工作，並以 Knowledge Graph 建立具 provenance 的唯讀 QA 記憶模型。

---

## 🛑 為什麼需要這套系統？

傳統自動化測試通常能回答「指令有沒有跑完」，卻未必能回答下列問題：

- 這次測試是否真的使用正確 binary、fixture、版本與 target？
- Exit code 0 是否代表產品功能正確，還是只代表 help command 能執行？
- PASS 是否可以直接解讀成 workflow 完成、系統健康或允許發布？
- Redmine、Gitea、test case、evidence 與 Wiki 的狀態是否一致？
- Agent 產生的內容是否可能帶入 token、內部路徑或未授權資訊？
- 失敗後應該重跑全部流程，還是只修復受影響的節點？

如果讓 LLM 同時負責推理、執行、判定 PASS 與寫入 tracker，容易把「看似合理」誤當成「已被證據證明」。因此，我把系統切成兩層：**Hermes 提供自然語言互動與候選內容，deterministic engine 掌握 contract、truth、validation 與 write permission。**

---

## 🏗️ 系統架構：AI 協作，規則引擎掌握真實狀態

![AI Quality Pilot deterministic-first 系統架構](/postImg/ai-quality-pilot/architecture.svg)

使用者從 Hermes 輸入 `/quality-pilot ...`，dynamic skill 會收集必要上下文並呼叫 Python engine。Engine 讀取 target repository 與 `.quality-pilot-project` overlay，依固定順序完成環境檢查、scope selection、case execution、result normalization、deduplication、write gate、report 與 state persistence。

```text
Validate config → Health checks → Pull tracker state → Select scope
→ Run cases → Normalize results → Deduplicate actions → Write gate
→ Tracker write when allowed → Render reports → Persist state
```

遠端 Redmine/Gitea 操作採 MCP handoff：engine 先產生經驗證的 request payload，Hermes 再執行 MCP；engine 不保存 tracker token，也不允許 agent 跳過 gate 直接改 issue 或 Wiki。

### Host-project overlay

每個待測產品保有自己的設定與測試資產：

```text
.quality-pilot.yaml
.quality-pilot-project/
├── cases/       # executable case contracts
├── runners/     # product-specific runners
├── rules/       # domain and side-effect policies
├── state/       # generated workflow state
├── evidence/    # redacted execution evidence
└── reports/     # Markdown / JSON reports
```

這個邊界讓 AI Quality Pilot 維持通用，也避免將產品 fixture、內部 issue、主機資訊或測試紀錄誤提交到工具 repository。

---

## 🧭 四軸 Truth Model：一個 PASS 不代表全部通過

![AI Quality Pilot 四軸真實狀態模型](/postImg/ai-quality-pilot/truth-model.svg)

我將常被混在一起的狀態拆成四個獨立維度：

| 狀態軸 | 回答的問題 | 例子 |
| --- | --- | --- |
| `workflow_status` | 品質流程目前走到哪裡？ | `RUNNING`、`BLOCKED`、`HOLD`、`COMPLETED` |
| `test_outcome` | 已執行 assertion 實際觀察到什麼？ | `PASS`、`FAIL`、`BLOCK`、`HOLD`、`NOT_RUN` |
| `gate_status` | 下一個寫入或發布動作可以進行嗎？ | `ALLOWED`、`DENIED`、`NEEDS_APPROVAL` |
| `health_status` | 元件或整合健康是否被獨立檢查？ | `HEALTHY`、`DEGRADED`、`NOT_EVALUATED` |

例如，一條 command assertion 可以 PASS，但若環境證據不足、coverage 太淺或 remote write 尚未核准，workflow 仍可能是 `BLOCKED/HOLD`，gate 也不能放行。只有 partial probe 時，觀察結果會保留在 `probe_outcome`，正式 `test_outcome` 仍是 `HOLD`，避免以淺層探針製造假 PASS。

---

## 🕸️ Graph Engineering：Task Graph 與 Knowledge Graph

這個專案採用 Graph Engineering 的雙圖設計，但兩者的責任完全不同。

### 1. Task Graph：agent 如何工作

Task Graph 將工作拆成具明確 dependency 的 DAG：

```text
Scoped Context → Node Contract → Parallel Workers → Independent Verifier
→ Single Merge Owner → Human Gate → Checkpoint → Targeted Repair / Resume
```

核心設計包括：

- 每個 node 只取得允許相信的 scoped context，不能任意讀取所有秘密與歷史對話。
- Contract 明確定義 required input/output、validator、owner、side-effect boundary 與 repair policy。
- 無相依性的 case 可以 bounded parallel 執行；verifier 必須與 worker 分離，避免自我驗證。
- 每個 artifact 只有一個 writer，防止平行工作互相覆蓋。
- 節點失敗時，只 invalidate 該節點與 descendants，保留其他已驗證 checkpoint。
- Publish、tracker write 或 PR 等不可逆操作前才加入 human gate。

### 2. Knowledge Graph：agent 記住什麼

Knowledge Graph 是具 provenance 的 QA read model：SQLite 作為 canonical store，JSON 作為可攜式輸出。Entity、relation 與 event 都必須包含來源、時間、信心值與 evidence；ontology 會檢查型別、domain/range 與 event schema。

Knowledge Graph 可以回答「哪個 run 產生了這個 case 的 evidence」等追蹤問題，但 graph node 數量、查詢成功或 extraction confidence **都不能直接產生 QA PASS、READY、APPROVED 或 MERGE_ALLOWED**。Source system 與 deterministic QA artifacts 仍是權威來源。

---

## 🔄 Evidence-driven Close Loop

![AI Quality Pilot evidence-driven close-loop lifecycle](/postImg/ai-quality-pilot/close-loop.svg)

整體 lifecycle 使用以下語彙：

```text
Observe → Normalize → Execute → Triage → Publish → Evolve → Prune
```

1. **Observe：** 讀取 repository、近期變更、Redmine/Gitea issue、PR、既有 cases、latest run 與 environment profile。
2. **Normalize：** 建立 canonical issue mapping、去重、確認 scope 與 executable contract。
3. **Execute：** 先做 environment preflight，再以 runner 執行 structured assertions，保存 evidence 與 contract hash。
4. **Triage：** 分離 PASS、FAIL、BLOCK、HOLD，檢查 evidence freshness、coverage 與四軸 truth。
5. **Publish：** 通過 gate 後，才產生 Gitea issue update、Wiki status、advisory review comment 或 PR handoff。
6. **Evolve：** 依新的 code、issue、run 與 failure signal 產生 growing cases，修正後再進入 retest。
7. **Prune：** 移除 closed/resolved issue 的 active tracking，清理 duplicate 與 stale state。

`close-loop heartbeat` 是一次 sensor-driven tick：有新工作時只執行新產生或明確選定的 cases；沒有新 signal 時回報 `idle`。排程由 Hermes 或外部 scheduler 觸發，工具不會私自安裝背景 timer。

---

## 🧪 測試案例、Oracle 與 Evidence

Case generation 分成三種入口：

- `--init`：第一次分析產品 repo，以分層方式建立可執行的初始 cases。
- `--growing`：根據 issue、commit、PR、latest run 與既有 coverage 產生新增 cases，並避免 duplicate command 消耗新增額度。
- `--redmine-issues`：從 Redmine MCP snapshot 建立 linked cases，串回 Gitea 與 evidence mapping。

每個 case 不是只有一條 shell command，而是包含環境需求、side-effect boundary 與 structured assertions。第一版 oracle 可檢查：

- Exit status
- stdout / stderr 的 contains、regex、equals
- Duration bounds
- Assertion ID 與 oracle result
- Contract hash 與 evidence freshness

對需要真實產品環境的 case，系統會先檢查 local/remote mode、entrypoint、fixture、credential environment variable、target 與執行權限。缺少必要資訊時回 `BLOCK`，而不是執行一個替代命令再錯誤宣稱 PASS。

---

## 🔍 PR Review 與真實產品測試

`review pr` 會 pin 住 PR head SHA，建立 detached worktree，重建必要 diff，選擇 repository regression suite，並將 evidence 綁定到該版本。Comprehensive mode 會分別呈現 black-box、white-box、functional、boundary、stress 與 documentation 維度；changed-file-driven oracle 只有在對應 product test 實際成功後才算 evidence。

Product build、product operation 與 browser UI 是不同 cases：

- Build 必須在 disposable writable copy 中產生真實 artifact。
- Product operation 必須具 semantic assertion；只有 exit code 的 probe 維持 `HOLD`。
- Web UI 使用真實 Playwright interaction 與 positive UI assertion，不以 curl、mock DOM 或 API probe 假裝 browser test。
- 缺少 dependency、browser、server、fixture 或 oracle 時，回報 `BLOCK/HOLD`，不誤判為產品 `FAIL/PASS`。

Review 的遠端輸出只準備 advisory `COMMENT`；最終 `COMMENT / REQUEST_CHANGES / APPROVED` 仍由使用者決定。

---

## 🔐 安全與寫入邊界

為了讓 agent 能進入實際工程流程，又不取得過度權限，我加入以下安全設計：

1. **Deterministic write gate：** 檢查 target state、contract match、evidence freshness 與 secret leakage，通過後才可建立遠端 handoff。
2. **Secret fail-closed：** Token、password、private key、PII、內部路徑與高熵字串在 context、evidence、graph 與 remote payload 邊界統一檢測與遮罩。
3. **No direct tracker token：** Engine 不保存 Gitea/Redmine token，由 Hermes MCP 執行已核准 request。
4. **Safe command execution：** Product/review command 使用 allowlisted argv 與 `shell=False`；README command 只有經使用者確認後才能執行。
5. **Environment authorization：** 系統記錄 credential **環境變數名稱**、target env name 與 side-effect boundary，不保存秘密值，也不把 repo 推論冒充使用者授權。
6. **Human-owned irreversible actions：** Wiki apply、issue write、review reply 與 PR handoff 都保留可檢查的 payload、ledger 與人工決策點。

---

## 📊 目前完成度與誠實邊界

AI Quality Pilot 目前是 **partial close loop**，公開文件以 capability matrix 明確區分 Supported、Partial 與 Planned，避免把 roadmap 當成已完成能力。

| 狀態 | 目前範圍 |
| --- | --- |
| **Supported / first slice** | Hermes skill 與 dispatcher、setup/doctor/audit、environment preflight、init/growing cases、structured assertions、evidence/contract hash、四軸 truth、single-tick heartbeat、Task Graph 核心、local Knowledge Graph |
| **Partial** | Redmine/Gitea 全流程同步與 reconciliation、完整 A0–A8 resumable loop、risk-based PASS/HOLD gate、PR review 的產品專屬 adapter、post-fix 自動 retest |
| **Planned** | 深度 mutation/fuzz/security/load/soak、完整 UI 與 distributed-system strategy、remote GraphRAG、跨程序 scheduler supervision |

這種標示方式本身也是品質工程的一部分：**功能存在、測試通過與可安全用於正式決策，是三件不同的事。**

---

## 🛠️ 技術棧與我的工程貢獻

- **Language / Package：** Python 3.10+、setuptools、PyYAML
- **Testing：** Pytest、unittest、BDD/Gherkin、structured oracle
- **Agent integration：** Hermes dynamic skill、MCP handoff、candidate-only subagent boundary
- **Workflow：** Task Graph DAG、bounded parallel execution、checkpoint、targeted repair、human gate
- **Knowledge：** SQLite、JSON、ontology validation、provenance、reversible fusion
- **Trackers / Delivery：** Redmine、Gitea Issue、Wiki、PR review and repair handoff
- **Browser / Runtime：** Playwright、local/remote environment profile、bounded PTY/TUI probe
- **Security：** Redaction、secret detection、contract hash、write ledger、allowlisted argv

我負責將需求整理成系統架構與 contract，實作 Python engine、CLI/Hermes command surface、case/evidence pipeline、Task/Knowledge Graph、issue/Wiki/PR gate，並以 BDD 與自動化測試持續驗證狀態語意及安全邊界。

---

## 💡 專案心得

這個專案讓我重新思考 AI 在 SWQA 中最適合的位置。AI 很適合讀懂大量上下文、找出候選風險、協助產生 case 與人類可讀報告；但 PASS、證據有效性、遠端寫入與 release decision 不應只依賴模型的自然語言結論。

因此，AI Quality Pilot 最重要的設計不是「更自主」，而是 **可驗證、可恢復、可稽核，而且知道何時必須停下來請人決定**。這也是我在研華工作期間，將測試自動化進一步推向 AI-assisted Quality Engineering 的實作。

> **查看原始碼與完整文件：** [https://github.com/siriChiu/quality-assurance-AI-system-testing](https://github.com/siriChiu/quality-assurance-AI-system-testing)
