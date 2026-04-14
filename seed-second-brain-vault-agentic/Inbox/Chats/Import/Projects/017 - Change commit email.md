---
title: Change commit email
category: Projects
priority: Medium
starred: None
created: 2025-12-12T18:18:02.037603
updated: 2025-12-12T18:32:42.589949
dg-publish: true
---
# Change commit email

**Priority:** Medium

## Conversation

### Assistant

On **macOS**, the cleanest way is to use the built-in **Shortcuts** app and assign a keyboard shortcut.

---

## Method 1 (Recommended): macOS Shortcuts

### Step 1: Create the shortcut
1. Open **Shortcuts** app
2. Click **+** (New Shortcut)
3. Name it: e.g. `Open Meditation Dashboard`
4. Add action: **Open URLs**
5. Enter the webpage URL
6. (Optional) Add action **Open App** → select **Safari**
   - This forces Safari even if another browser is default

---

### Step 2: Assign a keyboard shortcut
1. Click the **ⓘ (Info)** button (top-right)
2. Enable **Use as Quick Action**
3. Check **Services**
4. Click **Add Keyboard Shortcut**
5. Press your shortcut (example):
   - `⌃ Control + ⌥ Option + D`

Close Shortcuts.

---

### Step 3: Use it
Press your shortcut → Safari opens the webpage instantly.

---

## Method 2: Automator (older but still works)

1. Open **Automator**
2. Create **Quick Action**
3. Set:
   - Receives: *no input*
   - In: *any application*
4. Add **Open URLs**
5. Add your URL
6. Save
7. Go to:
   - **System Settings → Keyboard → Keyboard Shortcuts → Services**
8. Assign a shortcut

---

## Recommended shortcut patterns (avoid conflicts)
- `⌃⌥ + letter`
- `⌃⌥⌘ + letter`

Example:
- `⌃⌥⌘M` → Meditation app page
- `⌃⌥⌘L` → LinkedIn post draft

---

If you want:
- one shortcut per project
- open **multiple tabs**
- open in **specific Safari profile**
- open + run JS (for dashboards)

say which one and I’ll tailor it.

---

