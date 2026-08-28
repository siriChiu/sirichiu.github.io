---
title: "Portfolio Deck"
description: "Siri Chiu’s website-native engineering portfolio: from hardware signals and models to verifiable automation systems."
type: presentation
layout: single
presentation:
  eyebrow: "A 5–6 minute engineering portfolio tour"
  coreLabel: "Core story"
  appendixLabel: "Appendix · Q&A"
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
  slides:
    - id: intro
      group: core
      variant: hero
      kicker: "Software Engineer · Automation · DSP"
      title: "Siri Chiu: Turning Hardware Signals into Verifiable Software Systems"
      summary: "I work across server automation, thermal control, DSP, and biomedical imaging, turning physical signals and manual procedures into measurable, traceable, and inspectable engineering systems."
      image: "/images/head.jpg"
      imageAlt: "Portrait of Siri Chiu"
      tags: ["Golang / Python", "C++ / C# / MATLAB", "Prometheus / Grafana"]
      article:
        href: "/en/job_exp_advantech/"
        label: "View my current-role portfolio"
    - id: engineering-loop
      group: core
      variant: process
      kicker: "Engineering through-line"
      title: "Sense → Model → Automate / Verify"
      summary: "The domains change, but the method stays consistent: obtain trustworthy signals, build an explainable model, then automate and verify with evidence."
      image: "/postImg/job_advantech/engineering-portfolio-map.svg"
      imageAlt: "Portfolio map connecting server systems, automation, and quality engineering"
      items:
        - title: "Sense"
          text: "IPMI, SNMP, ultrasound, and workflow state"
        - title: "Model"
          text: "Thermal profiles, power response, signal structure, and state contracts"
        - title: "Automate / Verify"
          text: "Distributed execution, observability, test evidence, and write gates"
      article:
        href: "/en/job_exp_advantech/"
        label: "Read the engineering portfolio context"
    - id: current-impact
      group: core
      variant: project
      kicker: "Advantech · 2022/11–Present"
      title: "Current-Role Impact"
      summary: "Software engineering connects server control, lab procedures, equipment data, and quality workflows."
      image: "/postImg/job_advantech/thumbnail-v2.png"
      imageAlt: "Advantech engineering portfolio thumbnail"
      bullets:
        - "Derive control parameters from steady-state thermal profiles for repeatable engineering validation."
        - "Coordinate multi-SUT testing with target-power models and distributed agents."
        - "Integrate IPMI/SNMP, Prometheus/Grafana, and gated quality automation."
      note: "Public material excludes internal equipment configurations, coefficients, thresholds, customer data, and legal status."
      article:
        href: "/en/job_exp_advantech/"
        label: "View current-role cases and disclosure scope"
    - id: stress-testing
      group: core
      variant: project
      kicker: "Case 01 · Distributed Automation"
      title: "Repeatable Target-Power Stress Testing"
      summary: "A fixed load is not a target wattage; characterize component responses, estimate a workload mix, and retain long-duration telemetry."
      image: "/postImg/smartfan/predict-control-analyze-loop.svg"
      imageAlt: "Stress-testing workflow from component power modeling and target control to Grafana analysis"
      bullets:
        - "A Golang controller/agent flow schedules SUTs and returns state and logs."
        - "Pre-tests describe approximately linear CPU and saturating Memory/Ethernet power responses."
        - "Grafana retains power, temperature, and fan data for review; AI chart review remains assistive."
      article:
        href: "/en/smart-stress-testing/"
        label: "Read the stress-testing case"
    - id: thermal-control
      group: core
      variant: project
      kicker: "Case 02 · Control Systems"
      title: "Explainable Server Thermal Control"
      summary: "Replace repeated trial-and-error with a traceable flow: steady-state measurement → parameter derivation → engineering validation → BMC runtime."
      image: "/postImg/ice_algo/thermal-control-loop.svg"
      imageAlt: "Server thermal identification, parameter derivation, and BMC runtime loop"
      bullets:
        - "A Golang host controller coordinates the chamber, SUT/BMC, workload, and fans."
        - "Record equilibrium at dT/dt ≈ 0 and derive parameters from profile slope and system gain."
        - "Use a non-zero integral-reset path after load dumps to reduce RPM undershoot and oscillation risk."
      article:
        href: "/en/new-pid-for-server/"
        label: "Read the thermal-control case"
    - id: observability
      group: core
      variant: project
      kicker: "Case 03 · Infrastructure"
      title: "Unified Observability Across Heterogeneous Devices"
      summary: "Devices speak different protocols; normalization at the collector boundary keeps the backend and dashboards consistent."
      image: "/postImg/rack_monitor/observability-pipeline-v2.svg"
      imageAlt: "Observability pipeline from IPMI and SNMP equipment through a collector to Prometheus and Grafana"
      bullets:
        - "Read server BMCs through IPMI and implement Netgear, Cisco, and Raritan SNMP collectors from MIBs."
        - "Normalize Prometheus metrics for Grafana views and threshold alerts."
        - "Separate read-only telemetry from PDU power control to preserve a clear safety boundary."
      article:
        href: "/en/rack-monitor/"
        label: "Read the rack-observability case"
    - id: quality-loop
      group: core
      variant: project
      kicker: "Case 04 · AI-assisted QA"
      title: "From AI Assistance to a Gated QA Loop"
      summary: "The LLM helps interpret and draft; a deterministic engine owns test truth, evidence, and remote-write authorization."
      image: "/postImg/ai-quality-pilot/close-loop.svg"
      imageAlt: "AI Quality Pilot gated loop from issues and tests to evidence and repair handoff"
      bullets:
        - "Hermes is the conversational entry point; a Python engine owns contracts and four-axis test state."
        - "Connect Redmine/Gitea MCP, Pytest/BDD, a Task Graph, and a Knowledge Graph."
        - "The public GitHub version excludes internal hosts, accounts, test data, customer information, and lab topology."
      article:
        href: "/en/ai-quality-pilot/"
        label: "Read the AI Quality Pilot case"
    - id: signal-to-firmware
      group: core
      variant: project
      kicker: "Sentons · 2021/10–2022/09"
      title: "From Ultrasound Signals to Product Firmware"
      summary: "Place measured waveforms, parameter decisions, calibration tooling, and firmware delivery in one reviewable engineering path."
      image: "/postImg/job_sentos/signal-to-firmware-flow.svg"
      imageAlt: "Flow from ultrasound signals and waveform analysis through calibration tooling to C++ firmware"
      bullets:
        - "MATLAB: time/frequency analysis, simulation, and linear/nonlinear filtering."
        - "C# WPF: GUI/SDK integrating device communication, signal display, and parameter configuration."
        - "C++: implement validated parameters and requested features while supporting international collaboration and product validation."
      note: "No customer, product-model, production-yield, or unpublished quantitative details are disclosed."
      article:
        href: "/en/job_exp_sentos/"
        label: "Read the DSP and firmware case"
    - id: biomedical-imaging
      group: core
      variant: project
      kicker: "NCKU · Biomedical Imaging"
      title: "Biomedical Imaging: Structure-Enhanced Micro-Doppler"
      summary: "Suppress tissue and background signals in high-frequency ultrafast ultrasound sequences, preserving fine blood-flow structures for research and clinical discussion."
      image: "/postImg/HFUDCEI/0.png"
      imageAlt: "Microvascular image after high-frequency ultrasound micro-Doppler processing"
      bullets:
        - "Use block-wise SVD to separate tissue and blood-flow signals."
        - "Apply curvilinear structure enhancement to improve microvascular-tree visibility."
        - "The linked public research case reports visualization of vessel structures down to approximately 35 μm in diameter."
      article:
        href: "/en/high-frequency-ultrafast-ultrasound-micro-doppler-imaging-for-estimating-finger-tendon-neovascularity-based-on-curvilinear-structure-enhancement/"
        label: "Read the biomedical-imaging research"
    - id: what-i-bring
      group: core
      variant: closing
      kicker: "Role Fit"
      title: "What I Bring"
      summary: "A fit for software and platform teams that need an engineer to cross hardware, data, and verification boundaries."
      image: "/images/portfolio-qr.svg"
      imageAlt: "QR code for Siri Chiu’s portfolio website"
      items:
        - title: "Systems thinking"
          text: "Treat signals, models, execution, observation, and safety boundaries as one system."
        - title: "Hardware/software translation"
          text: "Build usable interfaces across BMC/IPMI/SNMP, DSP, firmware, and applications."
        - title: "Evidence-first automation"
          text: "Support decisions with repeatable workflows, observable data, and explicit disclosure limits."
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
      title: "Skills Mapped to Evidence"
      summary: "Each capability links back to a reviewable website case."
      items:
        - title: "Golang · Distributed Automation"
          text: "Target-power stress testing"
          href: "/en/smart-stress-testing/"
        - title: "Control · BMC / IPMI"
          text: "Server thermal control"
          href: "/en/new-pid-for-server/"
        - title: "Prometheus · Grafana · SNMP"
          text: "Heterogeneous-device observability"
          href: "/en/rack-monitor/"
        - title: "Python · QA · AI Agents"
          text: "Evidence-based, gated QA loop"
          href: "/en/ai-quality-pilot/"
        - title: "MATLAB · C# · C++"
          text: "Ultrasound signals to firmware"
          href: "/en/job_exp_sentos/"
        - title: "Biomedical Signal Processing"
          text: "High-frequency ultrasound micro-Doppler"
          href: "/en/high-frequency-ultrafast-ultrasound-micro-doppler-imaging-for-estimating-finger-tendon-neovascularity-based-on-curvilinear-structure-enhancement/"
    - id: additional-products
      group: appendix
      variant: gallery
      kicker: "A2 · Additional automation products"
      title: "Additional Automation Products"
      summary: "Two smaller products with complete workflow and human/machine boundary stories."
      items:
        - title: "Lightnews"
          text: "An n8n + local-LLM technical-content draft pipeline with human publish approval."
          href: "/en/lightnews/"
          image: "/postImg/lightnews/editorial-pipeline-v2.svg"
          imageAlt: "Lightnews automation pipeline and editorial gate"
        - title: "Redmine Smart Companion"
          text: "An Electron/React + FastAPI Plan → Track → Review → Log desktop workflow."
          href: "/en/redmine-tracker/"
          image: "/postImg/Redmine-Tracker/plan-track-log-flow.svg"
          imageAlt: "Redmine Smart Companion desktop time-entry workflow"
    - id: education-research
      group: appendix
      variant: appendix
      kicker: "A3 · Education and selected research"
      title: "Education and Selected Research"
      items:
        - title: "National Cheng Kung University"
          text: "M.S., Biomedical Engineering"
        - title: "National Chin-Yi University of Technology"
          text: "B.S., Electronic Engineering"
        - title: "Projectile Vector Doppler Imaging"
          text: "High-frequency ultrasound vector-Doppler research"
          href: "/en/projectile-vector-doppler-imaging/"
        - title: "Evaluation of Hand Tendon Movement"
          text: "Finger-tendon movement assessment"
          href: "/en/evaluation-of-hand-tendon-movement/"
    - id: other-projects
      group: appendix
      variant: gallery
      kicker: "A4 · Other projects"
      title: "Other Projects"
      summary: "Cross-domain work to open during Q&A."
      items:
        - title: "Pose Detection"
          href: "/en/pose-detection/"
          image: "/postImg/pose-detection/1.jpg"
          imageAlt: "Pose-detection project thumbnail"
        - title: "X-ray Classification"
          href: "/en/covid19-chestxray/"
          image: "/postImg/covid19-chastXray/1.jpg"
          imageAlt: "Chest X-ray classification project thumbnail"
        - title: "Fingerprint Enhancement"
          href: "/en/fingerprint-dirt-fix/"
          image: "/postImg/fingerprint-dirt-fix/1.jpg"
          imageAlt: "Fingerprint-image enhancement project thumbnail"
        - title: "Four-bar Linkage"
          href: "/en/4-bar-linkage/"
          image: "/postImg/4-Bar Linkage/1.png"
          imageAlt: "Four-bar linkage simulation project thumbnail"
        - title: "IoT Monitoring"
          href: "/en/物聯網溫溼度感測器即時監控系統/"
          image: "/postImg/物聯網溫溼度感測器即時監控系統/0.png"
          imageAlt: "IoT temperature and humidity monitoring project thumbnail"
        - title: "Long-term Care Platform"
          href: "/en/長照2.0服務整合平台/"
          image: "/postImg/長照2.0服務整合平台/1.png"
          imageAlt: "Long-term care service integration platform thumbnail"
    - id: disclosure-notes
      group: appendix
      variant: appendix
      kicker: "A5 · Claim and disclosure notes"
      title: "Claim and Disclosure Notes"
      bullets:
        - "Server thermal-control work is described as patent-application experience; this deck makes no grant-status or ownership claim."
        - "Percentage improvements without a publishable baseline and conditions are excluded from the core story."
        - "The 35 μm description comes from the linked public research case; formal citation should use the original paper or conference record."
        - "The AI Quality Pilot GitHub version is a de-identified generic architecture with Supported / Partial / Planned capability levels."
        - "Corporate cases exclude customers, product models, internal hosts, accounts, topology, coefficients, thresholds, and test data."
---
