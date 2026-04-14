---
title: MDS store in Activity Monitor
category: Projects
priority: Medium
starred: None
created: 2025-12-16T14:51:42.720855
updated: 2025-12-16T17:25:16.736091
dg-publish: true
---
# MDS store in Activity Monitor

**Priority:** Medium

## Conversation

### Assistant

**`deutexperd`** is a macOS system daemon related to **on-device text understanding and intelligence**.

### What it does
- `deutexperd` = **DEUT (Device Understanding & Text Processing) Expert Daemon**
- Performs local analysis of text for Apple’s intelligence features
- Supports:
  - Text recognition and classification
  - Suggestions, summaries, and language understanding
  - Features used by Siri, Spotlight, Notes, Mail, Photos, and other apps
  - Apple Intelligence / Core ML text pipelines (on-device)

### Why it appears in Activity Monitor
You may see it active when:
- Spotlight indexes text-heavy files
- Notes, Mail, or Messages process content
- PDFs or documents are opened
- System updates refresh language models
- Apple Intelligence features run locally

Short CPU spikes are normal.

### Is it safe?
- Yes. It is a **legitimate macOS system process**
- Sandboxed and managed by the OS
- Restarts automatically if stopped

### When resource usage is noticeable
Typically during:
- First-time analysis of documents
- Large folders with many text files
- System or language model updates

It should settle once processing completes.

### When to investigate
Only if:
- CPU usage remains high for an extended period
- No apps using text or search features are active

Possible steps:
- Restart the Mac
- Let indexing finish
- Reduce Spotlight indexing scope if needed

### Summary
- `deutexperd` handles on-device text intelligence
- Normal background macOS service
- Temporary activity is expected
- Not malware and not removable

If you want, provide **CPU %, duration, and what you were doing**, and I can confirm whether it’s behaving normally.

---

