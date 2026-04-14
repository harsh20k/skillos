---
title: Echo command explanation
category: General
priority: Medium
starred: None
created: 2025-12-20T09:16:03.752569
updated: 2025-12-20T09:16:13.805904
dg-publish: true
---
# Echo command explanation

**Priority:** Medium

## Conversation

### Assistant

The **`echo` command** is a basic shell command used to **print text or variable values to standard output (the terminal)**.

---

## Core purpose
- Display a message
- Print the value of variables
- Send text into files or other commands

---

## Basic syntax
```bash
echo [options] [string]
```

---

## Common examples

### 1. Print plain text
```bash
echo "Hello world"
```
Output:
```
Hello world
```

---

### 2. Print a variable value
```bash
name="Harsh"
echo $name
```
Output:
```
Harsh
```

---

### 3. Print multiple words
```bash
echo This is a test
```

---

### 4. Redirect output to a file
Overwrite file:
```bash
echo "Line 1" > file.txt
```

Append to file:
```bash
echo "Line 2" >> file.txt
```

---

### 5. Use escape sequences (`-e`)
```bash
echo -e "Line1\nLine2\tTabbed"
```
- `\n` → new line  
- `\t` → tab  

---

### 6. Suppress newline (`-n`)
```bash
echo -n "Loading..."
```
Output stays on the same line.

---

## Practical uses
- Debugging shell scripts
- Printing command progress or status
- Generating config files or simple scripts
- Piping text into other commands

Example:
```bash
echo "error" | grep "err"
```

---

## Important notes
- `echo` behavior can vary slightly between shells (`bash`, `zsh`, `sh`)
- For precise output (especially in scripts), `printf` is sometimes preferred

If you want, I can explain **`echo` vs `printf`**, or show **real examples from bash scripts**.

---

