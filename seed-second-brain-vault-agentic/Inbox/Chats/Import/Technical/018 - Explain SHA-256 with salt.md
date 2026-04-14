---
title: Explain SHA-256 with salt
category: Technical
priority: Medium
starred: None
created: 2025-10-30T09:50:07.679609
updated: 2025-10-30T10:24:29.943110
dg-publish: true
---
# Explain SHA-256 with salt

**Priority:** Medium

## Conversation

### Assistant

**SHA-256** is a *fast hash function*.  
**bcrypt**, **scrypt**, and **Argon2** are *password-hashing algorithms*.  

### 1. Core difference
| Aspect | SHA-256 | bcrypt / scrypt / Argon2 |
|--------|----------|---------------------------|
| Purpose | General cryptographic hash | Password hashing (key derivation) |
| Speed | Very fast → bad for passwords | Intentionally slow |
| Salt | Must be added manually | Built-in |
| Iterations | 1 (fixed) | Configurable cost parameter |
| Attack resistance | Weak against brute force | Strong; tunable work factor |
| Memory use | Low | High (esp. scrypt, Argon2) |

### 2. bcrypt
- Based on the Blowfish cipher.  
- Adjustable “cost” (2ⁿ rounds) slows attackers.  
- Handles its own salt.  
- Output includes salt and cost in one string.  

### 3. scrypt
- Adds **memory hardness**: requires significant RAM per hash.  
- Makes GPU/ASIC cracking inefficient.  
- Still adjustable for CPU and memory cost.  

### 4. Argon2
- Modern successor (Password Hashing Competition winner, 2015).  
- Three variants:  
  - **Argon2d:** GPU-resistant.  
  - **Argon2i:** side-channel resistant.  
  - **Argon2id:** hybrid, recommended.  
- Fully tunable for time, memory, and parallelism.  

**Summary:**  
SHA-256 = fast integrity hash.  
bcrypt/scrypt/Argon2 = purpose-built, slow, salted, tunable password hashing → far safer for authentication.

---

