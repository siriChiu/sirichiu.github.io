---
title: "Portfolio Deck"
description: "Siri Chiu’s bilingual website-native engineering portfolio: software automation, AI applications, and DSP/firmware."
type: presentation
layout: single
presentation:
  eyebrow: "8–10 minute engineering portfolio"
  coreLabel: "Core deck"
  appendixLabel: "Appendix"
  backLabel: "Back to site"
  languageLabel: "繁體中文"
  controls:
    previous: "Previous"
    next: "Next"
    overview: "Overview"
    slides: "Slide mode"
    fullscreen: "Fullscreen"
    exitFullscreen: "Exit fullscreen"
    keyboard: "Keyboard help"
    keyboardHelp: "←/→ or PageUp/PageDown to move · Home/End to jump · O overview · F fullscreen · Esc overview"
    slideStatus: "Slide %d of %d: %s"
    overviewStatus: "Overview mode, %d slides"
    openSlide: "Open slide"
  labels:
    situation: "Situation"
    ownership: "Task / Ownership"
    decisions: "Action / Three Engineering Decisions"
    result: "Result / Deliverable"
    validation: "Evidence / Validation"
    boundary: "Boundary"
  slides:
    - id: intro
      group: core
      variant: hero
      kicker: "01 · Executive Summary"
      title: "Siri Chiu | Software Automation Engineer"
      summary: "Software Engineer at Advantech building server stress-test, thermal-control, device-observability, and QA tools in Golang/Python; AI assists only behind verifiable rules and human gates."
      image: "/images/head.jpg"
      imageAlt: "Portrait of Siri Chiu"
      capabilities:
        - title: "Workflow automation"
          text: "Connect equipment, schedulers, APIs, and engineering work with Golang and Python."
        - title: "Observable platforms"
          text: "Turn IPMI/SNMP and execution state into metrics, logs, and alerts."
        - title: "Controlled AI applications"
          text: "Models produce candidates; deterministic rules and people decide what can be written."
      roleLine: "Primary | Software Automation / Platform　Secondary | AI Applications　Foundation | DSP / Firmware"

    - id: career-timeline
      group: core
      variant: timeline
      kicker: "02 · Career & Ownership"
      title: "From signal analysis to engineering workflow and platform automation"
      summary: "My ownership grew from research algorithms and product firmware to software systems spanning equipment and services."
      timeline:
        - period: "2022/11–Present"
          company: "Advantech"
          role: "Software Engineer"
          text: "Responsible for Golang/Python automation, server control, IPMI/SNMP integration, Prometheus/Grafana paths, and AI-assisted QA work."
        - period: "2021/10–2022/09"
          company: "Sentons"
          role: "DSP / Firmware Engineer"
          text: "Responsible for MATLAB signal analysis, C# WPF calibration tooling, and C++ firmware work after validation."
        - period: "2019–2021"
          company: "National Cheng Kung University"
          role: "M.S., Biomedical Engineering"
          text: "Proposed and evaluated an ultrasound imaging method using SVD, background suppression, and structure enhancement."
      note: "Target: Software Automation/Platform first, AI application development second; DSP/Firmware supports device and physical-signal boundaries."

    - id: engineering-method
      group: core
      variant: method
      kicker: "03 · Engineering Method"
      title: "Sense → Model / Contract → Automate → Observe / Verify"
      summary: "Software automation is the main line. AI and DSP support it when a system must interpret unstructured content or physical signals."
      method:
        - step: "01"
          title: "Sense"
          text: "Acquire BMC, SNMP, waveform, issue, and workflow state."
        - step: "02"
          title: "Model / Contract"
          text: "Define power response, thermal profiles, test truth, and data semantics."
        - step: "03"
          title: "Automate"
          text: "Execute through controllers, agents, collectors, and pipelines."
        - step: "04"
          title: "Observe / Verify"
          text: "Retain metrics, logs, assertions, and human gates."
      mainLine: "Main line | Software Automation: Adapters → Orchestration → Observability → Gated Action"
      supportLine: "Support | AI: candidate content and context · DSP/Firmware: signal, device, and product boundaries"

    - id: stress-testing
      group: core
      variant: case
      kicker: "04 · Automation Case"
      title: "Target-Power Stress Testing: One Controller, Multiple Servers"
      problem: "Fixed burn-in percentages can create high load but do not ensure proximity to a target system wattage; multi-SUT state and long-run logs were also fragmented."
      ownership: "I designed the Golang controller/agent flow, pre-test power-response modeling, and telemetry review path. Success meant repeatable scheduling, state collection, and inspectable engineering data."
      architecture: ["Operator", "Go Controller", "Go Agents / SUT", "Telemetry & Logs", "Grafana"]
      decisions:
        - title: "Model component responses"
          text: "Pre-tests showed approximately linear CPU and saturating Memory/Ethernet behavior, so I did not assign every workload the same percentage."
        - title: "Buffer logs at each agent"
          text: "Agents retain execution records across temporary disconnects before returning them to the controller, reducing gaps in long tests."
        - title: "Keep AI out of diagnosis"
          text: "The model proposes chart observations for engineer review; power, thermal, fan, and throttling telemetry remains the review source."
      result: "Delivered one-to-many scheduling, state return, target-power workload estimation, and retention of long-duration telemetry."
      validation: "Reviewed power, temperature, fan, frequency, and throttling time series in the actual Grafana dashboard."
      boundary: "Public evidence includes no target-power MAE or recovery test, so I do not claim precise target matching."
      image: "/postImg/smartfan/chart.png"
      imageAlt: "Grafana dashboard for stress-test power, temperature, fans, frequency, and throttling"
      article: { href: "/en/smart-stress-testing/", label: "Case details and disclosure scope" }

    - id: thermal-control
      group: core
      variant: case
      kicker: "05 · Automation Case"
      title: "Server Thermal Control: From Weeks of Tuning to an Hours-Scale Workflow"
      problem: "Open-loop control can over-cool for long periods; repeated trial-and-error PID tuning could take weeks and was difficult to reproduce."
      ownership: "I owned the Golang host controller, steady-state profile method, parameter derivation, and non-zero integral reset after load dump. Parameters had to be reproducible and engineering-validated before BMC handoff."
      architecture: ["Environmental Chamber", "Host Controller", "SUT / BMC", "Workload / Fan"]
      decisions:
        - title: "Build profiles at equilibrium"
          text: "I defined steady state as dT/dt ≈ 0, then derived explainable parameters from profile slope and system gain."
        - title: "Do not let offline output control the product"
          text: "Candidate parameters require engineering validation before BMC delivery, preserving the product-control boundary."
        - title: "Use a non-zero reset after load dump"
          text: "I reset the integral term to a dynamically calculated safe base instead of zero to reduce RPM undershoot and oscillation risk."
      result: "In the stated internal workflow, reduced a process that could take weeks to hours, established a parameter-handoff procedure, and gained patent-application experience in server thermal control."
      validation: "The equilibrium detection and data-recording flow is repeatable; engineers still inspect the profile and candidate parameters before delivery."
      boundary: "Weeks to hours applies to that specific workflow, not a cross-platform benchmark."
      image: "/postImg/ice_algo/1.jpg"
      imageAlt: "Equilibrium detection and data-recording flow for server thermal characterization"
      article: { href: "/en/new-pid-for-server/", label: "Method and safety boundary" }

    - id: rack-observability
      group: core
      variant: case
      kicker: "06 · Platform Case"
      title: "Rack Observability: Normalize IPMI/SNMP at the Collector Boundary"
      problem: "Servers, switches, and PDUs expose different protocols, MIBs, and fields, forcing engineers to inspect separate equipment interfaces."
      ownership: "I implemented collection logic from Netgear, Cisco, and Raritan MIBs and normalized BMC/IPMI and SNMP data into Prometheus metrics."
      architecture: ["BMC / IPMI", "Vendor SNMP Adapters", "Collectors", "Prometheus", "Grafana / Alerts"]
      decisions:
        - title: "Preserve source semantics"
          text: "Metrics retain device class and source; similarly named fields from different equipment are not assumed to mean the same thing."
        - title: "Separate telemetry from control"
          text: "Read-only data follows the observability path; PDU power control requires separate authorization and audit."
        - title: "Isolate vendor differences in adapters"
          text: "Adding a vendor changes the boundary collector rather than the dashboard’s core data model."
      result: "Delivered one Prometheus/Grafana observability path across server, switch, and PDU classes with threshold-alert support."
      validation: "Checked each device class and source against the documented collector → Prometheus → Grafana architecture."
      boundary: "I do not claim an unpublished polling SLA, deployment scale, or universal model compatibility."
      image: "/postImg/rack_monitor/architecture.svg"
      imageAlt: "Architecture from IPMI and SNMP adapters through collectors to Prometheus and Grafana"
      article: { href: "/en/rack-monitor/", label: "Collector implementation and limits" }

    - id: ai-quality-pilot
      group: core
      variant: case
      kicker: "07 · AI Application Case"
      title: "AI Quality Pilot: Deterministic Rules Own PASS and Write Access"
      problem: "When an LLM executes, declares PASS, and edits a tracker, plausible language can be mistaken for a validated result."
      ownership: "I designed the public system contract and implemented the Python engine, case/evidence pipeline, four-axis truth model, Task/Knowledge Graphs, and issue/Wiki/PR gates."
      architecture: ["Hermes / LLM", "Candidate Content", "Deterministic Engine", "Evidence", "Write Gate / Human"]
      decisions:
        - title: "Separate four kinds of truth"
          text: "workflow_status, test_outcome, gate_status, and health_status evolve independently so one done state cannot conceal failure."
        - title: "Validate evidence, not only exit codes"
          text: "Evidence retains structured assertions, stdout/stderr, duration, contract hashes, and freshness."
        - title: "Keep human gates for irreversible action"
          text: "Commands use allowlists and shell=False; remote issue, Wiki, and PR writes pass deterministic gates."
      result: "Delivered an MIT-licensed, repository-agnostic QA toolkit with inspectable state, evidence, local gates, and remote-write request artifacts."
      validation: "The public repository and architecture are reviewable; its matrix distinguishes Supported, Partial, and Planned capabilities."
      boundary: "Supported: contracts/evidence/local gates; Partial: MCP and repair handoff; Planned: broader remote integration."
      image: "/postImg/ai-quality-pilot/architecture.svg"
      imageAlt: "AI Quality Pilot architecture separating the LLM from deterministic evidence and write gates"
      article: { href: "/en/ai-quality-pilot/", label: "Public architecture and capability matrix" }

    - id: dsp-firmware
      group: core
      variant: case
      kicker: "08 · Supporting DSP / Firmware"
      title: "DSP Productization: From Measured Waveform to C++ Firmware"
      problem: "Ultrasound-touch parameters change with materials, hardware, and environment; direct config editing hides the relationship among gestures, waveforms, and parameters."
      ownership: "I owned MATLAB signal analysis, the C# WPF device/calibration tool, and implementation of validated parameters or requested features in C++ firmware."
      architecture: ["Measured Waveform", "MATLAB Analysis", "C# WPF Calibration", "Engineer Validation", "C++ Firmware"]
      decisions:
        - title: "Retain time/frequency context first"
          text: "MATLAB time/frequency analysis, simulation, and linear/nonlinear filtering avoided reducing a waveform to one value."
        - title: "Let the tool propose candidate bands"
          text: "The WPF GUI combined gesture guidance, device communication, and waveform display so parameters could be reviewed in context."
        - title: "Move into firmware only after validation"
          text: "C++ delivered parameters after the product validation path; I do not claim a one-click optimum across materials."
      result: "Established a reviewable signal-to-firmware handoff supporting product validation and production issue work."
      validation: "Waveform context, candidate parameters, and firmware handoff retained human review; product outcomes were collaborative."
      boundary: "Customers, product models, yield, and unpublished quantitative results are excluded."
      image: "/postImg/job_sentos/signal-to-firmware-flow.svg"
      imageAlt: "Flow from measured ultrasound waveform and calibration to C++ firmware"
      article: { href: "/en/job_exp_sentos/", label: "DSP and firmware case" }

    - id: supporting-index
      group: core
      variant: index
      kicker: "09 · Supporting Products & Research"
      title: "Additional Products and Research"
      summary: "Lightnews, Redmine, and biomedical imaging demonstrate complete delivery across content workflows, desktop tooling, and research algorithms."
      items:
        - title: "Lightnews"
          text: "Content curation required repeated RSS-to-CMS switching; I connected cleanup, Ollama summarization/translation, and WordPress drafts in n8n, delivering a browsable site and editable draft pipeline."
          href: "/en/lightnews/"
          image: "/postImg/lightnews/1.jpg"
          imageAlt: "Lightnews website showing articles and categories"
          evidence: "Full STAR+ in A1"
        - title: "Redmine Smart Companion"
          text: "Reframed scattered time entry as Plan → Track → Review → Log; delivered a React/Electron + FastAPI Windows desktop workflow."
          href: "/en/redmine-tracker/"
          image: "/postImg/Redmine-Tracker/calender.jpg"
          imageAlt: "Weekly planner view in Redmine Smart Companion"
          evidence: "Full STAR+ in A2"
        - title: "Biomedical Imaging"
          text: "Applied block-wise SVD, background suppression, and structure enhancement to micro-flow imaging; delivered a published method and research results."
          href: "/en/high-frequency-ultrafast-ultrasound-micro-doppler-imaging-for-estimating-finger-tendon-neovascularity-based-on-curvilinear-structure-enhancement/"
          image: "/postImg/HFUDCEI/0.png"
          imageAlt: "High-frequency ultrasound micro-flow and vascular-structure research images"
          evidence: "Full STAR+ in A3"

    - id: skills-evidence
      group: core
      variant: skills
      kicker: "10 · Skills × Project Evidence"
      title: "Skill Tree Mapped to Project Evidence"
      summary: "Capabilities are grouped by engineering layer and linked to delivered work."
      skillGroups:
        - title: "Backend / Automation"
          technologies: "Golang · Python · FastAPI · REST"
          evidence: "Stress-test controller/agents; thermal host controller; Redmine local service"
        - title: "Infrastructure / Data"
          technologies: "IPMI · SNMP · Prometheus · Grafana · Linux"
          evidence: "Rack collectors; stress telemetry; self-hosted Lightnews workflow"
        - title: "AI / QA"
          technologies: "Pytest · BDD · MCP · Ollama · n8n"
          evidence: "AI Quality Pilot contracts/evidence/gates; reviewable Lightnews drafts"
        - title: "DSP / Firmware"
          technologies: "MATLAB · C# WPF · C++ · SVD"
          evidence: "Sentons calibration-to-firmware; high-frequency ultrasound research"

    - id: role-fit
      group: core
      variant: closing
      kicker: "11 · Role Fit"
      title: "Software Automation / Platform | Problems I Can Own"
      summary: "I can own problems where devices, APIs, data, and validation remain fragmented across manual workflows."
      workFits:
        - "Laboratory or engineering work still depends on manual execution, transcription, and review."
        - "The team needs device protocols, service APIs, scheduling, and observability connected."
        - "AI features require truth sources, validation, and safe write boundaries."
      collaboration: "Collaboration | Define success conditions and control boundaries with domain experts first, then iterate through small, observable deliveries."
      ownershipLine: "End-to-end ownership | Adapters → Orchestration → Observability → Gated Action"
      image: "/images/portfolio-qr.svg"
      imageAlt: "QR code for Siri Chiu’s portfolio"
      contacts:
        - { label: "Portfolio", href: "https://sirichiu.github.io/" }
        - { label: "LinkedIn", href: "https://linkedin.com/in/sirichiu" }
        - { label: "GitHub", href: "https://github.com/siriChiu" }
      closing: "If these are the problems your team is solving, I would like to discuss them further."

    - id: lightnews-case
      group: appendix
      variant: case
      kicker: "A1 · Lightnews STAR+"
      title: "Lightnews: A Local-LLM Technical Draft Pipeline"
      problem: "Technical-content curation required repeated switching among RSS, page cleanup, translation, summarization, images, and the CMS."
      ownership: "I designed a Linux-hosted workflow that produces consistent, human-reviewable Traditional Chinese drafts."
      architecture: ["RSS", "n8n Extraction", "Ollama", "Image Candidate", "WordPress Draft", "Editor"]
      decisions:
        - title: "Use n8n for orchestration"
          text: "RSS watching, extraction, HTML cleaning, branches, and CMS handoff stay inspectable as separate workflow steps."
        - title: "Keep text inference on a managed host"
          text: "Ollama generates summaries, translations, categories, and image keywords, reducing text sent to third-party LLM APIs."
        - title: "Default WordPress output to draft"
          text: "Editors decide source meaning, translation, image licensing, and publication; the model has no publish authority."
      result: "Delivered a browsable Traditional Chinese technology-news site and reviewable draft pipeline."
      validation: "The public site capture shows articles, categories, and publication presentation."
      boundary: "Local applies only to text inference; RSS, Unsplash, and WordPress remain external boundaries."
      image: "/postImg/lightnews/1.jpg"
      imageAlt: "Lightnews website showing articles and categories"
      article: { href: "/en/lightnews/", label: "Full case" }

    - id: redmine-case
      group: appendix
      variant: case
      kicker: "A2 · Redmine STAR+"
      title: "Redmine Smart Companion: Plan → Track → Review → Log"
      problem: "In the observed context, one time entry could require roughly ten clicks and page changes, while weekly omissions were hard to inspect."
      ownership: "I redesigned Plan → Track → Review → Log and delivered the React/Electron UI, local FastAPI service, and Windows installer."
      architecture: ["React Planner", "Electron", "Local FastAPI", "Redmine API", "Review / Log"]
      decisions:
        - title: "Retain the Python backend"
          text: "This reused existing Redmine automation rather than rewriting all API logic for a desktop UI."
        - title: "Separate desktop lifecycle and service"
          text: "Electron manages UI/process lifecycle; PyInstaller packages the backend so users do not install Python."
        - title: "Separate local planning from remote writes"
          text: "Planning, tracking, and review do not imply that a Redmine record was written; the UI retains the submission boundary."
      result: "Delivered a Windows planner/calendar/dashboard and Redmine time-entry workflow."
      validation: "The actual calendar UI demonstrates planning and review surfaces; public material documents Windows packaging."
      boundary: "I do not claim macOS/Linux release, fixed productivity gains, or unpublished remote-write test coverage."
      image: "/postImg/Redmine-Tracker/calender.jpg"
      imageAlt: "Weekly calendar interface in Redmine Smart Companion"
      article: { href: "/en/redmine-tracker/", label: "Full case" }

    - id: biomedical-case
      group: appendix
      variant: case
      kicker: "A3 · Biomedical Imaging STAR+"
      title: "HFUDCEI: Micro-Doppler Vascular-Structure Enhancement"
      problem: "Micro-flow in mouse organs and injured finger tendons required stronger tissue-clutter separation, background suppression, and curvilinear vessel enhancement."
      ownership: "I proposed the HFUDCEI imaging algorithm and evaluated it with animal and human research data."
      architecture: ["Ultrafast Ultrasound", "Block-wise SVD", "Background Suppression", "Vesselness", "Research Evaluation"]
      decisions:
        - title: "Separate signals with block-wise SVD"
          text: "Tissue/clutter components were separated from flow information to reduce tissue-motion interference."
        - title: "Suppress background before enhancing structure"
          text: "This avoided having Hessian/Frangi-style multiscale vesselness amplify residual noise."
        - title: "Combine comparison and follow-up evaluation"
          text: "I compared four mouse-kidney cases and examined tendon neovascularity presentation in human follow-up cases."
      result: "Delivered and published a micro-Doppler method for vascular-tree visualization and finger-tendon neovascularity research."
      validation: "Public comparisons and the paper report CNR 20.76 dB and SNR 71.98 dB; ~35 μm refers only to visible vessel-structure diameter."
      boundary: "The human recovery relationship is preliminary research, not diagnostic or causal proof."
      image: "/postImg/HFUDCEI/10.png"
      imageAlt: "HFUDCEI image-quality and vessel-profile comparison results"
      article: { href: "/en/high-frequency-ultrafast-ultrasound-micro-doppler-imaging-for-estimating-finger-tendon-neovascularity-based-on-curvilinear-structure-enhancement/", label: "Research case and paper" }

    - id: project-index
      group: appendix
      variant: gallery
      kicker: "A4 · Broader Project Index"
      title: "Other Project Index"
      summary: "For Q&A follow-up; links are secondary evidence."
      items:
        - { title: "Pose Detection", text: "Human pose and keypoint detection.", href: "/en/pose-detection/", image: "/postImg/pose-detection/1.jpg", imageAlt: "Pose-detection project" }
        - { title: "X-ray Classification", text: "Chest X-ray classification experiment.", href: "/en/covid19-chestxray/", image: "/postImg/covid19-chastXray/1.jpg", imageAlt: "Chest X-ray classification project" }
        - { title: "Fingerprint Enhancement", text: "Image enhancement for dirty fingerprint regions.", href: "/en/fingerprint-dirt-fix/", image: "/postImg/fingerprint-dirt-fix/1.jpg", imageAlt: "Fingerprint enhancement project" }
        - { title: "IoT Monitoring", text: "Temperature/humidity sensing and live monitoring.", href: "/en/物聯網溫溼度感測器即時監控系統/", image: "/postImg/物聯網溫溼度感測器即時監控系統/0.png", imageAlt: "IoT monitoring project" }
        - { title: "Four-bar Linkage", text: "Four-bar linkage simulation.", href: "/en/4-bar-linkage/", image: "/postImg/4-Bar Linkage/1.png", imageAlt: "Four-bar linkage simulation" }
        - { title: "Long-term Care Platform", text: "Long-term care service integration prototype.", href: "/en/長照2.0服務整合平台/", image: "/postImg/長照2.0服務整合平台/1.png", imageAlt: "Long-term care platform" }

    - id: disclosure-notes
      group: appendix
      variant: disclosure
      kicker: "A5 · Claim & Disclosure Notes"
      title: "Claim and Disclosure Boundaries"
      disclosures:
        - claim: "Thermal workflow reduced from weeks to hours"
          scope: "Applies only to the described internal tuning workflow; it is not a cross-platform benchmark."
        - claim: "AI Quality Pilot close loop"
          scope: "The public version is a partial close loop; Supported, Partial, and Planned must remain distinct."
        - claim: "Approximately 35 μm"
          scope: "Means visibility of an approximately 35 μm-diameter vessel structure in the public research, not generic system resolution."
        - claim: "Corporate project results"
          scope: "Exclude customers, product models, hosts, accounts, topology, coefficients, thresholds, raw test data, and legal status."
        - claim: "Cases without public metrics"
          scope: "State delivered artifacts and observable capabilities only; do not infer scale, accuracy, savings, or deployment state."
---
