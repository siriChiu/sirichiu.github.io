---
title: "Self-Growing SWQA Agent: A Closed-Loop Quality System Based on Harness Engineering"
slug: self-growing-swqa-agent
date: 2026-05-11
categories:
- Professional Technology
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

This ongoing project is a **self-growing SWQA agent** designed with Harness Engineering principles. It integrates test cases, heartbeat scheduling, Gitea issues, wiki status pages, test evidence, and failure retrospectives into a traceable, reproducible, and continuously expandable closed-loop QA system.

<!--more-->

Unlike a traditional test scheduler that only executes scripts periodically, this system is designed to synchronize first, test second, and then feed the result back into the quality loop. The Hermes agent handles context understanding and decision-making, while the heartbeat process advances the workflow on a fixed cadence. Each run synchronizes live issue states first, selects the run scope from `TEST_ITEMS.md` and the runner registry, and then writes results back to local documents, issue mirrors, and the test status page.

---

## 📋 Project Abstract

The goal of this SWQA agent is to build a long-running quality assurance loop:

1. **Governable test inventory:** `TEST_ITEMS.md` is the single source of truth for all test cases.
2. **Synchronized issue state:** Gitea issues are live sources; every heartbeat synchronizes comments, open / closed state, and updated timestamps first.
3. **Persistent test evidence:** PASS results keep local evidence; FAIL results update issues, status pages, and wiki content.
4. **Failure-driven growth:** Failed cases go through a six-thinking-hats retrospective and end with `no_change`, `update_existing_tc`, or `add_new_tc`.
5. **Readable reporting:** `Test status (Siri).md` and the Gitea wiki must answer "what was tested" directly, instead of becoming action logs.

The project is still in progress. The current focus is the workflow, data contracts, state machine, and documentation structure. The next stage is to connect runners, Gitea sync adapters, wiki publishing, and scheduling.

---

## 🛑 Problem Statement

In software quality assurance, the hardest part is often not the lack of tests, but the fragmentation of testing information. Test cases live in documents, scripts live in the repository, failures live in issues, conclusions live in comments, and the latest status may be on a wiki page or in a team discussion.

This creates several recurring problems:

1. **Unclear scope:** Which cases were executed in this run? How many cases exist in the full inventory? Which cases were only prepared for retest?
2. **Stale issue tracking:** If the agent does not synchronize the latest issue state first, it may continue tracking a defect that has already been fixed or closed.
3. **Inconsistent PASS / FAIL evidence:** Without local evidence for PASS results, it becomes difficult to prove what was actually verified later.
4. **Failures do not improve the suite:** If a failure only creates an issue but never improves the test inventory, the same boundary may remain under-tested.
5. **Status pages become logs:** Engineers should be able to open the status page and immediately see inventory total, run scope, executed count, method summary, and result summary per case.

For this reason, I define this project as a behaviour harness, not just a cron-based runner. Its purpose is to stabilize the inputs, sensors, inference outputs, and steering decisions of QA into a maintainable closed loop.

---

## 🛠️ Technical Deep Dive

### 1. Mapping to Harness Engineering

The system uses Harness Engineering to define the responsibility boundaries of the QA agent:

| Harness Element | System Mapping |
| --- | --- |
| Feedforward guides | `README.md`, `TEST_ITEMS.md`, `TEST_CASE/<TC_ID>/README.md`, runner registry, test plan documents |
| Computational sensors | `help_test.sh`, `diagnostic_test.sh`, `mb_test.sh`, `vm_test.sh`, `mcinfo_test.sh`, plus stdout, return codes, and logs |
| Inferential sensors | `Test status (Siri).md`, `ISSUE_DOCS/*`, Gitea issue triage, six-thinking-hats retrospectives |
| Maintainability sensors | `go test ./...`, `golangci-lint run`, boundary / validation tests, format gates |
| Steering loop | After FAIL, update issue / status / case documents first, then decide whether to update or add test cases |
| Harnessability | Fixed case templates, runner registry, evidence directories, and structured status outputs |

With this structure, the agent does not merely execute commands. It understands which guides it follows, which sensors provide evidence, and when it must stop for human confirmation.

### 2. Closed-Loop Heartbeat Workflow

Each heartbeat follows a fixed state machine:

`Idle -> Syncing -> Selecting -> Executing -> Triaging -> Filing/Updating -> Publishing -> Retrospecting -> Done/Abort`

![Self-growing SWQA agent closed-loop heartbeat flow](/postImg/swqa-agent/closed-loop-flow.svg)

The key principle is **synchronize first, test second**. Since Gitea issues are live, the heartbeat cannot rely only on an old local snapshot. It first fetches the latest comments, mentions, state, updated timestamp, and closing conclusion, then writes them into `ISSUE_DOCS/<gitea_issue_id>.md` before deciding whether the issue still belongs to active tracking.

