---
title: Battery-Efficient Timer Design
category: Projects
priority: Medium
starred: None
created: 2025-07-14T07:41:47.102260
updated: 2025-07-14T13:23:13.343750
dg-publish: true
---
# Battery-Efficient Timer Design

**Priority:** Medium

## Conversation

### Assistant

By default Xcode runs your app in the Simulator using the **Debug** configuration, so you usually just:

1. **Select your scheme & destination**  
   - In the toolbar at the top, click the Scheme pop-up (it shows your app’s name).  
   - Make sure your app’s scheme is selected.  
   - Immediately to its right, pick an iOS Simulator (e.g. “iPhone 15 Pro”).

2. **Run (build + launch)**  
   - Hit **⌘R** (Product → Run), or click the ▶️ button in the toolbar.  
   - Xcode will compile under the **Debug** configuration and launch the app in the Simulator.

3. **(Optional) Just Build**  
   - If you only want to compile (no launch), hit **⌘B** (Product → Build).  
   - This uses the same Debug configuration, but won’t start the Simulator.

4. **Verify Your Build Configuration**  
   - Go to Product → Scheme → Edit Scheme…  
   - Under the **Run** action, confirm **Build Configuration** is set to **Debug**.  
   - You can also check the **Build** action to see that “Debug” is the default for your scheme.

---

**Tip:**  
- Any breakpoints you’ve set will be active.  
- Your `print(...)` and `os_log` output will appear in Xcode’s console when you run under Debug.

---

