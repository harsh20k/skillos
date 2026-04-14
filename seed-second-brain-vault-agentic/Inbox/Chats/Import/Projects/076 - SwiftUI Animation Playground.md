---
title: SwiftUI Animation Playground
category: Projects
priority: Medium
starred: None
created: 2025-07-15T08:59:38.695797
updated: 2025-07-15T13:00:33.507317
dg-publish: true
---
# SwiftUI Animation Playground

**Priority:** Medium

## Conversation

### Assistant

I’ve over-hauled the playground so it now mirrors every nuance in your bullet list:

* fills the 5 small circles **top→bottom** while a block runs  
* launches one outline circle that springs up and **un-fills the small circles bottom→top** as it passes  
* re-centres both the bottom stack (after a circle leaves) and the top stack (after a circle arrives) with the same snappy spring  
* hides the middle row entirely once the last circle finishes its journey

Open **MeditationAnimationView.swift** in the side panel (or drag into Xcode) and hit the preview. Tweak the counts, timings, or spring constants at the top until it feels just right. Ping me if you’d like extra polish—e.g. easing curves, colours, or accessibility sizing!

---

