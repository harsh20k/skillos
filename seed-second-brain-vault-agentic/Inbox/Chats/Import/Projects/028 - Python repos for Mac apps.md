---
title: Python repos for Mac apps
category: Projects
priority: Medium
starred: None
created: 2025-11-18T15:18:11.905943
updated: 2025-11-24T09:32:02.871421
dg-publish: true
---
# Python repos for Mac apps

**Priority:** Medium

## Conversation

### Assistant

Use **cloc**. It is the most reliable and widely used tool for counting lines of code in a repository while excluding unwanted file types.

## Recommended Tool: **cloc (Count Lines of Code)**

### Why cloc?
- Excludes file types automatically (Markdown, images, JSON, etc.)
- Lets you specify which files to count
- Works on macOS, Windows, Linux
- Very accurate for large repositories

---

## Install on macOS
```
brew install cloc
```

---

## Count lines in a repo (excluding markdown and other file types)

### Basic usage
```
cloc .
```

### Exclude specific file types
```
cloc . --exclude-ext=md,txt,json,yml
```

### Exclude entire folders
```
cloc . --exclude-dir=tests,docs,build
```

### Combine both
```
cloc . --exclude-ext=md,txt,json,yml --exclude-dir=tests,docs,examples
```

---

## Example Output
```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                         112           2021           1533           9874
-------------------------------------------------------------------------------
```

---

## Alternative Tools (optional)

### 1. **tokei**
Fast, modern alternative written in Rust.
```
brew install tokei
```

Usage:
```
tokei .
tokei . --exclude tests --exclude *.md
```

### 2. **scc** ('sloc clone')
Another fast LOC counter.
```
brew install scc
```

Usage:
```
scc --exclude-dir docs --exclude-ext md .
```

---

## Best Choice
If you want **accuracy + customization + easy filtering**, go with:

### → **cloc**

If you want **speed**, pick:

### → **tokei**

---

If you want, I can also write a **one-liner script** that automatically removes common non-code files and shows only Python LOC.

---

