---
title: Git repository setup
category: General
priority: Medium
starred: None
created: 2025-11-13T16:20:57.226450
updated: 2025-11-13T16:57:36.607696
dg-publish: true
---
# Git repository setup

**Priority:** Medium

## Conversation

### Assistant

Now you’re seeing **the opposite problem**:

- Your `PublicKeyCredentialCreationOptions` has **neither** `.model_dump()` **nor** `.to_dict()`.

This tells me your installed package is **NOT `webauthn`** but **`python-webauthn` (very old)** or another fork.

Let’s fix this cleanly.

---

# ✔ The simplest working approach  
Use the **correct modern library**:

```sh
pip install py-webauthn
```

Then change your imports.

---

# 1. Install the correct library

Inside your venv:

```sh
pip uninstall webauthn -y
pip uninstall python-webauthn -y
pip install py-webauthn
```

Now `PublicKeyCredentialCreationOptions` will have **`.model_dump()`**.

---

# 2. Update your imports

Replace your existing imports with:

```python
from webauthn.helpers import generate_registration_options, generate_authentication_options
from webauthn.helpers import verify_registration_response, verify_authentication_response
```

---

# 3. Now these lines will work:

```python
return jsonify(options.model_dump())
```

and

```python
return jsonify(options.model_dump())
```

---

# Why we do this
There are 3 similarly named but different projects on PyPI:

| Package name | State | Functions |
|--------------|--------|-----------|
| `webauthn` | Old, unmaintained | no `.model_dump()` |
| `python-webauthn` | very old | no `.to_dict()` |
| `py-webauthn` (correct) | actively maintained | uses Pydantic → `.model_dump()` |

Your environment currently has either of the **first two**, causing confusion.

---

# 4. Confirm version

Run:

```sh
pip show py-webauthn
```

You should see version **2.x or 3.x**.

---

# If you want, paste your full `app.py` and I will rewrite it 100% correct with the proper library.

---

