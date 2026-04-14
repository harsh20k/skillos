---
title: CMake error fix
category: Academic
priority: Medium
starred: None
created: 2025-11-19T07:27:46.156351
updated: 2025-11-19T07:46:48.580428
dg-publish: true
---
# CMake error fix

**Priority:** Medium

## Conversation

### Assistant

Your `keytool` is working — it just uses a slightly older syntax, so **`-version` is not supported**. That’s fine.  
You can still generate the keystore normally.

Now let’s generate the missing `debug.keystore`.

---

# ✅ **STEP 1 — Navigate to app folder**

Run this from your project root:

```bash
cd android/app
```

Confirm you are inside:

```bash
pwd
```

Should show:

```
.../frontend/android/app
```

---

# ✅ **STEP 2 — Generate debug.keystore**

Use this exact command (compatible with the keytool version you have):

```bash
keytool -genkeypair \
 -storetype PKCS12 \
 -keystore debug.keystore \
 -alias androiddebugkey \
 -keyalg RSA \
 -keysize 2048 \
 -validity 10000 \
 -storepass android \
 -keypass android \
 -dname "CN=Android Debug,O=Android,C=US"
```

After running it, verify the file exists:

```bash
ls
```

You should see:

```
debug.keystore
```

---

# ✅ **STEP 3 — Rebuild the app**

Go back to project root:

```bash
cd ../..
```

Then:

```bash
npx react-native run-android
```

---

# 🎉 This will fix the current error:
```
validateSigningDebug FAILED
debug.keystore not found
```

Because the keystore now exists, the build will pass signing.

---

# If anything fails, send:

```
ls android/app
```

and I’ll check the folder structure.

---

