---
title: Check Java SDK Mac
category: General
priority: Medium
starred: None
created: 2025-10-22T18:26:34.543842
updated: 2025-10-22T18:26:41.805168
dg-publish: true
---
# Check Java SDK Mac

**Priority:** Medium

## Conversation

### Assistant

You can check if Java SDK (JDK) is installed on your Mac in a few simple ways:  

### 🧭 Option 1: Use Terminal
1. Open **Terminal** (press `Cmd + Space` → type “Terminal” → hit Enter).
2. Type:
   ```bash
   java -version
   ```
   or
   ```bash
   javac -version
   ```

**Interpret the results:**
- If you see something like  
  ```
  java version "17.0.9" 2023-10-17 LTS
  Java(TM) SE Runtime Environment ...
  ```
  → ✅ You have Java (JDK) installed.
- If it says  
  ```
  No Java runtime present, requesting install.
  ```
  → ❌ Java is **not installed** (macOS may prompt you to install it).

---

### 🧱 Option 2: Check installation path
You can also check if the JDK folder exists:
```bash
/usr/libexec/java_home -V
```
If you see output listing paths like:
```
Matching Java Virtual Machines (1):
    17.0.9 (arm64) "Oracle Corporation" - "/Library/Java/JavaVirtualMachines/jdk-17.0.9.jdk/Contents/Home"
```
→ Java SDK is installed there.

---

### 🧩 Option 3: Check in Finder
Open Finder and navigate to:
```
/Library/Java/JavaVirtualMachines/
```
If you see folders like `jdk-17.jdk` or `zulu-21.jdk`, those are installed JDKs.

---

Would you like me to show how to install or update the JDK (e.g. to Java 21 or 17)?

---

