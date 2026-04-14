---
title: Display recent notes
category: General
priority: Medium
starred: None
created: 2025-10-17T10:18:19.685282
updated: 2025-10-17T10:18:37.451333
dg-publish: true
---
# Display recent notes

**Priority:** Medium

## Conversation

### Assistant

In **Obsidian**, you can show your **most recent notes** in several ways depending on how you prefer to work — using built-in sorting, community plugins, or Dataview queries. Here are the best methods 👇  

---

## 🧭 1. Using the File Explorer (Quick Way)
- Open the **File Explorer** pane (default on the left).  
- Click the **“Sort” icon** (two arrows).  
- Choose **“Sort by Modified Time”** → “Descending.”  
Now the newest notes appear at the top of the list.

---

## ⚡ 2. Using the **Recent Files** Plugin (Built-in)
1. Go to **Settings → Core Plugins → Enable “Recent Files.”**  
2. Then open the **Command Palette (Cmd/Ctrl + P)** → type “Recent Files: Show list.”  
3. You’ll get a floating list of your most recently opened notes.  
   You can even **pin** this to your sidebar for quick access.

---

## 📊 3. Using **Dataview** Plugin (Dynamic List)
If you want an automatically updating list of recently *modified* notes inside a dashboard note:

```dataview
TABLE file.mtime as "Last Modified"
FROM ""
SORT file.mtime desc
LIMIT 10
```

➡️ This shows your 10 most recently modified notes, with modification dates.

**Tips:**
- Replace `FROM ""` with `FROM "foldername"` to restrict to a folder.
- Use `file.ctime` instead of `file.mtime` for *creation time*.
- Add `FLATTEN dateformat(file.mtime, "yyyy-MM-dd HH:mm")` for a prettier date.

---

## 🧩 4. Using **Home Tab / Recent Files Plugin (Community)**
Install from **Community Plugins → “Recent Files” or “Homepage” or “Smart Random Note.”**  
These can display your recent notes automatically when you open Obsidian.

---

Would you like me to show you a **ready-to-paste dashboard snippet** that lists your 10 most recent notes with clickable links and formatted timestamps (for your Obsidian Home note)?

---

