---
title: Immich vs Nextcloud
category: General
priority: Medium
starred: None
created: 2025-12-19T14:42:31.445368
updated: 2025-12-19T14:42:45.870668
dg-publish: true
---
# Immich vs Nextcloud

**Priority:** Medium

## Conversation

### Assistant

**Immich + Nextcloud** is a common and effective combination. They serve different purposes and complement each other well.

---

## What each tool is best at

### Immich
- Purpose: **Google Photos–like experience**
- Strengths:
  - Automatic photo/video backup from mobile
  - Fast timeline view
  - Face recognition, location maps, memories
  - Excellent mobile UX
- Weakness:
  - Not a general file manager
  - Still evolving (breaking changes possible)

### Nextcloud
- Purpose: **General cloud storage & collaboration**
- Strengths:
  - Files, folders, sharing, permissions
  - Docs, calendar, contacts, notes
  - Mature, stable ecosystem
- Weakness:
  - Photo experience is functional, not delightful
  - Slower for large media libraries

---

## Recommended setup (best practice)

**Use both, with clear separation of responsibility**

- **Immich**
  - Owns: photos & videos
  - Mobile auto-backup enabled
  - Primary photo viewing/searching app

- **Nextcloud**
  - Owns: documents, PDFs, code, backups, shared folders
  - Optional: secondary backup target for Immich exports

You do **not** need to make Nextcloud the primary photo app.

---

## Integration options

### Option A: Separate (simplest, most common)
- Immich stores media in its own volume
- Nextcloud stores everything else
- Zero coupling, fewer issues

### Option B: One-way backup
- Immich → scheduled export → Nextcloud folder
- Nextcloud acts as cold backup / archive

### Option C: Same storage (not recommended)
- Both pointing to same photo directory
- Risky: metadata conflicts, broken indexes

---

## When this combo makes sense
- You want **self-hosted Google Photos replacement**
- You also want **Dropbox/Drive-like storage**
- You value UX for photos and stability for files

## When it doesn’t
- You want **one app only**
- You don’t want to manage Docker or storage volumes

---

## Bottom line
- **Immich for photos**
- **Nextcloud for files**
- Together = best self-hosted cloud stack today

If you want, I can:
- Suggest a **Docker Compose layout**
- Recommend **storage sizing**
- Advise on **backup strategy (3-2-1)**

---

