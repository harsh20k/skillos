---
title: Error fixing C++ header
category: Academic
priority: Medium
starred: None
created: 2025-10-06T12:31:31.259818
updated: 2025-10-06T12:31:48.328712
dg-publish: true
---
# Error fixing C++ header

**Priority:** Medium

## Conversation

### Assistant

The error in your screenshot:  

```
fatal error: 'type_traits' file not found
```

means the compiler cannot locate the standard C++ header `<type_traits>`, which is part of the **C++ standard library (libc++)**.  
This usually happens when building a C++ project (like **pgModeler**) on macOS with **Homebrew-installed Qt** and an **incomplete or misconfigured compiler environment**.

---

### 🔍 What’s likely happening

`/opt/homebrew/lib/QtCore.framework/Headers/qglobal.h` includes `<type_traits>`, but:
- The **C++ standard library include path** isn’t found by the compiler,  
- or you’re using **an older/missing Xcode Command Line Tools**,  
- or **CMake/qmake** isn’t pointing to the right compiler.

---

### 🧩 Step-by-step fix

#### 1. Verify Xcode Command Line Tools
Run:
```bash
xcode-select --install
```
If it says they’re already installed, check the active path:
```bash
xcode-select -p
```
✅ Expected output:
```
/Library/Developer/CommandLineTools
```
If it’s not, fix it:
```bash
sudo xcode-select --switch /Library/Developer/CommandLineTools
```

---

#### 2. Reinstall or update CLT headers (for `<type_traits>`)
Sometimes the headers are missing. Run:
```bash
sudo xcode-select --reset
sudo xcodebuild -runFirstLaunch
```

Then check if the header exists:
```bash
ls /Library/Developer/CommandLineTools/usr/include/c++/*/type_traits
```

If it exists, the compiler can find it again.

---

#### 3. Ensure correct compiler flags in your build

If you’re building manually (e.g., with `make`), ensure that `CXXFLAGS` include:
```bash
-std=c++17 -stdlib=libc++
```

If you’re using `qmake` or `cmake`, re-run configuration:
```bash
qmake CONFIG+=release
make clean
make
```
or for cmake:
```bash
cmake -DCMAKE_CXX_STANDARD=17 -DCMAKE_CXX_FLAGS="-stdlib=libc++" ..
make
```

---

#### 4. Check your compiler version
```bash
clang++ --version
```
✅ Should show something like:
```
Apple clang version 15.0.0 (clang-1500.0.40.1)
```

If not, install via:
```bash
brew install llvm
```
and then use:
```bash
export CC=/opt/homebrew/opt/llvm/bin/clang
export CXX=/opt/homebrew/opt/llvm/bin/clang++
```

Then rebuild.

---

#### 5. (Optional) Clean Homebrew Qt cache
Sometimes Qt built via Homebrew references incorrect include paths:
```bash
brew reinstall qt
brew doctor
```

---

### ✅ Summary of likely fix

Run these in order:
```bash
xcode-select --install
sudo xcode-select --switch /Library/Developer/CommandLineTools
sudo xcodebuild -runFirstLaunch
```
Then rebuild your project:
```bash
make clean
qmake CONFIG+=release
make
```

---

If you’d like, share your **macOS version**, **Qt version**, and **compiler command** you used (`qmake` or `cmake`), and I can give you the **exact command line** to fix the include path issue.

---

