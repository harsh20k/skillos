---
title: Preferred delegation explained
category: General
priority: Medium
starred: None
created: 2025-11-15T18:29:58.938414
updated: 2025-11-16T15:11:38.398287
dg-publish: true
---
# Preferred delegation explained

**Priority:** Medium

## Conversation

### Assistant

Here is an updated version without using the word *challenge*:

**How a passkey works (very short points):**

- User’s device creates a **public key + private key pair**.  
- **Private key stays safely on the device** (Secure Enclave / TPM).  
- **Public key is sent to the server** and stored.  
- During login, the server sends a **random message** for the device to prove its identity.  
- The device uses the **private key** to sign that message (with Touch ID / biometrics).  
- The server checks the signature using the **public key**.  
- If it matches, authentication succeeds — **no password needed**.

---

