---
title: 🧪🧪🧪Learn TDD practically
category: General
priority: Medium
starred: None
created: 2025-10-29T09:12:24.489008
updated: 2025-10-29T17:19:59.006455
dg-publish: true
---
# 🧪🧪🧪Learn TDD practically

**Priority:** Medium

## Conversation

### Assistant

You can test the `isOverdue()` method by **controlling the date** so you can simulate tasks that are overdue and not overdue.

Right now your class uses:
```python
deadline = Date.today()
```
and compares it against `Date.today()` again, which always returns **False** (since both are the same day).  
Let’s make it testable.

---

### ✅ Step 1 — Fix implementation for testability
Use Python’s `datetime.date` and store `deadline` per instance:
```python
from datetime import date, timedelta

class Taskk:
    def __init__(self, deadline=None):
        self.assignedTo = None
        self.status = "new"
        self.deadline = deadline or date.today()

    def assignTo(self, team_member):
        self.assignedTo = team_member
        return self.assignedTo

    def updateStatus(self, status):
        self.status = status
        return self.status

    def isOverdue(self):
        return date.today() > self.deadline
```

---

### ✅ Step 2 — Write tests for both cases
`tests/test_helloWorld.py`
```python
from datetime import date, timedelta
from taskk import Taskk

def test_is_overdue_false():
    task = Taskk(deadline=date.today() + timedelta(days=2))
    assert task.isOverdue() is False

def test_is_overdue_true():
    task = Taskk(deadline=date.today() - timedelta(days=1))
    assert task.isOverdue() is True
```

---

### ✅ Step 3 — Run tests
```bash
pytest -v
```

Expected output:
```
test_helloWorld.py::test_is_overdue_false PASSED
test_helloWorld.py::test_is_overdue_true PASSED
```

---

Would you like me to show how to mock the date using `unittest.mock.patch` instead of passing a deadline manually (for stricter isolation)?

---

