---
title: Delete file on VM
category: Academic
priority: Medium
starred: None
created: 2025-12-06T20:34:29.076097
updated: 2025-12-06T20:34:36.450591
dg-publish: true
---
# Delete file on VM

**Priority:** Medium

## Conversation

### Assistant

Yes. You delete files on a VM using standard shell commands over an SSH connection.

### 1. Delete a File After Connecting via SSH
```bash
ssh -p 2222 lab@127.0.0.1
rm filename.ext
```

Example:
```bash
rm dbms-test.jar
```

### 2. Delete a File on the VM Without Logging In (Single Command)
```bash
ssh -p 2222 lab@127.0.0.1 "rm /home/lab/nemo/dbms-test.jar"
```

### 3. Safe Delete (Prompt Before Deleting)
```bash
rm -i filename.ext
```

### 4. Force Delete (No Prompts)
```bash
rm -f filename.ext
```

### 5. Delete a Directory
```bash
rm -r foldername
```

### 6. Force Delete a Directory
```bash
rm -rf foldername
```

If required, you can also combine `scp` + `rm` into a single deployment command.

---

