---
title: Exit SSH commands
category: Projects
priority: Medium
starred: None
created: 2025-12-07T00:59:48.908075
updated: 2025-12-07T00:59:56.447946
dg-publish: true
---
# Exit SSH commands

**Priority:** Medium

## Conversation

### Assistant

Use the appropriate method based on your situation:

### 1. Exit the SSH session (log out from the remote machine)
```bash
exit
```
or
```bash
logout
```
or press:
```bash
Ctrl + D
```

---

### 2. If you are stuck in a frozen SSH session
Press:
```bash
Enter
~.
```
(That is a newline, then tilde, then dot.)

---

### 3. If you are inside a program running over SSH (not the shell)
Use the program’s exit command, for example:
- `q` → quit (for `less`, `man`)
- `:q` → quit (for `vim`)
- `Ctrl + C` → stop a running process

If you specify what screen you are stuck on, the exact exit command can be given.

---

