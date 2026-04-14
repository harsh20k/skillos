---
title: SHA-256 with salt explained
category: Academic
priority: Medium
starred: None
created: 2025-10-30T09:49:40.649451
updated: 2025-10-30T09:49:50.401893
dg-publish: true
---
# SHA-256 with salt explained

**Priority:** Medium

## Conversation

### Assistant

SHA-256 is a **cryptographic hash function** that produces a 256-bit (32-byte) output from any input.  
Adding a **salt** means you prepend or append a **random value** to the input before hashing.  

Example:  
```
password = "mypassword"
salt = "7f3a92"
hash = SHA256(salt + password)
```

Purpose:  
- Makes identical passwords produce different hashes.  
- Protects against precomputed dictionary or rainbow table attacks.  

Summary:  
- **SHA-256** → hashing algorithm  
- **Salt** → random data added to input  
- **Result** → unique hash per user, even if passwords match

---

