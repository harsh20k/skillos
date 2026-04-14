---
title: Python Mac Battery Percent
category: Projects
priority: Medium
starred: None
created: 2025-12-24T08:28:59.403011
updated: 2025-12-24T08:29:12.027096
dg-publish: true
---
# Python Mac Battery Percent

**Priority:** Medium

## Conversation

### Assistant

Yes. A Python program can read and print the battery percentage on macOS.

### Option 1: Using a macOS system command (simple, reliable)

macOS exposes battery info via `pmset`.

```python
import subprocess
import re

output = subprocess.check_output(["pmset", "-g", "batt"]).decode()
match = re.search(r"(\d+)%", output)

if match:
    print(f"Battery: {match.group(1)}%")
else:
    print("Battery info not found")
```

**How it works**
- `pmset -g batt` returns battery status
- Python parses the percentage from the output
- No extra libraries required

---

### Option 2: Using `psutil` (cross-platform, but less reliable on macOS)

```bash
pip install psutil
```

```python
import psutil

battery = psutil.sensors_battery()
if battery:
    print(f"Battery: {battery.percent}%")
else:
    print("Battery info not available")
```

**Note**
- On macOS, `psutil` may fail or return `None` on some machines
- Works better on Windows/Linux

---

### Option 3: Using IOKit via `ioreg` (most macOS-native)

```python
import subprocess
import re

cmd = ["ioreg", "-rc", "AppleSmartBattery"]
output = subprocess.check_output(cmd).decode()

current = re.search(r'"CurrentCapacity" = (\d+)', output)
maxcap = re.search(r'"MaxCapacity" = (\d+)', output)

if current and maxcap:
    percent = int(current.group(1)) / int(maxcap.group(1)) * 100
    print(f"Battery: {percent:.0f}%")
```

**Best for**
- macOS-specific tools
- Accurate readings

---

### Recommendation
- **Quick script / automation** → `pmset`
- **Cross-platform app** → `psutil`
- **macOS system utility** → `ioreg`

If you want:
- a menu-bar tool
- a background daemon
- SwiftUI + Python bridge
- or Live Activity / notification integration

say which use-case you’re targeting.

---

