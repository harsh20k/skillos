---
title: What is SSH
category: General
priority: Medium
starred: None
created: 2025-12-20T19:23:07.642684
updated: 2025-12-20T19:23:17.537612
dg-publish: true
---
# What is SSH

**Priority:** Medium

## Conversation

### Assistant

**SSH (Secure Shell)** is a **secure network protocol** used to **log in to and control another computer over a network**, typically from a terminal.

image_group{"query":["SSH client server diagram","SSH authentication key exchange","SSH terminal remote login"]}

### What SSH is used for
- Securely log in to a remote server (VM, cloud instance, another computer)
- Run commands on a remote machine
- Transfer files securely (`scp`, `sftp`)
- Set up secure tunnels (port forwarding)
- Authenticate to services like GitHub using SSH keys

### Why SSH is important
- Encrypts all communication (prevents eavesdropping)
- Replaces insecure protocols like Telnet and FTP
- Uses strong cryptography and authentication

### How SSH works (simplified)
1. You run an SSH client on your machine
2. It connects to an SSH server on the remote machine (usually port 22)
3. Identity is verified using:
   - Password **or**
   - Cryptographic key pair (private key on your machine, public key on the server)
4. An encrypted session is established

### Example
```bash
ssh user@remote-server
```

### SSH keys (very common in development)
- **Private key**: stays on your machine (`~/.ssh/id_ed25519`)
- **Public key**: copied to the server (`~/.ssh/id_ed25519.pub`)
- No password needed after setup

### Common tools built on SSH
- `ssh` – remote login
- `scp` – secure copy
- `sftp` – secure file transfer
- Git over SSH (`git@github.com:repo.git`)

### In one line
SSH is **a secure, encrypted way to access and manage remote machines from the command line**.

---

