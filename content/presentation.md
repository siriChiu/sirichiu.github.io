---
title: "作品簡報"
description: "邱璽睿的網站原生工程作品簡報：從硬體訊號、模型到可驗證的自動化系統。"
type: presentation
layout: single
presentation:
  eyebrow: "5–6 分鐘工程作品導覽"
  coreLabel: "核心故事"
  appendixLabel: "附錄 · Q&A"
  backLabel: "返回網站"
  languageLabel: "English"
  controls:
    previous: "上一頁"
    next: "下一頁"
    overview: "總覽"
    slides: "投影片"
    fullscreen: "全螢幕"
    exitFullscreen: "離開全螢幕"
    keyboard: "鍵盤操作"
    keyboardHelp: "←/→ 或 PageUp/PageDown 切換 · Home/End 跳轉 · O 總覽 · F 全螢幕 · Esc 總覽"
    slideStatus: "第 %d 張，共 %d 張：%s"
    overviewStatus: "總覽模式，共 %d 張投影片"
    openSlide: "開啟投影片"
  slides:
    - id: intro
      group: core
      variant: hero
      kicker: "Software Engineer · Automation · DSP"
      title: "邱璽睿：把硬體訊號轉成可驗證的軟體系統"
      summary: "我橫跨伺服器自動化、熱控制、DSP 與醫學影像，把物理訊號與人工流程轉成可量測、可追蹤、可檢查的工程系統。"
      image: "/images/head.jpg"
      imageAlt: "邱璽睿的個人照片"
      tags: ["Golang / Python", "C++ / C# / MATLAB", "Prometheus / Grafana"]
      article:
        href: "/job_exp_advantech/"
        label: "查看現職作品總覽"
    - id: engineering-loop
      group: core
      variant: process
      kicker: "工程主線"
      title: "Sense → Model → Automate / Verify"
      summary: "領域不同，方法一致：先取得可信訊號，再建立可解釋模型，最後用自動化與證據驗證結果。"
      image: "/postImg/job_advantech/engineering-portfolio-map.svg"
      imageAlt: "伺服器系統、自動化與品質工程的作品集關係圖"
      items:
        - title: "Sense"
          text: "IPMI、SNMP、超音波與工作流程狀態"
        - title: "Model"
          text: "熱特徵、功耗反應、訊號結構與狀態契約"
        - title: "Automate / Verify"
          text: "分散執行、可觀測性、測試證據與寫入閘門"
      article:
        href: "/job_exp_advantech/"
        label: "閱讀工程作品脈絡"
    - id: current-impact
      group: core
      variant: project
      kicker: "研華科技 · 2022/11–Present"
      title: "現職影響總覽"
      summary: "以軟體工程串起伺服器控制、實驗流程、設備資料與品質作業。"
      image: "/postImg/job_advantech/thumbnail-v2.png"
      imageAlt: "研華工程作品集縮圖"
      bullets:
        - "由穩態熱特徵推導控制參數，支援可重複的工程驗證。"
        - "以目標功耗模型與分散式 agent 協調多台 SUT 測試。"
        - "整合 IPMI/SNMP、Prometheus/Grafana 與具閘門的品質自動化。"
      note: "公開內容不包含內部設備配置、係數、門檻、客戶資料或法務狀態。"
      article:
        href: "/job_exp_advantech/"
        label: "查看現職案例與揭露範圍"
    - id: stress-testing
      group: core
      variant: project
      kicker: "Case 01 · Distributed Automation"
      title: "目標功耗導向、可重複的壓力測試"
      summary: "固定負載不等於目標功耗；先描述元件反應，再估算 workload 組合並保留長時間遙測。"
      image: "/postImg/smartfan/predict-control-analyze-loop.svg"
      imageAlt: "從元件功耗建模、目標控制到 Grafana 分析的壓力測試流程"
      bullets:
        - "Golang controller / agent 排程多台 SUT、回傳狀態與 logs。"
        - "以前測描述 CPU 近似線性、Memory/Ethernet 飽和型功耗反應。"
        - "Grafana 保留功率、溫度與風扇資料供回顧；AI 判讀僅為輔助。"
      article:
        href: "/smart-stress-testing/"
        label: "閱讀壓力測試案例"
    - id: thermal-control
      group: core
      variant: project
      kicker: "Case 02 · Control Systems"
      title: "可解釋的伺服器熱控"
      summary: "把反覆試調改成「穩態量測 → 參數推導 → 工程驗證 → BMC runtime」的可追蹤流程。"
      image: "/postImg/ice_algo/thermal-control-loop.svg"
      imageAlt: "伺服器熱特徵識別、參數推導與 BMC 執行迴路"
      bullets:
        - "Golang host controller 協調環境測試室、SUT/BMC、負載與風扇。"
        - "在 dT/dt ≈ 0 記錄平衡點，由 profile slope 與 system gain 推導參數。"
        - "加入 load dump 的非零積分重置路徑，降低轉速下探與震盪風險。"
      article:
        href: "/new-pid-for-server/"
        label: "閱讀熱控制案例"
    - id: observability
      group: core
      variant: project
      kicker: "Case 03 · Infrastructure"
      title: "異質設備的統一可觀測性"
      summary: "設備各自說不同的協定；collector 在邊界正規化資料，讓後端與儀表板維持一致。"
      image: "/postImg/rack_monitor/observability-pipeline-v2.svg"
      imageAlt: "IPMI 與 SNMP 設備經 collector 進入 Prometheus 和 Grafana 的可觀測性管線"
      bullets:
        - "以 IPMI 讀取 server BMC，依 MIB 實作 Netgear、Cisco 與 Raritan SNMP collectors。"
        - "正規化為 Prometheus metrics，由 Grafana 顯示與執行門檻告警。"
        - "將唯讀遙測與 PDU 電源控制分開，維持清楚的安全邊界。"
      article:
        href: "/rack-monitor/"
        label: "閱讀機櫃監控案例"
    - id: quality-loop
      group: core
      variant: project
      kicker: "Case 04 · AI-assisted QA"
      title: "從 AI 輔助到可稽核品質閉環"
      summary: "LLM 協助理解與草擬；deterministic engine 擁有測試真實狀態、證據與遠端寫入權。"
      image: "/postImg/ai-quality-pilot/close-loop.svg"
      imageAlt: "AI Quality Pilot 從議題、測試、證據到修復交接的受控閉環"
      bullets:
        - "Hermes 作為對話入口，Python engine 管理 contract 與四軸測試狀態。"
        - "串接 Redmine/Gitea MCP、Pytest/BDD、Task Graph 與 Knowledge Graph。"
        - "公開 GitHub 版本排除內部 hosts、帳號、測試資料、客戶資訊與實驗室拓樸。"
      article:
        href: "/ai-quality-pilot/"
        label: "閱讀 AI Quality Pilot 案例"
    - id: signal-to-firmware
      group: core
      variant: project
      kicker: "Sentons · 2021/10–2022/09"
      title: "從超音波訊號到產品韌體"
      summary: "把量測波形、參數判讀、校正工具與韌體交付放進同一條可複核的工程路徑。"
      image: "/postImg/job_sentos/signal-to-firmware-flow.svg"
      imageAlt: "從超音波訊號、波形分析、校正工具到 C++ 韌體的流程"
      bullets:
        - "MATLAB：時頻分析、模擬、線性與非線性濾波。"
        - "C# WPF：整合裝置通訊、訊號顯示與參數設定的 GUI / SDK。"
        - "C++：實作驗證後的參數與需求功能，支援跨國協作與產品驗證。"
      note: "不揭露客戶、產品型號、量產良率或未公開的量化成果。"
      article:
        href: "/job_exp_sentos/"
        label: "閱讀 DSP 與韌體案例"
    - id: biomedical-imaging
      group: core
      variant: project
      kicker: "NCKU · Biomedical Imaging"
      title: "醫學影像：結構增強微都卜勒"
      summary: "從高頻超快速超音波序列中抑制組織與背景訊號，保留細微血流結構供研究與臨床討論。"
      image: "/postImg/HFUDCEI/0.png"
      imageAlt: "高頻超音波微都卜勒處理後的微血管影像"
      bullets:
        - "使用 block-wise SVD 分離組織與血流訊號。"
        - "以曲線結構增強改善微血管樹的可見度。"
        - "公開研究案例描述可顯示最小約 35 μm 直徑的血管結構。"
      article:
        href: "/high-frequency-ultrafast-ultrasound-micro-doppler-imaging-for-estimating-finger-tendon-neovascularity-based-on-curvilinear-structure-enhancement/"
        label: "閱讀醫學影像研究"
    - id: what-i-bring
      group: core
      variant: closing
      kicker: "Role Fit"
      title: "我能帶來什麼"
      summary: "適合需要軟體與平台工程師跨越硬體、資料與驗證邊界的團隊。"
      image: "/images/portfolio-qr.svg"
      imageAlt: "前往邱璽睿作品集網站的 QR code"
      items:
        - title: "系統思考"
          text: "把訊號、模型、執行、觀測與安全邊界視為同一個系統。"
        - title: "軟硬體翻譯"
          text: "在 BMC/IPMI/SNMP、DSP、韌體與應用層之間建立可用介面。"
        - title: "Evidence-first"
          text: "以可重複流程、可觀測資料與明確揭露限制支持工程判斷。"
      contacts:
        - label: "Portfolio"
          href: "https://sirichiu.github.io/"
        - label: "LinkedIn"
          href: "https://linkedin.com/in/sirichiu"
        - label: "GitHub"
          href: "https://github.com/siriChiu"
      closing: "Questions?"
    - id: skills-evidence
      group: appendix
      variant: appendix
      kicker: "A1 · Skills mapped to evidence"
      title: "技能與證據對照"
      summary: "每一項能力都連回可檢視的網站案例。"
      items:
        - title: "Golang · Distributed Automation"
          text: "目標功耗壓力測試"
          href: "/smart-stress-testing/"
        - title: "Control · BMC / IPMI"
          text: "伺服器熱控制"
          href: "/new-pid-for-server/"
        - title: "Prometheus · Grafana · SNMP"
          text: "異質設備可觀測性"
          href: "/rack-monitor/"
        - title: "Python · QA · AI Agents"
          text: "具證據與閘門的品質閉環"
          href: "/ai-quality-pilot/"
        - title: "MATLAB · C# · C++"
          text: "超音波訊號到韌體"
          href: "/job_exp_sentos/"
        - title: "Biomedical Signal Processing"
          text: "高頻超音波微都卜勒"
          href: "/high-frequency-ultrafast-ultrasound-micro-doppler-imaging-for-estimating-finger-tendon-neovascularity-based-on-curvilinear-structure-enhancement/"
    - id: additional-products
      group: appendix
      variant: gallery
      kicker: "A2 · Additional automation products"
      title: "其他自動化產品"
      summary: "兩個較小、但可完整說明工作流與人機邊界的產品案例。"
      items:
        - title: "Lightnews"
          text: "n8n + local LLM 的技術內容草稿管線，保留人工發佈審核。"
          href: "/lightnews/"
          image: "/postImg/lightnews/editorial-pipeline-v2.svg"
          imageAlt: "Lightnews 編輯審核與自動化內容管線"
        - title: "Redmine Smart Companion"
          text: "Electron/React + FastAPI 的 Plan → Track → Review → Log 桌面工作流。"
          href: "/redmine-tracker/"
          image: "/postImg/Redmine-Tracker/plan-track-log-flow.svg"
          imageAlt: "Redmine Smart Companion 桌面工時工作流"
    - id: education-research
      group: appendix
      variant: appendix
      kicker: "A3 · Education and selected research"
      title: "學歷與精選研究"
      items:
        - title: "國立成功大學"
          text: "生物醫學工程研究所 · 碩士"
        - title: "國立勤益科技大學"
          text: "電子工程系 · 學士"
        - title: "Projectile Vector Doppler Imaging"
          text: "高頻超音波向量都卜勒研究"
          href: "/projectile-vector-doppler-imaging/"
        - title: "Evaluation of Hand Tendon Movement"
          text: "手指肌腱運動評估"
          href: "/evaluation-of-hand-tendon-movement/"
    - id: other-projects
      group: appendix
      variant: gallery
      kicker: "A4 · Other projects"
      title: "其他專案"
      summary: "Q&A 時可快速展開的跨領域作品。"
      items:
        - title: "Pose Detection"
          href: "/pose-detection/"
          image: "/postImg/pose-detection/1.jpg"
          imageAlt: "人體姿態偵測專案縮圖"
        - title: "X-ray Classification"
          href: "/covid19-chestxray/"
          image: "/postImg/covid19-chastXray/1.jpg"
          imageAlt: "胸腔 X 光分類專案縮圖"
        - title: "Fingerprint Enhancement"
          href: "/fingerprint-dirt-fix/"
          image: "/postImg/fingerprint-dirt-fix/1.jpg"
          imageAlt: "指紋影像增強專案縮圖"
        - title: "Four-bar Linkage"
          href: "/4-bar-linkage/"
          image: "/postImg/4-Bar Linkage/1.png"
          imageAlt: "四連桿機構模擬專案縮圖"
        - title: "IoT Monitoring"
          href: "/物聯網溫溼度感測器即時監控系統/"
          image: "/postImg/物聯網溫溼度感測器即時監控系統/0.png"
          imageAlt: "物聯網溫溼度監控專案縮圖"
        - title: "Long-term Care Platform"
          href: "/長照2.0服務整合平台/"
          image: "/postImg/長照2.0服務整合平台/1.png"
          imageAlt: "長照服務整合平台專案縮圖"
    - id: disclosure-notes
      group: appendix
      variant: appendix
      kicker: "A5 · Claim and disclosure notes"
      title: "成果與揭露說明"
      bullets:
        - "伺服器熱控制採用「專利申請經驗」；本簡報不宣稱核准狀態或所有權。"
        - "百分比改善若缺少可公開的 baseline 與條件，不列為核心成果。"
        - "35 μm 描述來自已連結的公開研究案例；正式引用以原始論文或會議資料為準。"
        - "AI Quality Pilot 的 GitHub 版本是去識別化通用架構，能力依 Supported / Partial / Planned 分級。"
        - "企業案例排除客戶、產品型號、內部 hosts、帳號、拓樸、係數、門檻與測試資料。"
---
