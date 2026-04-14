---
title: Push notifications overview
category: General
priority: Medium
starred: None
created: 2025-11-07T15:22:09.236698
updated: 2025-11-08T01:31:17.293837
dg-publish: true
---
# Push notifications overview

**Priority:** Medium

## Conversation

### Assistant

Yes. GitHub and Git both let you track a file’s full history.  

---

### 🧩 Option 1 — Using the GitHub website
1. Open the repository on GitHub.  
2. Navigate to the file.  
3. Click the **“History”** button (top-right of the file view).  

You’ll see every commit that modified that file, with author, date, and message.  
You can click any commit to view the file’s content at that point in time or compare changes line by line.

---

### 🧩 Option 2 — Using Git in your terminal
From your repo folder:
```bash
git log -- path/to/file
```
Shows commit history for that file.

For inline diffs:
```bash
git log -p -- path/to/file
```

For a concise summary of who changed which lines:
```bash
git blame path/to/file
```

To see how the file looked at a specific commit:
```bash
git show <commit_id>:path/to/file
```

---

### ✅ Summary
| Task | Command / Action |
|------|------------------|
| View commits on GitHub | **History** button |
| View commits in terminal | `git log -- path/to/file` |
| See changes per commit | `git log -p -- path/to/file` |
| See line authorship | `git blame path/to/file` |
| View file at past commit | `git show <commit_id>:file` |

All changes to a file since it was added are fully traceable this way.

---

