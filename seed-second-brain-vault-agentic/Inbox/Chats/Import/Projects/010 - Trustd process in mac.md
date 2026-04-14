---
title: Trustd process in mac
category: Projects
priority: Medium
starred: None
created: 2025-12-19T15:20:34.514550
updated: 2025-12-19T15:20:50.370551
dg-publish: true
---
# Trustd process in mac

**Priority:** Medium

## Conversation

### Assistant

**`trustd`** is a core macOS **security daemon** responsible for **certificate trust evaluation**.

### What `trustd` does
- Verifies **SSL/TLS certificates** when you visit HTTPS websites.
- Validates certificates used by **apps, system services, software updates**, and **code signing**.
- Checks **certificate chains**, expiration, revocation status (OCSP/CRL), and Apple trust policies.
- Acts as the backend for macOS’s **Keychain trust services**.

### Why you see it running
- It runs automatically in the background.
- CPU usage may spike temporarily when:
  - Opening many HTTPS sites
  - Installing apps
  - First-time certificate checks
  - Network changes (Wi-Fi ↔ Ethernet, VPN)

### Is it safe?
- **Yes.**  
- It is an Apple-signed system process.
- Location (normal):
  ```
  /usr/libexec/trustd
  ```

### When it becomes a problem
If `trustd` is using **high CPU constantly**, common causes are:
- Corrupted certificate cache
- Network issues (captive portals, VPNs, proxies)
- Problematic certificates added to Keychain

### Safe troubleshooting steps
1. Restart the service (it will auto-restart):
   ```bash
   sudo killall trustd
   ```
2. Check for unusual certificates:
   - Open **Keychain Access**
   - Look for manually added or expired root certificates
3. Disable VPN temporarily and test
4. Update macOS (trust policies are updated via system updates)

### Do **not**
- Do not delete `trustd`
- Do not permanently block it via firewall

### Summary
| Aspect | Details |
|---|---|
| Type | System security daemon |
| Purpose | Certificate & trust validation |
| Required | Yes |
| Safe to quit | Temporarily (auto-restarts) |
| Safe to remove | No |

If you are seeing **persistent high CPU or network usage**, describe the symptom (CPU %, network activity, VPN usage), and the root cause can be narrowed precisely.

---

