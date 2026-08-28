---
title: "AI Quality Pilot: A Deterministic-First AI Software QA Closed-Loop System"
slug: ai-quality-pilot
date: 2026-08-28T00:00:00+08:00
aliases:
- /en/self-growing-swqa-agent/
categories:
- Professional Technology
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

**AI Quality Pilot** is an AI-assisted software quality assurance project I designed and developed while working at **Advantech**. It combines a conversational Hermes agent with a deterministic QA engine, connecting issue synchronization, executable test-case generation, evidence, reporting, Wiki publishing, and repair PR handoff into a traceable, gated, and continuously evolving loop.

<!--more-->

![AI Quality Pilot project identity](/postImg/ai-quality-pilot/logo.svg)

> 🔗 **GitHub:** [siriChiu/quality-assurance-AI-system-testing](https://github.com/siriChiu/quality-assurance-AI-system-testing)<br>
> 🏢 **Project context:** Developed during my work at Advantech<br>
> 🧰 **Technology:** Python 3.10+, Hermes dynamic skill, Redmine/Gitea MCP, Pytest, BDD, Task Graph, and Knowledge Graph<br>
> 📄 **License:** MIT

This post describes the generic public GitHub version. It contains no internal company hosts, accounts, test data, customer information, or lab topology.

---

## 📋 Project Abstract

The central idea is not to let an LLM freely operate the QA lifecycle. AI helps interpret context and draft candidate content, while a deterministic engine remains responsible for test truth, state transitions, evidence validation, and remote-write authorization.

The main capabilities are:

1. **Repository-agnostic SWQA:** Product-specific cases, runners, rules, and evidence live in a host-project overlay rather than contaminating the tool repository.
2. **Issue-driven testing:** Redmine and Gitea state is synchronized into a canonical mapping that connects issue IDs, case IDs, evidence, and pull requests.
3. **Executable case generation:** Initial, growing, and Redmine-linked cases use structured oracles instead of relying only on process exit codes.
4. **Evidence-first reporting:** Contract hashes, assertion results, stdout/stderr, duration, and reports preserve what was actually verified.
5. **Gated close loop:** Issue, Wiki, review-comment, and PR handoffs pass through deterministic write gates, with human gates for irreversible actions.
6. **Graph Engineering:** A Task Graph controls how agents work, while a provenance-backed Knowledge Graph provides a read-only QA memory model.

---

## 🛑 Why Build This System?

Traditional automation can often answer whether a command finished, but not necessarily whether:

- The correct binary, fixture, version, and target were used.
- Exit code 0 proved product behavior rather than only a shallow help probe.
- PASS also means workflow completion, system health, or publication permission.
- Redmine, Gitea, test cases, evidence, and Wiki state agree.
- Agent-generated output leaks tokens, internal paths, or restricted information.
- A failure should restart the entire workflow or only invalidate affected nodes.

Allowing an LLM to reason, execute, declare PASS, and update trackers creates a risk that plausible language will be mistaken for verified truth. I therefore separated the system into two layers: **Hermes provides natural-language interaction and candidate assistance; the deterministic engine owns contracts, validation, truth, and write permission.**

---

## 🏗️ Architecture: AI-Assisted, Deterministic at the Truth Boundary

![AI Quality Pilot deterministic-first architecture](/postImg/ai-quality-pilot/architecture.svg)

Users enter `/quality-pilot ...` in Hermes. The dynamic skill collects the required context and invokes the Python engine. The engine reads the target repository and its `.quality-pilot-project` overlay, then follows a fixed order for environment checks, scope selection, execution, result normalization, deduplication, write gating, reporting, and state persistence.

```text
Validate config → Health checks → Pull tracker state → Select scope
→ Run cases → Normalize results → Deduplicate actions → Write gate
→ Tracker write when allowed → Render reports → Persist state
```

Remote Redmine/Gitea operations use MCP handoff files. The engine first creates a validated request payload; Hermes then performs the MCP action. The engine stores no tracker token, and the agent cannot bypass the gate to update an issue or Wiki page directly.

### Host-project overlay

Each product repository owns its testing assets:

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

This boundary keeps the toolkit generic and prevents fixtures, internal issues, host information, and runtime evidence from being accidentally committed to the tool repository.

---

## 🧭 Four-Axis Truth Model

![AI Quality Pilot four-axis truth model](/postImg/ai-quality-pilot/truth-model.svg)

I separated four questions that are often collapsed into one status:

| Axis | Question | Examples |
| --- | --- | --- |
| `workflow_status` | Where is the lifecycle now? | `RUNNING`, `BLOCKED`, `HOLD`, `COMPLETED` |
| `test_outcome` | What did the executed assertions observe? | `PASS`, `FAIL`, `BLOCK`, `HOLD`, `NOT_RUN` |
| `gate_status` | May the next write or publication happen? | `ALLOWED`, `DENIED`, `NEEDS_APPROVAL` |
| `health_status` | Was component or integration health checked independently? | `HEALTHY`, `DEGRADED`, `NOT_EVALUATED` |

A command assertion can pass while the workflow remains blocked because evidence is insufficient, coverage is shallow, or a remote write is not approved. Runs containing only partial probes preserve observations in `probe_outcome`, while the official `test_outcome` remains `HOLD`; a shallow probe cannot manufacture an official PASS.

---

## 🕸️ Graph Engineering: Task Graph and Knowledge Graph

The project applies both halves of Graph Engineering, but they have different responsibilities.

### 1. Task Graph: how agents work

```text
Scoped Context → Node Contract → Parallel Workers → Independent Verifier
→ Single Merge Owner → Human Gate → Checkpoint → Targeted Repair / Resume
```

Key rules include:

- Each node receives only the scoped context it is allowed to trust.
- Contracts define inputs, outputs, validators, ownership, side-effect boundaries, and repair policies.
- Independent cases may run with bounded parallelism, while a separate verifier prevents self-validation.
- Each artifact has one writer to avoid parallel overwrite conflicts.
- A failed node invalidates only itself and its descendants; unrelated verified checkpoints remain reusable.
- Human gates are placed before irreversible publication, tracker writes, and PR actions rather than before every read-only step.

### 2. Knowledge Graph: what agents remember

The Knowledge Graph is a provenance-backed QA read model. SQLite is the canonical store and JSON is the portable export. Entities, relations, and events require sources, timestamps, confidence, and evidence; ontology validation enforces types, domain/range constraints, and event schemas.

It can answer traceability questions such as “Which run produced evidence for this case?” However, graph counts, successful queries, and extraction confidence **cannot produce QA PASS, READY, APPROVED, or MERGE_ALLOWED**. Source systems and deterministic QA artifacts remain authoritative.

---

## 🔄 Evidence-Driven Close Loop

![AI Quality Pilot evidence-driven close-loop lifecycle](/postImg/ai-quality-pilot/close-loop.svg)

The lifecycle follows:

```text
Observe → Normalize → Execute → Triage → Publish → Evolve → Prune
```

1. **Observe:** Read repository changes, Redmine/Gitea issues, PRs, cases, latest runs, and the environment profile.
2. **Normalize:** Build canonical issue mappings, deduplicate actions, select scope, and validate executable contracts.
3. **Execute:** Run environment preflight and structured assertions, then store evidence and contract identity.
4. **Triage:** Separate PASS, FAIL, BLOCK, and HOLD while checking evidence freshness, coverage, and the four truth axes.
5. **Publish:** Only gated actions may produce issue updates, Wiki status, advisory review comments, or PR handoffs.
6. **Evolve:** Generate growing cases from new code, issues, runs, and failures, then re-enter retesting after repair.
7. **Prune:** Remove closed/resolved items from active tracking and clean up duplicate or stale state.

`close-loop heartbeat` is one sensor-driven tick. It executes newly generated or explicitly selected work and reports `idle` when there is no new signal. Hermes or an external scheduler triggers future ticks; the tool does not silently install a background timer.

---

## 🧪 Test Cases, Oracles, and Evidence

Case generation provides three entry points:

- `--init` analyzes a product repository and produces an initial stratified set of executable cases.
- `--growing` uses issues, commits, PRs, latest runs, and existing coverage to propose new cases without allowing duplicate commands to consume the new-case budget.
- `--redmine-issues` creates linked cases from Redmine MCP snapshots and connects them to Gitea and evidence mappings.

A case contains more than a shell command. It includes environment requirements, side-effect boundaries, and structured assertions. The first supported oracle slice covers exit status, stdout/stderr contains/regex/equals checks, duration bounds, assertion IDs, oracle results, contract hashes, and evidence freshness.

Prepared-environment cases first validate local/remote mode, entrypoint, fixtures, credential environment variables, targets, and authorization. Missing requirements yield `BLOCK` rather than running a substitute command and incorrectly reporting PASS.

---

## 🔍 PR Review and Real Product Testing

`review pr` pins a PR head SHA, creates a detached worktree, reconstructs the required diff, selects repository regression tests, and binds evidence to that source identity. Comprehensive mode reports black-box, white-box, functional, boundary, stress, and documentation dimensions separately. A changed-file-driven oracle becomes evidence only after its mapped product test actually runs successfully.

Product build, product operation, and browser UI are independent cases:

- A build must create a real artifact in a disposable writable copy.
- A product operation needs a semantic assertion; exit-only probes remain `HOLD`.
- Web testing uses real Playwright interaction and positive UI assertions, with no curl, mock-DOM, or API fallback pretending to be a browser test.
- Missing dependencies, browser, server, fixture, or oracle result in `BLOCK/HOLD`, not a false product `FAIL/PASS`.

Remote review output is advisory `COMMENT` only. The user retains ownership of the final `COMMENT`, `REQUEST_CHANGES`, or `APPROVED` decision.

---

## 🔐 Security and Write Boundaries

The following controls allow the agent to participate in engineering workflows without receiving excessive authority:

1. **Deterministic write gate:** Checks target state, contract match, evidence freshness, and secret leakage before creating a remote handoff.
2. **Fail-closed secret handling:** Tokens, passwords, private keys, PII, local paths, and high-entropy payloads are detected and redacted at context, evidence, graph, and remote-write boundaries.
3. **No direct tracker tokens:** The engine stores no Gitea/Redmine token; Hermes MCP applies approved requests.
4. **Safe command execution:** Product and review commands use allowlisted argv with `shell=False`; README commands require explicit user approval.
5. **Environment authorization:** Profiles store credential **environment-variable names**, target env names, and side-effect boundaries—not secret values—and repository inference never substitutes for user authorization.
6. **Human-owned irreversible actions:** Wiki apply, issue writes, review replies, and PR handoffs retain inspectable payloads, ledgers, and human decision points.

---

## 📊 Current Scope and Honest Boundaries

AI Quality Pilot is currently a **partial close loop**. Its public capability matrix distinguishes Supported, Partial, and Planned work so roadmap design is not misrepresented as implemented behavior.

| Status | Current scope |
| --- | --- |
| **Supported / first slice** | Hermes skill and dispatcher, setup/doctor/audit, environment preflight, init/growing cases, structured assertions, evidence and contract hashes, four-axis truth, single-tick heartbeat, Task Graph core, and local Knowledge Graph |
| **Partial** | End-to-end Redmine/Gitea reconciliation, a fully resumable A0–A8 loop, deep risk-based PASS/HOLD gating, product-specific PR review adapters, and automatic post-fix retesting |
| **Planned** | Deep mutation/fuzz/security/load/soak testing, complete UI and distributed-system strategies, remote GraphRAG, and cross-process scheduler supervision |

This classification is itself part of quality engineering: **feature presence, a passing test, and safety for production decisions are three different claims.**

---

## 🛠️ Technology and My Engineering Contributions

- **Language / package:** Python 3.10+, setuptools, PyYAML
- **Testing:** Pytest, unittest, BDD/Gherkin, structured oracles
- **Agent integration:** Hermes dynamic skill, MCP handoff, candidate-only subagent boundary
- **Workflow:** Task Graph DAG, bounded parallel execution, checkpoints, targeted repair, human gates
- **Knowledge:** SQLite, JSON, ontology validation, provenance, reversible fusion
- **Trackers / delivery:** Redmine, Gitea Issues, Wiki, PR review and repair handoff
- **Browser / runtime:** Playwright, local/remote environment profiles, bounded PTY/TUI probes
- **Security:** Redaction, secret detection, contract hashes, write ledgers, and allowlisted argv

I translated the product requirements into system architecture and contracts, implemented the Python engine and CLI/Hermes command surface, built the case/evidence pipeline, Task/Knowledge Graph workflows, and issue/Wiki/PR gates, and used BDD plus automated tests to validate status semantics and safety boundaries continuously.

---

## 💡 What I Learned

This project changed how I think about AI in SWQA. AI is valuable for understanding large contexts, identifying candidate risks, generating cases, and drafting readable reports. PASS, evidence validity, remote writes, and release decisions, however, should not depend solely on a model's natural-language conclusion.

The most important property of AI Quality Pilot is therefore not maximum autonomy. It is being **verifiable, resumable, auditable, and able to stop when a human decision is required**. This is how I extended test automation toward AI-assisted Quality Engineering during my work at Advantech.

> **Source code and full documentation:** [https://github.com/siriChiu/quality-assurance-AI-system-testing](https://github.com/siriChiu/quality-assurance-AI-system-testing)
