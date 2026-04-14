---
creation date: 2026-01-02 13:35
tags: 
description:
dg-publish: true
---
Here is a concise overview of what each service offers, with emphasis on what you can use for free today (roughly 2025–2026 era; always double‑check before betting a production system on it).

## Frontend hosting + fullstack platforms

### Vercel (vercel.com)

Vercel focuses on frontend and serverless fullstack (especially Next.js). The **Hobby** plan is free and intended for personal projects. [1][2]

Free highlights (Hobby):

- Deploy static sites and Next.js apps from Git repositories  
- Global CDN, preview deployments on PRs, automatic HTTPS [1][2]
- Serverless / edge functions with included but capped bandwidth and execution (limits are sufficient for small personal projects) [2]

### Netlify (netlify.com)

Netlify is for static and JAMstack sites with CI/CD, functions, and forms. The **Free / Starter** plan is genuinely free without a card. [3][4][5][6]

Free highlights:

- Unlimited static sites, Git-based CI/CD, global CDN [5][6]
- 100 GB bandwidth and 300 build minutes per month [4][5][6]
- 125k serverless function invocations and 1M edge function requests per month [4][5]
- Basic form handling and identity (auth) features [5][6]

### Render (render.com)

Render does frontend and backend (Node, Python, Docker, etc.) plus managed Postgres and Redis. It still has a meaningful free tier. [7][8][9]

Free highlights:

- Static sites free to host (with bandwidth and build limits) [10][7]
- Free instance types for web services and Postgres, with about 750 instance‑hours/month (enough for one always‑on small service) [10][7][8]
- 100 GB bandwidth and 500 build minutes per month on free tier directories like freetier.co [7]

### Railway (railway.app)

Railway is for “backend without infra”: deploy from Git, attach managed DBs. The old perpetual free tier is gone; now you mainly get trial credits. [11][12][13]

Free / trial highlights:

- One‑time $5 usage credit as a **Free** tier, valid ~30 days, no true always‑free plan [11][12]
- Includes enough to experiment with services (0.5 GB RAM, 0.5 GB volume) and databases during the trial [11]
- After credits are used or expired you must switch to a paid tier to keep apps running [11][14]

### Fly.io (fly.io)

Fly.io runs Dockerized apps close to users on a global network. It historically had a free tier; currently it is mostly usage‑based with small “effectively free” allowances and no standalone free plan for new users. [15][16][17][18]

Key points:

- Usage-based pricing with no fixed monthly fee; compute, storage, and bandwidth are metered [17][18]
- Docs still describe “free allowances” like up to 3 small VMs, 3 GB volumes, and 160 GB egress, but new accounts generally no longer get a classic free tier and must attach billing [16][17][19]

## Backend-as-a-service databases and auth

### Supabase (supabase.com)

Supabase is an open-source Firebase alternative: Postgres, auth, storage, edge functions. The **Free** plan is real and useful for hobby projects. [20][21][22]

Free highlights:

- Up to 2 active projects per organization [20][22]
- 500 MB Postgres database per project, 1 GB file storage [20][21][22]
- Around 2 GB database egress/month and small daily egress quotas [20][22]
- 10,000 MAUs on auth plus limited Edge Function invocations [20][22]

### Firebase (firebase.google.com)

Firebase is Google’s serverless backend suite: Firestore/RTDB, auth, hosting, functions, storage, analytics. The **Spark** plan is always‑free with quotas. [23][24][25][26]

Free highlights (Spark):

- Firestore: 1 GiB storage, 50k reads, 20k writes, 20k deletes per day, 10 GiB monthly egress [25]
- Realtime Database: about 1 GiB storage, 100 concurrent connections, 10 GB download/month [23]
- Hosting: 1 GiB storage and 10 GB data transfer/month with global CDN and SSL [23]
- Cloud Functions and Storage have multi‑million monthly free invocations/GB‑seconds and ~1 GiB storage / 10 GB download, suitable for small apps [23][24][26]
- Firebase Auth: up to ~50,000 MAUs free on the base tier [24][27]

### Clerk (clerk.dev)

Clerk is auth/identity (hosted user management, sessions, UI components). It has a generous MAU‑based free tier. [28][29][30][31]

Free highlights:

- First 10,000 monthly active users free on all plans [32][31]
- Typically includes core email/password, magic links, social logins, and prebuilt UI components for web frameworks [30]
- Beyond free MAUs, extra users and advanced features require a paid plan, with per‑MAU pricing [32][31]

## Edge runtimes and workers

### Cloudflare Workers (workers.cloudflare.com)

Cloudflare Workers is an edge compute platform that runs JS/Wasm at Cloudflare’s PoPs. There is a strong free tier. [33][34][35]

Free highlights:

- 100,000 requests per day across all Workers [33][34][35]
- Up to 100 worker scripts and a free workers.dev subdomain [33][34]
- ~10 ms CPU time per request and limited KV storage; egress bandwidth is not separately metered on Workers plans [33][34][35]

---
