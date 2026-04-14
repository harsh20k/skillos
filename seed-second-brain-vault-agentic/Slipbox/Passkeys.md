---
creation date: 2025-11-16 11:55
tags: [concept]
share_link: https://share.note.sx/280du8lj#19kPjJM3Vzc8eXj71EUd2GXQ4mSbW373PO1v2lVokFY
share_updated: 2025-11-16T11:55:39-04:00
dg-publish: true
---

## [[Passkeys (non technical)]]

## Registration Flow (Creating a Passkey)

```mermaid
sequenceDiagram
    participant User as 👤 User
    participant Browser as 🌐 Browser
    participant Server as 🖥️ Server (Relying Party)
    participant Auth as 🔐 Authenticator<br/>(Touch ID/Security Key)

    User->>Browser: Click "Register Passkey"
    Browser->>Server: POST /register/start<br/>{username: "harsh"}
    
    Note over Server: Generate random challenge<br/>(cryptographic nonce)
    Server->>Server: Store challenge in session
    Server->>Browser: PublicKeyCredentialCreationOptions<br/>{challenge, rp, user}
    
    Browser->>Auth: navigator.credentials.create()
    Note over Auth: Prompt user for<br/>biometric/PIN
    
    User->>Auth: Touch ID / Face ID / PIN
    
    Note over Auth: Generate new keypair:<br/>• Private key (stays on device)<br/>• Public key (sent to server)
    
    Auth->>Auth: Sign challenge with private key
    Auth->>Browser: Credential Response<br/>{publicKey, attestation, signature}
    
    Browser->>Server: POST /register/finish<br/>{credential, signature}
    
    Note over Server: Verify signature matches challenge<br/>Store public key + credential ID
    Server->>Server: Link public key to user account
    Server->>Browser: ✅ Registration Success
    Browser->>User: "Passkey registered!"
```

## Authentication Flow (Logging in with Passkey)

```mermaid
sequenceDiagram
    participant User as 👤 User
    participant Browser as 🌐 Browser
    participant Server as 🖥️ Server (Relying Party)
    participant Auth as 🔐 Authenticator<br/>(Touch ID/Security Key)

    User->>Browser: Click "Login with Passkey"
    Browser->>Server: POST /login/start<br/>{username: "harsh"}
    
    Note over Server: Generate new challenge<br/>Look up user's credentials
    Server->>Server: Store challenge in session
    Server->>Browser: PublicKeyCredentialRequestOptions<br/>{challenge, allowCredentials}
    
    Browser->>Auth: navigator.credentials.get()
    Note over Auth: Find matching credential<br/>Prompt user for verification
    
    User->>Auth: Touch ID / Face ID / PIN
    
    Note over Auth: Sign challenge with<br/>stored private key
    Auth->>Browser: Authentication Response<br/>{credentialId, signature}
    
    Browser->>Server: POST /login/finish<br/>{credential, signature}
    
    Note over Server: Verify signature using<br/>stored public key
    Server->>Server: Signature valid? ✓<br/>User authenticated!
    Server->>Browser: ✅ Login Success
    Browser->>User: "Logged in successfully!"
```

## Cryptographic Key Relationship

```mermaid
graph TB
    subgraph "🔐 Device (User's Phone/Computer)"
        PK[Private Key 🔑<br/>Never leaves device]
        Auth[Authenticator<br/>Touch ID / Face ID]
        PK -.Securely stored.-> Auth
    end
    
    subgraph "🖥️ Server (Website)"
        PublicKey[Public Key 🔓<br/>Stored in database]
        UserDB[(User Database)]
        PublicKey --> UserDB
    end
    
    Challenge[Challenge<br/>Random string]
    
    Challenge -->|Sign with| PK
    PK -->|Creates| Signature[Digital Signature ✍️]
    Signature -->|Verify with| PublicKey
    PublicKey -->|Valid? ✓| Success[Authentication Success ✅]
    
    style PK fill:#ff6b6b
    style PublicKey fill:#51cf66
    style Signature fill:#ffd43b
    style Success fill:#51cf66
```

## High-Level Architecture

```mermaid
graph LR
    subgraph "Client Side"
        A[Web Browser] --> B[WebAuthn API]
        B --> C[Authenticator<br/>Touch ID / YubiKey]
    end
    
    subgraph "Server Side"
        D[Flask App] --> E[WebAuthn Service]
        E --> F[Credentials DB]
    end
    
    A <-->|HTTPS| D
    
    style A fill:#4dabf7
    style C fill:#ff6b6b
    style D fill:#51cf66
    style F fill:#ffd43b
```

## Key Concepts

**Public-Private Key Pair** - During registration, the authenticator generates two mathematically linked keys [3][4][5]:
- **Private Key**: Stays on your device (never transmitted)
- **Public Key**: Stored on the server

**Challenge-Response** - The server sends a random challenge that must be signed with the private key and verified with the public key [1][6][7].

**Phishing Resistant** - Credentials are bound to the origin (domain), so they won't work on fake sites [3][5].

**No Passwords** - Your biometric data never leaves your device; only cryptographic signatures are sent [2][4][5].

This is exactly what your Flask app implements! [1][2][3]

Sources
[1] WebAuthn: How it Works & Example Flows https://www.descope.com/learn/post/webauthn
[2] What Is WebAuthn and How Does It Work? https://fusionauth.io/articles/authentication/webauthn
[3] WebAuthn Explained https://supertokens.com/blog/webauthn-explained
[4] What are passkeys and how do they work? - Clerk https://clerk.com/blog/what-are-passkeys
[5] What Is a Passkey & How Does It Work? - Descope https://www.descope.com/learn/post/passkeys
[6] Passkeys Cheat Sheet for Developers https://www.corbado.com/blog/passkeys-cheat-sheet
[7] Authentication - How it Works https://webauthn.wtf/how-it-works/authentication
[8] High level architecture of a passkey application https://developers.yubico.com/Passkeys/High_level_architecture_of_a_passkey_application.html
[9] An API for accessing Public Key Credentials - Level 3 https://www.w3.org/TR/webauthn-3/
[10] Enable Web Authentication API (WebAuthn) passkeys https://learn.microsoft.com/en-us/aspnet/core/security/authentication/passkeys/?view=aspnetcore-10.0


