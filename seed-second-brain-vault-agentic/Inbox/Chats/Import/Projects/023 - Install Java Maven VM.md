---
title: Install Java Maven VM
category: Projects
priority: Medium
starred: None
created: 2025-12-02T09:28:39.247683
updated: 2025-12-02T09:31:06.530783
dg-publish: true
---
# Install Java Maven VM

**Priority:** Medium

## Conversation

### Assistant

This error is **not your fault**.  
It happens because your VM is **ARM64 (aarch64)** and Ubuntu’s **ports.ubuntu.com** mirrors are giving **corrupted or outdated package indexes**.

This specific error:

```
Hash Sum mismatch  
404 Not Found  
```

means:

- The mirror index says a package should have checksum X  
- But Ubuntu server actually returns a different file (checksum Y), or file missing  
- This breaks apt and stops installation

This is **very common on ARM64 Ubuntu servers inside VirtualBox**, because:

1. VirtualBox **does NOT emulate ARM64**.  
2. So you are running an **ARM64 disk image** incorrectly.  
3. Ubuntu ARM repos are often outdated or inconsistent.

**Your VM is ARM64, but your CPU (x86) can’t run ARM64 — VirtualBox fakes half of it**, causing broken package downloads.

---

# Confirm what architecture your VM is reporting

Run:

```bash
uname -m
```

If it prints:

```
aarch64
arm64
```

then your VM is **ARM**, which is wrong for VirtualBox.

VirtualBox **supports only x86_64 VMs**, not ARM.

---

# Why this causes the errors

Because:

- Your ARM64 VM requests ARM packages  
- Ubuntu ARM mirrors serve inconsistent/corrupt packages  
- apt checks the hash → mismatch → fails

That’s why you’re seeing dozens of:

```
Hash Sum mismatch
404 Not Found
```

---

# Fix (the ONLY correct fix)

## **Solution: Install the x86_64 Ubuntu ISO in VirtualBox**

Download **Ubuntu 22.04 or 24.04 (Desktop or Server) — AMD64 (x86_64) version**:

https://ubuntu.com/download/desktop

Make sure file name contains:

```
amd64.iso
```

NOT:

```
arm64.iso  
aarch64.iso  
armhf.iso
```

Then reinstall OS in VirtualBox.

---

# Temporary workaround (not recommended but possible)

If you want to “try”, you can run:

```bash
sudo rm -rf /var/lib/apt/lists/*
sudo apt update --fix-missing
```

But ARM64 VM on VirtualBox **will keep failing forever**, especially with `openjdk-21` and any big package.

---

# Summary

| Reason | Explanation |
|--------|-------------|
| VirtualBox doesn’t support ARM64 | It only supports x86_64 VMs |
| You mistakenly installed ARM Ubuntu | It boots, but apt repos are corrupt/out-of-sync |
| apt breaks instantly | Hash mismatch and 404s |
| Real fix | Install x86_64 (amd64) Ubuntu ISO |

---

If you want, tell me your exact VM setup and I’ll guide you step-by-step to reinstall correctly.

---

