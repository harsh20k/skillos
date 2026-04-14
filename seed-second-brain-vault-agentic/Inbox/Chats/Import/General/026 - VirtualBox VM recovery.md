---
title: VirtualBox VM recovery
category: General
priority: Medium
starred: None
created: 2025-12-06T23:49:18.845125
updated: 2025-12-06T23:51:57.110018
dg-publish: true
---
# VirtualBox VM recovery

**Priority:** Medium

## Conversation

### Assistant

image_group{"layout":"carousel","query":["VirtualBox Failed to acquire the VirtualBox COM object NS_ERROR_FAILURE 0x80004005 macOS"]}

### What this error means

**“Failed to acquire the VirtualBox COM object (NS_ERROR_FAILURE 0x80004005)”** means:
- The **VirtualBox background service (`VBoxSVC`) is broken or locked**, and
- The **global VirtualBox configuration is corrupted or pointing to missing disk media** (which fits exactly with your SSD being unplugged while VMs were running).

This is **not a VM-level error** — it is a **VirtualBox core service failure**, so:
- The GUI cannot start
- No VM state can be accessed
- Restarting the app alone does nothing

---

## ✅ Correct Recovery Procedure (Do These in Order)

### 1️⃣ Force-stop all VirtualBox services (mandatory)

Run this exactly:

```bash
pkill -f VirtualBox
pkill -f VBoxHeadless
pkill -f VBoxSVC
```

Verify nothing is running:

```bash
ps aux | grep VBox
```

If anything remains → kill it again.

---

### 2️⃣ Reconnect the SSD and verify mount path

Your VMs **must be visible again at the exact path** VirtualBox expects.

Check:

```bash
ls /Volumes
```

If your SSD name changed (very common), **rename it back to the original name**.

---

### 3️⃣ Reset only the corrupted VirtualBox global config (safe)

This fixes the COM object failure without deleting VMs:

```bash
mv ~/.config/VirtualBox ~/.config/VirtualBox.broken
```

Also reset cache:

```bash
rm -rf ~/Library/VirtualBox
```

Now relaunch:

```bash
open -a VirtualBox
```

✅ In most cases, **this alone clears the COM object error**.

---

### 4️⃣ If VMs appear but show “Paused” → Discard State

For each VM:

```
Right-click → Discard Saved State → Start
```

If GUI freezes:

```bash
VBoxManage list vms
VBoxManage discardstate "VM_NAME"
```

---

## ❌ What NOT to Do

| Action | Result |
|--------|--------|
| Clicking “Resume” | Can corrupt the disk |
| Reinstalling VirtualBox first | Leaves corrupted config |
| Deleting `.vdi` files | Permanent VM data loss |
| Letting macOS “repair” the disk | Can break UUID mapping |

---

## ✅ Why This Happened (Technically)

When you unplugged the SSD **while VMs were actively writing**:

- `VBoxSVC` kept a **lock on missing disk UUIDs**
- The COM object database became **invalid**
- VirtualBox now crashes at startup with:
  ```
  NS_ERROR_FAILURE (0x80004005)
  ```

VirtualBox **cannot tolerate hot removal of active VM storage**.

---

## ✅ What I Need From You (If It Still Fails)

If after Step 3 the error still appears, run:

```bash
/Applications/VirtualBox.app/Contents/MacOS/VirtualBox
```

and paste the **full terminal error output**.  
That reveals exactly which internal registry or UUID is broken.

---

### ✅ Summary

This error = **corrupted VirtualBox core after live SSD removal**  
**Fix path:**  
1. Kill all VBox services  
2. Reattach SSD with same name  
3. Reset `~/.config/VirtualBox` and `~/Library/VirtualBox`  
4. Discard paused states  

---

Proceed with **Steps 1–3 now** and report:
- Does VirtualBox launch afterward?
- Do your VMs reappear?

---

