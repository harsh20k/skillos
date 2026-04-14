---
title: Move text to notes
category: Projects
priority: Medium
starred: None
created: 2025-08-18T13:20:39.144039
updated: 2025-08-18T13:33:28.289611
dg-publish: true
---
# Move text to notes

**Priority:** Medium

## Conversation

### Assistant

On a Mac, Finder hides system and “dot” files (like `.gitignore`, `.obsidian`, `.DS_Store`) by default.  
Here are the main ways to show them:

---

## 1. Quick Toggle (Shortcut)
- Open **Finder**.
- Press:  
  **⌘ Command + Shift + . (period)**  
- Hidden files will appear (slightly grayed out).  
- Press the shortcut again to hide them.

---

## 2. Make Them Always Visible (Terminal)
If you want hidden files to **always** show up:

1. Open **Terminal**.
2. Run:
   ```bash
   defaults write com.apple.finder AppleShowAllFiles YES
   killall Finder
   ```
3. To revert (hide them again):
   ```bash
   defaults write com.apple.finder AppleShowAllFiles NO
   killall Finder
   ```

---

## 3. Show Specific Hidden File
- In Finder, press **⌘ + Shift + G** (Go to Folder).
- Type the path, e.g.:
  ```
  ~/.obsidian
  ```
- Finder will open that hidden folder directly.

---

✅ Easiest day-to-day: **⌘ + Shift + .**  
✅ Permanent change: Terminal command.  

---

Do you want me to also show you how to make Finder **always show hidden file extensions** (like `.md`, `.txt`) alongside the hidden dotfiles?

---

