---
title: "Fully Automated Tech Information Aggregation Platform: Content Workflow Based on n8n and Local LLM"
slug: lightnews
date: 2025-08-15
categories:
- Professional Technology
tags:
- Automation
- n8n
- Ollama
- Deep Learning & Machine Learning
- Web Scraping
- RSS
- WordPress
thumbnailImagePosition: left
thumbnailImage: /postImg/lightnews/thumbnail-v2.png
---

Lightnews is a technical-content workflow hosted on Linux. n8n watches RSS feeds, cleans source pages, calls a local Ollama model for summaries and Traditional Chinese translation, retrieves image candidates, and hands reviewable posts to WordPress through its REST API. It automates repetitive processing while preserving editorial judgment.

<!--more-->

## Project Context

Curating international technical articles manually requires repeated context switching among source discovery, summarization, translation, classification, imagery, and a CMS. The original project description observed that information could lag by days or weeks; that is a workflow observation, not a measured service-level metric.

The project aims to produce a consistently structured Traditional Chinese draft first, allowing a human editor to focus on source fidelity, technical meaning, licensing, and the publish decision rather than moving fields by hand.

![Lightnews trust-boundary and editorial pipeline across external sources, local inference, CMS draft, and human review](/postImg/lightnews/editorial-pipeline-v2.svg)

## Architecture and Data Flow

1. **RSS watch and extraction:** n8n monitors selected sources, fetches a discovered page, and removes advertising and unrelated HTML.
2. **Local text inference:** Cleaned text is sent to `gpt-oss` through Ollama for summarization, Traditional Chinese translation, technical tags, and visual keywords.
3. **External image retrieval:** Visual keywords are sent to the Unsplash API; download and relevance signals rank/select an image candidate.
4. **CMS handoff:** n8n assembles title, body, tags, and image links, then uses the WordPress REST API to create a draft or publish according to the workflow.
5. **Editorial gate:** A draft still needs review for source meaning, translation, image licensing/attribution, and publication suitability.

“Local” applies specifically to text inference on the self-managed Linux host, reducing dependence on an external LLM API. RSS/source pages, Unsplash, and WordPress remain external service boundaries, so the workflow is neither fully offline nor entirely private.

![Existing Lightnews automated processing flow](/postImg/lightnews/pipeline.svg)
*Architecture diagram showing the main RSS, cleaning, local-LLM, image-selection, and WordPress-draft stages.*

## Technical Decisions

### Why n8n

n8n keeps API nodes, conditional branches, and failure paths visible on one orchestration surface, which suits an integration-heavy workflow. It replaces scattered crontab scripts as the coordinator, but individual nodes still require retry, validation, and monitoring policies.

### Why a Local LLM

Summarization, translation, and classification process substantial text. Local Ollama inference reduces the need to send that text to a third-party LLM API and provides control over model deployment. This does not guarantee translation accuracy: no benchmark set or human score is public, so generated text remains a draft for review.

### Image and Publication Boundaries

Unsplash download and relevance data are candidate-ranking signals, not proof that an image is “best” or automatically compliant with every licensing and attribution requirement. WordPress can create drafts or publish, but the safer default story is reviewable output before release.

## Visible Evidence and Limitations

The screenshot below demonstrates a browsable Traditional Chinese site surface. It does not establish uptime, throughput, translation quality, or editorial error rates.

![Lightnews Traditional Chinese technology-news website](/postImg/lightnews/1.jpg)
*Live-site capture showing articles, categories, and publication-time presentation.*

Public material does not include an n8n workflow export, retry policy, update-frequency record, content-quality evaluation, or licensing audit. A future evaluation should track human review time per post, translation edit rate, source/image attribution completeness, and workflow failure/retry rate.

## Stack

**Linux · n8n · Ollama (`gpt-oss`) · RSS · Web extraction · Unsplash API · WordPress REST API**

## Live Site

> **External-content note:** The iframe below loads content from `lightnews.tw`; availability, cookies, and browser security settings are controlled outside this portfolio.

If the embedded site is unavailable, use the visible fallback link: [Open Lightnews](https://lightnews.tw/).

<iframe src="https://lightnews.tw/" title="External Lightnews website" width="100%" height="500" loading="lazy" style="border:0;max-width:100%;"></iframe>
