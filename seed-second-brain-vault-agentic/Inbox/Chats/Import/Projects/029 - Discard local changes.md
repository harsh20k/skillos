---
title: Discard local changes
category: Projects
priority: Medium
starred: None
created: 2025-11-22T08:14:27.908135
updated: 2025-11-22T18:40:44.041486
dg-publish: true
---
# Discard local changes

**Priority:** Medium

## Conversation

### Assistant

Use **pytest-cov**.

## 1. Install coverage plugin (if not already)
```
pip install pytest-cov
```

## 2. Run pytest with coverage
To get a coverage report for your Flask app:

```
pytest flask_app/tests/ --cov=flask_app --cov-report=term-missing
```

### Meaning:
- `--cov=flask_app` → measure coverage for the `flask_app` package  
- `--cov-report=term-missing` → shows which lines are not covered

You will see output like:

```
Name                           Stmts   Miss  Cover   Missing
----------------------------------------------------------------
flask_app/app.py                 120     10    92%   45-50
flask_app/routes/shop.py          80     5    94%   33-35
...
```

---

## 3. If you want an HTML report
```
pytest flask_app/tests/ --cov=flask_app --cov-report=html
```

This generates a folder `htmlcov/` with a clickable coverage report.

Open:
```
open htmlcov/index.html
```

---

If you want, I can help you set minimum required coverage or integrate this into GitLab CI.

---

