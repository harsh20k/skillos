---
title: Maven build failure fix
category: General
priority: Medium
starred: None
created: 2025-12-04T13:37:54.823263
updated: 2025-12-04T17:12:03.199969
dg-publish: true
---
# Maven build failure fix

**Priority:** Medium

## Conversation

### Assistant

Create a script like this on your VM.

## 1. Create the script

```bash
nano reset_nemo.sh
```

Add the following:

```bash
#!/bin/bash

# Delete the entire nemo directory if it exists
rm -rf nemo

# Recreate a fresh empty directory
mkdir nemo

# Optional: show confirmation
echo "nemo directory reset."
```

Save and exit.

---

## 2. Make executable

```bash
chmod +x reset_nemo.sh
```

---

## 3. Run it

```bash
./reset_nemo.sh
```

This performs:

- `rm -rf nemo` → removes folder and all contents  
- `mkdir nemo` → creates new empty directory  

If you want to do additional steps (like listing inside it), tell me.

---

