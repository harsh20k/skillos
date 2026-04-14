---
title: App storage location explanation
category: Projects
priority: Medium
starred: None
created: 2025-11-12T09:54:16.397811
updated: 2025-11-12T10:20:46.822360
dg-publish: true
---
# App storage location explanation

**Priority:** Medium

## Conversation

### Assistant

You’re seeing **“Operation not permitted”** because that folder is inside  
```
/System/Library/AssetsV2/
```
which is **protected by macOS System Integrity Protection (SIP)**.  
Even `sudo` cannot modify or delete files there unless SIP is disabled.

### You have two options

#### Option 1 – Safe (recommended)
Leave it alone or remove it **via Xcode**:
1. Open **Xcode → Settings → Platforms**.  
2. Find the iOS Simulator runtime version you don’t need.  
3. Right-click → **Delete**.  
   Xcode removes those `.dmg` files safely and updates internal links.

#### Option 2 – Force (not recommended)
If you truly want to delete manually:
1. **Reboot into Recovery mode**  
   (hold **⌘ + R** while booting).  
2. Open **Terminal** → run  
   ```bash
   csrutil disable
   reboot
   ```
3. After reboot, delete the folder with:
   ```bash
   sudo rm -rf "/System/Library/AssetsV2/com_apple_MobileAsset_iOSSimulatorRuntime"
   ```
4. Then re-enable SIP:
   - Reboot into Recovery again, open Terminal, and run:
     ```bash
     csrutil enable
     reboot
     ```

**Summary:** The “not permitted” message isn’t a permission bug—it’s SIP protecting system files. Delete through Xcode or disable SIP only temporarily if you fully understand the risk.

---

