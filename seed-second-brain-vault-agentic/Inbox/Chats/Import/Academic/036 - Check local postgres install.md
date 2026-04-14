---
title: Check local postgres install
category: Academic
priority: Medium
starred: None
created: 2025-11-03T22:24:43.258108
updated: 2025-11-04T00:24:49.704955
dg-publish: true
---
# Check local postgres install

**Priority:** Medium

## Conversation

### Assistant

Run this in the repo root (where `package.json` exists):  

```bash
npm install
```

That command:  
- Reads all dependencies listed in `package.json`  
- Downloads them into the local `node_modules` folder  

---

If your project uses **yarn** or **pnpm**, use the matching command instead:  
```bash
yarn install
# or
pnpm install
```

---

To confirm installation succeeded:
```bash
npm list --depth=0
```

---

