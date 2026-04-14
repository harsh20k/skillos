---
title: ⭐⭐IOS Meditation Stack
category: Projects
priority: Medium
starred: None
created: 2025-07-05T09:10:15.398583
updated: 2025-08-08T01:27:06.087290
dg-publish: true
---
# ⭐⭐IOS Meditation Stack

**Priority:** Medium

## Conversation

### Assistant

Here’s the skinny on a **ship bar** and the vocab that orbits it—plus a ready-to-use bar for *your* app.

# What is a “ship bar”?
A **ship bar** (aka **quality bar**, **release bar**, or **exit criteria**) is the *line you must clear* before you submit a build. It’s a short, explicit checklist + thresholds so you don’t argue with yourself at 2 AM about “is this good enough?”.

# Why it matters (especially solo)
- Kills scope creep.
- Prevents “ship while broken” panic.
- Lets you pause without losing standards: if it doesn’t meet the bar, it waits.

# The pieces of a ship bar

## 1) Bug/priority thresholds (the “bug bar”)
- **P0 (blockers):** 0 known.
- **P1 (major):** ≤ N (e.g., ≤2), clearly documented workarounds.
- **P2/P3:** Any, if they don’t break core flows.

## 2) Functional exit criteria
Define the *green path(s)* your app must pass end-to-end, every time:
- Build → select ritual → play → bells fire on time (locked + background) → session saved → appears in history after relaunch.
- Routine Builder: create, reorder, set repeats, save; Preview renders correctly.
- Standalone Timer: choose ritual + swap opening/closing bells → play.

## 3) Quality thresholds
- **Crash-free sessions:** ≥ 99.5% in TestFlight (or zero crashes in 20+ runs).
- **Performance:** first launch < 2.5s on iPhone 12+, play tap → audio ≤ 250 ms.
- **Battery:** 30-min session < 4% drain on iPhone 12+ (screen off).
- **Audio reliability:** 0 missed bells in 10 consecutive sessions.

## 4) Release hygiene
- **Privacy answers** correct; **Privacy Policy URL** live.
- Background audio configured (AVAudioSession category, capabilities).
- App icons, screenshots, description, version notes done.
- Feature flags/kill-switch guarding any risky WIP.

## 5) Operational safety net
- **Rollback plan:** prepared hotfix branch; keep previous build ready.
- **Crash/analytics:** SDK integrated and verified (e.g., Sentry/Crashlytics + TelemetryDeck/Amplitude).
- **Support contact:** in-app link + FAQ.

# Related terms you’ll see

- **Quality gate / Exit criteria:** Synonyms for ship bar.
- **Bug bar:** Just the bug-threshold slice (e.g., “0 P0, ≤2 P1”).
- **Feature freeze:** Stop adding features; only bug fixes/polish.
- **Code freeze:** No code changes except P0 fixes.
- **Stabilization sprint / Regression window:** Time reserved to hunt and fix regressions only.
- **RC (Release Candidate):** Build you intend to ship if no P0/P1 show up.
- **Defect waiver:** Conscious decision to ship with a known issue (documented scope/impact).
- **Canary / Phased rollout:** Release to a small % first; increase if stable.
- **Kill switch / Remote flag:** Remotely hide/disable a feature post-ship.
- **Go/No-Go:** A final mini-meeting/checklist before submitting.

# A concrete ship bar for *your* MVP (paste this in your repo)

## Rituals v1.0 – Ship Bar
**Bugs**
- P0: **0**
- P1: **≤ 2** (workaround documented, not in core flow)
- P2/P3: Any

**Green paths**
- Create ritual with 3 blocks (with repeats) → Preview → Play → Bells (open/transition/close) → Complete → Session visible in History after relaunch.
- Standalone Timer: pick ritual, change opening/closing bells → Play → Complete.

**Audio**
- Background + locked screen bells fire 100% in 10/10 runs.
- No overlapping/double bells in any run.

**Perf & battery**
- Launch < 2.5s; Play→first bell latency ≤ 250 ms.
- 30-min session battery drain < 4% (screen off).

**Persistence**
- No duplicate rituals on save; edits persist across relaunch.
- Session log reconstructs accurate per-block times (±1s tolerance).

**UX polish**
- No dead-ends; Back always works.
- Pinned rituals visible & persistent; preview layout doesn’t clip at Large Text.

**Store readiness**
- App Privacy + Privacy Policy URL done.
- Screenshots (dark), subtitle/keywords finalized.
- Version number bumped; release notes drafted.

**Ops**
- Crash reporting + telemetry enabled and verified.
- Rollback plan: previous RC archived; hotfix checklist ready.

# Minimal test script (15 minutes)
1) Build → create “Morning Mix” (3 blocks, one with ×2) → save → preview → play.  
2) Lock screen; listen for opening + transitions; unlock mid-block; pause/resume; finish.  
3) Relaunch app → History shows session with correct duration/completion.  
4) Pin “Morning Mix”; confirm it appears in pinned section; unpin → disappears.  
5) Standalone Timer → choose different opening/closing bells → play; confirm.

# How to use this (solo-dev friendly)
- At the end of each day, do a **bug triage**: label everything P0–P3.
- When you think you’re “done,” open the ship-bar doc and tick each line. If any line fails, it’s **no-go**.
- Cut scope instead of bending the bar. That’s how you keep momentum *and* quality.

If you want, I can turn this into a one-page checklist you can drop into your repo or Notion.

---