After synchronization, the agent reads `TEST_ITEMS.md` and uses `TEST_CASE/runner-registry.yaml` plus `scripts/qa_case_lookup.py` to select the runners for the current run. Scope parsing only reads test-case table fields, not status pages or issue mirrors, so report content is never mistaken for inventory data.

### 3. Fixed Data Contract

The project defines fixed inputs and outputs to keep the system reproducible and maintainable:

| Path | Role |
| --- | --- |
| `TEST_ITEMS.md` | Full test inventory and the only source for scope selection |
| `TEST_CASE/<TC_ID>/README.md` | Method, prerequisites, and expected result for one test case |
| `TEST_CASE/<TC_ID>/related-docs.md` | Optional references and related documents |
| `ISSUE_DOCS/<gitea_issue_id>.md` | Gitea issue mirror; synchronization only, not action narration |
| `Test status (Siri).md` | Engineer-readable overall test status table |
| `.qa/issue_state_snapshot.json` | Issue state snapshot |
| `.qa/heartbeat_runs/heartbeat_latest.json` | Latest heartbeat run summary |
| `.qa/side_channel_issues.jsonl` | Side-channel anomalies and deduplication source |

`Test status (Siri).md` is the most important human-readable output. It should list all cases from `TEST_ITEMS.md`, group similar tests together, and separately report inventory total, run scope, and executed count. This prevents readers from confusing the current run scope with the entire test inventory.

### 4. PASS / FAIL and Evidence Strategy

The system uses a fail-driven but evidence-first strategy:

* **PASS:** Store local evidence, case result, and run summary. If the related issue is already closed, fixed, or resolved, only perform the final synchronization and remove it from active tracking.
* **FAIL:** Update the local case document, issue mirror, `Test status (Siri).md`, and wiki. Trigger a retrospective when needed.
* **Fixed evidence order:** `TEST_CASE` -> test-related documents -> script copies and generated artifacts -> heartbeat log.
* **Wiki fallback:** If the Gitea wiki is unavailable or not writable, local `Test status (Siri).md` remains the canonical status page and the run summary records `wiki_synced=false`.

This keeps PASS and FAIL results traceable while avoiding internal `.qa` paths, run IDs, cron details, or agent instructions in issue and wiki content.

### 5. Gates and Risk Control

The heartbeat process includes four gates:

1. **Pre-flight gate:** Blocks execution when required files, permissions, connectivity, evidence directories, or runner resources are missing.
2. **Revision gate:** Retries up to three times when evidence is insufficient, failure descriptions are incomplete, or triage is not ready for filing.
3. **Escalation gate:** Stops for confirmation when write boundaries are unclear, a new failure mode appears, cross-case impact is possible, or human judgment is required.
4. **Abort gate:** Stops immediately and preserves the scene when critical dependencies fail, irreversible risk appears, or evidence is too weak to support a conclusion.

These gates allow automation to move quickly while preventing the agent from overreaching when the available information is not strong enough.

### 6. Six-Thinking-Hats Retrospective and Self-Growth

The "self-growing" part of this project does not mean the agent freely rewrites tests. Instead, every failed case goes through a structured retrospective before the test suite changes.

Each FAIL case is analyzed through White / Red / Black / Yellow / Green / Blue perspectives, and the final decision must be one of three outcomes:

* `no_change`: The current test case is sufficient; `TEST_ITEMS.md` stays unchanged.
* `update_existing_tc`: Update the existing test case document and `TEST_ITEMS.md`.
* `add_new_tc`: Add a new test case folder, update `TEST_ITEMS.md`, and include it in the next heartbeat.

This turns real failures into stronger positive, negative, boundary, and exception tests instead of simply accumulating defect tickets.

---

## 📊 Current Progress and Next Steps

The current work has completed the workflow design and specification: fixed directories, issue synchronization rules, scope selection rules, heartbeat state machine, PASS / FAIL behavior, evidence ordering, status page requirements, wiki fallback, gate design, and six-thinking-hats retrospective strategy.

Next engineering steps:

1. Implement the heartbeat runner and scheduler, with a default 12-hour cadence. P0 runs every cycle, P1 runs based on resources and time window, and P2 runs only when there is spare capacity.
2. Build the Gitea issue / wiki sync adapter while keeping issue mirrors as synchronization records only.
3. Complete `TEST_CASE/runner-registry.yaml` and `scripts/qa_case_lookup.py` for runner lookup.
4. Generate a readable `Test status (Siri).md` that shows method, output summary, and result summary for every case.
5. After the closed-loop QA flow is stable, evaluate whether to enable a remediation mode.

For me, the most important value of this project is moving SWQA from "periodically running scripts" toward a quality engineering system that is observable, feedback-driven, and able to evolve. It is not just automation; it is a behaviour harness that turns failures into better test assets for the next run.
