---
title: Weekly personal projects
category: Academic
priority: Medium
starred: None
created: 2025-09-22T10:31:38.615936
updated: 2025-10-28T11:20:15.173841
dg-publish: true
---
# Weekly personal projects

**Priority:** Medium

## Conversation

### Assistant

To **change your global Git email**, follow these simple steps 👇  

---

### 🪄 Step-by-step

1. **Check your current global email**
   ```bash
   git config --global user.email
   ```

2. **Set a new global email**
   ```bash
   git config --global user.email "your_new_email@example.com"
   ```

3. **Verify it was updated**
   ```bash
   git config --global --list
   ```
   You should now see something like:
   ```
   user.name=Your Name
   user.email=your_new_email@example.com
   ```

---

### 💡 Optional
If you only want to set the email for the **current project** (not all repos):
```bash
git config user.email "your_project_specific_email@example.com"
```
This writes the setting into the local repo’s `.git/config` instead of your global config.

---

### 📁 Where it’s stored
- Global config → `~/.gitconfig`  
- Local config → `.git/config` inside your repo  

You can open and edit those files manually too if needed.

---

Would you like me to show how to **link your Git commits to your GitHub account email** (to avoid “unverified commit” warnings)?

---

