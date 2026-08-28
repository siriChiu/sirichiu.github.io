---
title: "作品簡報"
description: "邱璽睿的網站原生雙語工程作品簡報：軟體自動化、AI 應用與 DSP／韌體。"
type: presentation
layout: single
presentation:
  eyebrow: "8–10 分鐘工程作品簡報"
  coreLabel: "核心簡報"
  appendixLabel: "附錄"
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
  labels:
    situation: "Situation｜情境"
    ownership: "Task / Ownership｜責任"
    decisions: "Action｜三個工程決定"
    result: "Result｜交付"
    validation: "Evidence｜驗證與觀測"
    boundary: "Boundary｜邊界"
  slides:
    - id: intro
      group: core
      variant: hero
      kicker: "01 · Executive Summary"
      title: "邱璽睿｜Software Automation Engineer"
      summary: "現職研華 Software Engineer；以 Golang／Python 開發伺服器壓力測試、熱控制、設備監控與 QA 工具，AI 僅在可驗證規則與人工閘門內協助。"
      image: "/images/head.jpg"
      imageAlt: "邱璽睿的個人照片"
      capabilities:
        - title: "流程自動化"
          text: "以 Golang／Python 串接設備、排程、API 與工程作業。"
        - title: "可觀測平台"
          text: "將 IPMI／SNMP 與執行狀態整理成 metrics、logs 與告警。"
        - title: "受控 AI 應用"
          text: "讓模型產生候選內容，由 deterministic rules 與人員決定寫入。"
      roleLine: "主軸｜Software Automation／Platform　副軸｜AI Applications　基礎｜DSP／Firmware"

    - id: career-timeline
      group: core
      variant: timeline
      kicker: "02 · Career & Ownership"
      title: "從訊號分析，走到工程流程與平台自動化"
      summary: "責任範圍由研究演算法與產品韌體，逐步延伸到跨設備、跨服務的軟體系統。"
      timeline:
        - period: "2022/11–Present"
          company: "研華 Advantech"
          role: "Software Engineer"
          text: "負責 Golang／Python 自動化、伺服器控制、IPMI／SNMP 整合，以及 Prometheus／Grafana 與 AI-assisted QA。"
        - period: "2021/10–2022/09"
          company: "Sentons"
          role: "DSP / Firmware Engineer"
          text: "負責 MATLAB 訊號分析、C# WPF 校正工具與通過驗證後的 C++ 韌體功能。"
        - period: "2019–2021"
          company: "國立成功大學"
          role: "Biomedical Engineering M.S."
          text: "提出超音波影像處理方法，以 SVD、背景抑制與結構增強完成研究驗證。"
      note: "求職定位：Software Automation／Platform 為主，AI application 次之；DSP／Firmware 是處理裝置與實體訊號邊界的基礎。"

    - id: engineering-method
      group: core
      variant: method
      kicker: "03 · Engineering Method"
      title: "Sense → Model / Contract → Automate → Observe / Verify"
      summary: "主線是把工程流程做成軟體；AI 與 DSP 在需要理解非結構資料或實體訊號時提供支援。"
      method:
        - step: "01"
          title: "Sense"
          text: "取得 BMC、SNMP、波形、issue 與 workflow state。"
        - step: "02"
          title: "Model / Contract"
          text: "定義功耗反應、熱特徵、測試真相與資料語意。"
        - step: "03"
          title: "Automate"
          text: "以 controller、agent、collector 與 pipeline 執行。"
        - step: "04"
          title: "Observe / Verify"
          text: "保存 metrics、logs、assertions 與人工閘門。"
      mainLine: "主線｜Software Automation：Adapters → Orchestration → Observability → Gated Action"
      supportLine: "支援｜AI：候選內容與脈絡協助　·　DSP／Firmware：訊號、裝置與產品邊界"

    - id: stress-testing
      group: core
      variant: case
      kicker: "04 · Automation Case"
      title: "目標功耗壓力測試：單一 Controller 協調多台伺服器"
      problem: "固定 burn-in 比例可以製造高負載，卻不保證接近指定 system wattage；多台 SUT 的狀態與長時間 log 也分散。"
      ownership: "我設計 Golang controller／agent 流程、pre-test 功耗反應建模與 telemetry 回顧路徑；成功條件是可重跑排程、回收狀態並留下工程師可檢查的資料。"
      architecture: ["Operator", "Go Controller", "Go Agents / SUT", "Telemetry & Logs", "Grafana"]
      decisions:
        - title: "依元件反應建模"
          text: "前測顯示 CPU 可近似線性、Memory／Ethernet 呈飽和；因此不把所有 workload 設成相同比例。"
        - title: "Agent 本地緩衝 logs"
          text: "短暫斷線時先保留執行紀錄，再回傳 controller，降低長時間測試的資料缺口。"
        - title: "AI 不做診斷結論"
          text: "模型只產生待工程師確認的圖表 observation；功率、溫度、風扇與 throttling telemetry 才是回顧來源。"
      result: "完成一對多排程、狀態回傳、目標功耗 workload 估算，以及長時間遙測保存。"
      validation: "以實際 Grafana dashboard 檢查功率、溫度、風扇、頻率與 throttling 時序。"
      boundary: "公開資料未提供 target-power MAE 或 recovery test，因此不宣稱精準命中。"
      image: "/postImg/smartfan/chart.png"
      imageAlt: "壓力測試的 Grafana 功率、溫度、風扇、頻率與 throttling 儀表板"
      article:
        href: "/smart-stress-testing/"
        label: "案例與揭露範圍"

    - id: thermal-control
      group: core
      variant: case
      kicker: "05 · Automation Case"
      title: "伺服器熱控：把數週人工 PID 調校縮短為數小時流程"
      problem: "Open-loop 控制可能長期 over-cooling；PID 若靠反覆試調，流程可能耗時數週且難以重現。"
      ownership: "我負責 Golang host controller、steady-state profile 方法、參數推導，以及 load dump 的 non-zero integral reset 設計；參數須可重算且經工程驗證後才能交付 BMC。"
      architecture: ["Environmental Chamber", "Host Controller", "SUT / BMC", "Workload / Fan"]
      decisions:
        - title: "以平衡點建立 profile"
          text: "用 dT/dt ≈ 0 定義 steady state，再由 profile slope 與 system gain 推導可解釋參數。"
        - title: "離線推導不直接控制產品"
          text: "候選參數必須經工程驗證才交付 BMC，避免模型輸出跨過產品控制邊界。"
        - title: "Load dump 後非零重置"
          text: "將積分項重置到動態計算的安全基準，而不是清零，以降低 RPM 下探與震盪風險。"
      result: "在原特定內部流程中，將可能耗時數週的人工調校縮短為數小時，形成參數 handoff 程序，並累積伺服器熱控制相關專利申請經驗。"
      validation: "平衡點偵測與資料記錄流程可重跑；交付前仍由工程人員檢查 profile 與候選參數。"
      boundary: "「數週到數小時」是特定流程結果，不是跨機種 benchmark。"
      image: "/postImg/ice_algo/1.jpg"
      imageAlt: "伺服器熱特徵平衡點偵測與資料記錄流程"
      article:
        href: "/new-pid-for-server/"
        label: "方法與安全邊界"

    - id: rack-observability
      group: core
      variant: case
      kicker: "06 · Platform Case"
      title: "Rack Observability：在 Collector 邊界統一 IPMI／SNMP"
      problem: "Server、switch 與 PDU 使用不同協定、MIB 與欄位，工程師必須分別查看設備介面。"
      ownership: "我依 Netgear、Cisco、Raritan MIB 實作採集邏輯，並把 BMC／IPMI 與 SNMP 資料正規化為 Prometheus metrics。"
      architecture: ["BMC / IPMI", "Vendor SNMP Adapters", "Collectors", "Prometheus", "Grafana / Alerts"]
      decisions:
        - title: "保留來源語意"
          text: "metric 保留 device class 與 source，不假設不同設備的同名欄位具有相同語意。"
        - title: "遙測與控制分離"
          text: "唯讀 telemetry 走觀測管線；PDU power control 需要獨立授權與稽核。"
        - title: "Adapter 隔離 vendor 差異"
          text: "新增 vendor 時修改邊界 collector，而不重寫 dashboard 的核心資料模型。"
      result: "形成跨 server、switch 與 PDU 的單一 Prometheus／Grafana 觀測路徑，並支援 threshold alerts。"
      validation: "以 collector → Prometheus → Grafana 架構與實際設備類別逐項核對資料來源。"
      boundary: "不宣稱未公開的 polling SLA、部署規模或全型號相容性。"
      image: "/postImg/rack_monitor/architecture.svg"
      imageAlt: "IPMI 與 SNMP adapter 經 collectors 進入 Prometheus 與 Grafana 的架構"
      article:
        href: "/rack-monitor/"
        label: "採集實作與限制"

    - id: ai-quality-pilot
      group: core
      variant: case
      kicker: "07 · AI Application Case"
      title: "AI Quality Pilot：規則引擎掌握 PASS 與寫入權"
      problem: "LLM 若同時負責執行、判定 PASS 和修改 tracker，容易把合理敘述誤當成已驗證結果。"
      ownership: "我設計公開系統 contract，實作 Python engine、case／evidence pipeline、四軸 truth model、Task／Knowledge Graph 與 issue／Wiki／PR gate。"
      architecture: ["Hermes / LLM", "Candidate Content", "Deterministic Engine", "Evidence", "Write Gate / Human"]
      decisions:
        - title: "分開四種真相"
          text: "workflow_status、test_outcome、gate_status、health_status 各自演進，避免單一 done 掩蓋失敗。"
        - title: "驗證 evidence，而非只看 exit code"
          text: "保存 structured assertions、stdout／stderr、duration、contract hash 與 freshness。"
        - title: "不可逆操作保留 human gate"
          text: "命令採 allowlist 與 shell=False；issue、Wiki、PR 等遠端寫入需 deterministic gate。"
      result: "交付 MIT 授權、repository-agnostic 的 QA toolkit；可追蹤狀態、證據、local gates 與遠端寫入 request artifacts。"
      validation: "公開 repository 與 architecture 文件可檢查；能力表明示 Supported、Partial、Planned。"
      boundary: "Supported：contract／evidence／local gates；Partial：MCP 與 repair handoff；Planned：更完整遠端整合。"
      image: "/postImg/ai-quality-pilot/architecture.svg"
      imageAlt: "AI Quality Pilot 將 LLM 與 deterministic engine、evidence 和寫入閘門分離的架構"
      article:
        href: "/ai-quality-pilot/"
        label: "公開架構與 capability matrix"

    - id: dsp-firmware
      group: core
      variant: case
      kicker: "08 · Supporting DSP / Firmware"
      title: "DSP 產品化：從量測波形到 C++ 韌體交付"
      problem: "超音波觸控參數會隨材料、硬體與環境改變；直接編輯 config 難以把手勢、波形與參數放在同一脈絡檢查。"
      ownership: "我負責 MATLAB 訊號分析、C# WPF 裝置與校正工具，以及把通過驗證的參數或需求功能實作到 C++ 韌體。"
      architecture: ["Measured Waveform", "MATLAB Analysis", "C# WPF Calibration", "Engineer Validation", "C++ Firmware"]
      decisions:
        - title: "先保留時頻脈絡"
          text: "用 MATLAB 進行時域／頻域、模擬及線性／非線性濾波，避免只看單一數值。"
        - title: "工具提出候選頻段"
          text: "WPF GUI 整合手勢引導、裝置通訊與波形顯示，讓候選參數可在同一介面複核。"
        - title: "驗證後才進韌體"
          text: "候選參數經產品流程確認後才由 C++ 交付，不宣稱跨材料的一鍵最佳值。"
      result: "建立 signal-to-firmware 的可複核 handoff，支援產品驗證與量產問題處理。"
      validation: "波形脈絡、候選參數與韌體交付點均保留人工檢查；產品成果屬團隊協作。"
      boundary: "客戶、型號、良率與未公開量化結果不進簡報。"
      image: "/postImg/job_sentos/signal-to-firmware-flow.svg"
      imageAlt: "從超音波量測波形、分析與校正到 C++ 韌體的流程"
      article:
        href: "/job_exp_sentos/"
        label: "DSP／韌體案例"

    - id: supporting-index
      group: core
      variant: index
      kicker: "09 · Supporting Products & Research"
      title: "其他產品與研究成果"
      summary: "Lightnews、Redmine 與醫學影像分別展示內容工作流、桌面工具與研究演算法的完整交付。"
      items:
        - title: "Lightnews"
          text: "內容整理需反覆切換 RSS 與 CMS；我用 n8n 串接清理、Ollama 摘要／翻譯與 WordPress draft，輸出可瀏覽網站與待編輯草稿。"
          href: "/lightnews/"
          image: "/postImg/lightnews/1.jpg"
          imageAlt: "Lightnews 網站文章與分類畫面"
          evidence: "A1 完整 STAR+"
        - title: "Redmine Smart Companion"
          text: "把分散的工時操作改成 Plan → Track → Review → Log；輸出是 React／Electron + FastAPI 的 Windows 桌面工作流。"
          href: "/redmine-tracker/"
          image: "/postImg/Redmine-Tracker/calender.jpg"
          imageAlt: "Redmine Smart Companion 週曆規劃介面"
          evidence: "A2 完整 STAR+"
        - title: "Biomedical Imaging"
          text: "以 block-wise SVD、背景抑制與結構增強處理微血流；輸出是已發表方法與動物／人體研究影像。"
          href: "/high-frequency-ultrafast-ultrasound-micro-doppler-imaging-for-estimating-finger-tendon-neovascularity-based-on-curvilinear-structure-enhancement/"
          image: "/postImg/HFUDCEI/0.png"
          imageAlt: "高頻超音波微血流與血管結構研究影像"
          evidence: "A3 完整 STAR+"

    - id: skills-evidence
      group: core
      variant: skills
      kicker: "10 · Skills × Project Evidence"
      title: "技能樹與專案證據對照"
      summary: "依工作層次整理技術，並將每一組能力連回實際交付物。"
      skillGroups:
        - title: "Backend / Automation"
          technologies: "Golang · Python · FastAPI · REST"
          evidence: "壓力測試 controller／agent；熱控 host controller；Redmine local service"
        - title: "Infrastructure / Data"
          technologies: "IPMI · SNMP · Prometheus · Grafana · Linux"
          evidence: "Rack collectors；壓測 telemetry；Lightnews self-hosted workflow"
        - title: "AI / QA"
          technologies: "Pytest · BDD · MCP · Ollama · n8n"
          evidence: "AI Quality Pilot contracts／evidence／gates；Lightnews reviewable drafts"
        - title: "DSP / Firmware"
          technologies: "MATLAB · C# WPF · C++ · SVD"
          evidence: "Sentons calibration-to-firmware；高頻超音波影像研究"

    - id: role-fit
      group: core
      variant: closing
      kicker: "11 · Role Fit"
      title: "Software Automation／Platform｜我能承接的問題"
      summary: "我適合承接設備、API、資料與驗證仍分散在人工流程中的問題。"
      workFits:
        - "實驗室或工程工作流仰賴人工執行、抄錄與回顧。"
        - "團隊需要串接裝置協定、服務 API、排程與 observability。"
        - "AI 功能必須有 truth source、validation 與安全寫入邊界。"
      collaboration: "合作方式｜先與 domain expert 定義成功條件與不可跨越的控制邊界，再用小步可觀測交付迭代。"
      ownershipLine: "我能完整承接｜Adapters → Orchestration → Observability → Gated Action"
      image: "/images/portfolio-qr.svg"
      imageAlt: "前往邱璽睿作品集網站的 QR code"
      contacts:
        - label: "Portfolio"
          href: "https://sirichiu.github.io/"
        - label: "LinkedIn"
          href: "https://linkedin.com/in/sirichiu"
        - label: "GitHub"
          href: "https://github.com/siriChiu"
      closing: "如果這正是團隊要解決的問題，我希望進一步討論。"

    - id: lightnews-case
      group: appendix
      variant: case
      kicker: "A1 · Lightnews STAR+"
      title: "Lightnews：本地 LLM 技術內容草稿管線"
      problem: "技術內容整理需要反覆切換 RSS、網頁清理、翻譯、摘要、圖片與 CMS。"
      ownership: "我設計 Linux-hosted 工作流，目標是產生格式一致、可人工審查的繁體中文草稿。"
      architecture: ["RSS", "n8n Extraction", "Ollama", "Image Candidate", "WordPress Draft", "Editor"]
      decisions:
        - title: "n8n 負責 orchestration"
          text: "集中 RSS watching、extraction、HTML cleaning、branches 與 CMS handoff，讓每一步可檢查。"
        - title: "文字推論留在自管 host"
          text: "以 Ollama 產生摘要、翻譯、分類與圖片關鍵字，減少文字送往第三方 LLM API。"
        - title: "WordPress 預設為 draft"
          text: "來源語意、翻譯、圖片授權與發布由編輯決定；模型沒有 publish authority。"
      result: "交付可瀏覽的繁體中文科技新聞網站與 reviewable draft pipeline。"
      validation: "公開網站畫面可檢查文章、分類與發布呈現。"
      boundary: "本地僅指文字推論；RSS、Unsplash 與 WordPress 仍是外部邊界。"
      image: "/postImg/lightnews/1.jpg"
      imageAlt: "Lightnews 網站文章與分類畫面"
      article: { href: "/lightnews/", label: "完整案例" }

    - id: redmine-case
      group: appendix
      variant: case
      kicker: "A2 · Redmine STAR+"
      title: "Redmine Smart Companion：Plan → Track → Review → Log"
      problem: "一筆工時在原情境可能涉及約十次點擊與頁面切換，也不容易檢查一週是否漏記。"
      ownership: "我重設 Plan → Track → Review → Log 流程，完成 React／Electron UI、本機 FastAPI service 與 Windows installer。"
      architecture: ["React Planner", "Electron", "Local FastAPI", "Redmine API", "Review / Log"]
      decisions:
        - title: "保留 Python backend"
          text: "沿用既有 Redmine 自動化資產，避免為桌面介面重寫整個 API 邏輯。"
        - title: "桌面生命週期與服務分離"
          text: "Electron 管 UI／process lifecycle；PyInstaller 封裝 backend，使用者不需另裝 Python。"
        - title: "本機整理與遠端寫入分狀態"
          text: "規劃、追蹤與 review 不等於已寫入 Redmine，介面明確保留提交邊界。"
      result: "交付 Windows planner／calendar／dashboard 與 Redmine time-entry 工作流。"
      validation: "實際 calendar UI 證明規劃與 review 介面；Windows packaging 有公開描述。"
      boundary: "不宣稱 macOS／Linux 發布、固定生產力提升或未公開的 remote-write 測試。"
      image: "/postImg/Redmine-Tracker/calender.jpg"
      imageAlt: "Redmine Smart Companion 的週曆規劃介面"
      article: { href: "/redmine-tracker/", label: "完整案例" }

    - id: biomedical-case
      group: appendix
      variant: case
      kicker: "A3 · Biomedical Imaging STAR+"
      title: "HFUDCEI：微都卜勒血管結構增強"
      problem: "小鼠器官與受傷手指肌腱的微血流，需要更強的組織 clutter 分離、背景抑制與曲線血管增強。"
      ownership: "我提出 HFUDCEI 影像演算法，並在動物與人體研究資料上評估方法。"
      architecture: ["Ultrafast Ultrasound", "Block-wise SVD", "Background Suppression", "Vesselness", "Research Evaluation"]
      decisions:
        - title: "Block-wise SVD 分離訊號"
          text: "將 tissue／clutter components 與 flow information 分開，降低組織運動干擾。"
        - title: "先抑制背景再增強結構"
          text: "避免 Hessian／Frangi-style multiscale vesselness 同時放大殘餘雜訊。"
        - title: "同時比較與追蹤"
          text: "比較四個小鼠腎臟案例，並觀察人體追蹤案例中的肌腱新生血管呈現。"
      result: "交付並發表微都卜勒方法，用於顯示血管樹與研究手指肌腱新生血管。"
      validation: "公開比較影像與論文記錄 CNR 20.76 dB、SNR 71.98 dB；約 35 μm 僅指可見血管結構直徑。"
      boundary: "人體恢復關聯屬初步研究，不能解讀為診斷或因果證明。"
      image: "/postImg/HFUDCEI/10.png"
      imageAlt: "HFUDCEI 方法的影像品質與血管 profile 比較結果"
      article: { href: "/high-frequency-ultrafast-ultrasound-micro-doppler-imaging-for-estimating-finger-tendon-neovascularity-based-on-curvilinear-structure-enhancement/", label: "研究案例與論文" }

    - id: project-index
      group: appendix
      variant: gallery
      kicker: "A4 · Broader Project Index"
      title: "其他專案索引"
      summary: "供 Q&A 延伸；連結皆為次要佐證。"
      items:
        - { title: "Pose Detection", text: "人體姿態與關鍵點偵測。", href: "/pose-detection/", image: "/postImg/pose-detection/1.jpg", imageAlt: "人體姿態偵測專案" }
        - { title: "X-ray Classification", text: "胸腔 X 光影像分類實驗。", href: "/covid19-chestxray/", image: "/postImg/covid19-chastXray/1.jpg", imageAlt: "胸腔 X 光分類專案" }
        - { title: "Fingerprint Enhancement", text: "指紋髒污區域的影像增強。", href: "/fingerprint-dirt-fix/", image: "/postImg/fingerprint-dirt-fix/1.jpg", imageAlt: "指紋影像增強專案" }
        - { title: "IoT Monitoring", text: "溫溼度感測與即時監控。", href: "/物聯網溫溼度感測器即時監控系統/", image: "/postImg/物聯網溫溼度感測器即時監控系統/0.png", imageAlt: "物聯網溫溼度監控" }
        - { title: "Four-bar Linkage", text: "四連桿機構模擬。", href: "/4-bar-linkage/", image: "/postImg/4-Bar Linkage/1.png", imageAlt: "四連桿機構模擬" }
        - { title: "Long-term Care Platform", text: "長照服務整合平台原型。", href: "/長照2.0服務整合平台/", image: "/postImg/長照2.0服務整合平台/1.png", imageAlt: "長照服務整合平台" }

    - id: disclosure-notes
      group: appendix
      variant: disclosure
      kicker: "A5 · Claim & Disclosure Notes"
      title: "成果主張與揭露邊界"
      disclosures:
        - claim: "熱控流程從數週縮短到數小時"
          scope: "只適用於已描述的特定內部調校流程；不是跨機種 benchmark。"
        - claim: "AI Quality Pilot close loop"
          scope: "公開版為 partial close loop；Supported／Partial／Planned 必須分開閱讀。"
        - claim: "約 35 μm"
          scope: "指公開研究中約 35 μm 直徑血管結構的可見性，不是泛稱系統解析度。"
        - claim: "企業專案成果"
          scope: "不揭露客戶、產品型號、hosts、帳號、拓樸、係數、門檻、原始測試資料或法務狀態。"
        - claim: "未列公開 metric 的案例"
          scope: "只陳述已交付 artifact 與可觀測能力，不推估規模、準確率、節省或部署狀態。"
---
