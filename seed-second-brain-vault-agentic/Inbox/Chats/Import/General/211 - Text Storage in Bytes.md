---
title: Text Storage in Bytes
category: General
priority: Medium
starred: None
created: 2024-12-07T04:57:16.464887
updated: 2024-12-07T04:57:23.889353
dg-publish: true
---
# Text Storage in Bytes

**Priority:** Medium

## Conversation

### Assistant

The number of characters you can store in **144 bytes** depends on the encoding used to represent the text. Here's a breakdown:

1. **ASCII or ISO 8859-1 (Latin-1):**
   - Each character is 1 byte.
   - You can store **144 characters**.

2. **UTF-8 Encoding:**
   - Characters in the basic ASCII range (e.g., English letters, numbers, basic symbols) take **1 byte per character**.
   - Special characters outside the ASCII range (e.g., accented letters, non-Latin scripts) can take 2 to 4 bytes each.
   - You can store up to **144 ASCII characters**, but fewer if non-ASCII characters are included.

3. **UTF-16 Encoding:**
   - Most characters (e.g., those in the Basic Multilingual Plane) take **2 bytes** each.
   - Supplementary characters take 4 bytes.
   - You can store up to **72 characters** for most common texts.

4. **UTF-32 Encoding:**
   - Every character takes **4 bytes**.
   - You can store exactly **36 characters**.

### Summary:
- For ASCII text: **144 characters**
- For general UTF-8: **Varies, up to 144 characters** for pure ASCII, fewer for non-ASCII.
- For UTF-16: **Up to 72 characters**
- For UTF-32: **36 characters**

What text you store will determine the actual count.

---

