---
title: Ls files starting with fish
category: General
priority: Medium
starred: None
created: 2025-12-10T11:35:25.818792
updated: 2025-12-10T11:35:37.898496
dg-publish: true
---
# Ls files starting with fish

**Priority:** Medium

## Conversation

### Assistant

Use filename-globbing. To list files whose names **start with “fish”**, run:

```bash
ls fish*
```

This matches:

- `fish`
- `fish.txt`
- `fish_data.csv`
- `fisherman.log` (also starts with “fish”)

If you want **only files** (not directories):

```bash
ls -p fish* | grep -v /
```

If your shell is **fish (the Fish shell)** itself and you want tab-completion style listing:

```fish
ls fish*
```

Fish uses the same globbing pattern.

For case-insensitive match:

```bash
ls -I fish*
```

or in fish shell:

```fish
ls (string match -ri "fish.*" *)
```

If you need a different filter (e.g., exact prefix, specific extension), specify and I’ll adjust the command.

---

