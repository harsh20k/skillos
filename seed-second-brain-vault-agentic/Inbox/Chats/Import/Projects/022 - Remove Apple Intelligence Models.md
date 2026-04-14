---
title: Remove Apple Intelligence Models
category: Projects
priority: Medium
starred: None
created: 2025-12-02T10:40:51.167794
updated: 2025-12-02T10:45:09.251762
dg-publish: true
---
# Remove Apple Intelligence Models

**Priority:** Medium

## Conversation

### Assistant

Understood. Here is the **correct and complete way to remove Apple Intelligence 11 GB on macOS Sequoia**.

Apple Intelligence downloads large on-device models (usually 8–12 GB). macOS does **not** give an obvious delete button, but you *can* remove them in three reliable ways.

---

# 1. Turn Off Apple Intelligence (macOS will delete models automatically)
This is the cleanest method.

Go to:
**System Settings → Privacy & Security → Apple Intelligence → Turn Off**

After turning it off:
- macOS will delete the downloaded models within a few minutes to a few hours.
- Storage reclaims ~8–11 GB.

If you want to force it faster, continue below.

---

# 2. Reset “Siri & Apple Intelligence” (safe, quick)
This forces deletion of on-device model files.

System Settings → **General → Transfer or Reset → Reset** →  
**Reset Siri & Apple Intelligence**

This clears:
- Apple Intelligence models  
- Siri on-device speech models  
- Genmoji / image tools cache

Usually frees **5–11 GB immediately**.

---

# 3. Manually delete the model files (advanced, guaranteed)
If you want to delete them *right now*, remove the model directory.

Open Terminal and run:

```sh
rm -rf ~/Library/Apple/OnDeviceML
```

and also:

```sh
rm -rf /Library/Apple/OnDeviceML
```

These folders contain:
- Foundation models (LLMs)
- Image generation models
- Writing Tools models
- Siri on-device models  
Total: 7–12 GB.

macOS will recreate them only if you re-enable Apple Intelligence features.

---

# 4. Disable the features so models don’t download again
After deletion, ensure these are OFF:

System Settings → **Siri & Spotlight**
- Writing Tools → OFF  
- Image Playground → OFF  
- Clean Up → OFF  
- Genmoji → OFF  
- Siri on-device processing → OFF  
- Suggestions → OFF

System Settings → **Privacy & Security → Apple Intelligence** → OFF

---

# Quick Recommendation
If you want to reclaim space **right now**, run this and you’re done:

```sh
rm -rf ~/Library/Apple/OnDeviceML
```

If you prefer **safe UI-only**, use:
Reset Siri & Apple Intelligence → Turn Off Apple Intelligence.

---

If you tell me your macOS version and whether you want **safe option** or **terminal option**, I’ll give the exact steps tailored for you.

---

