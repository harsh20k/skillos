---
title: ★★DEEP Technical Timers 
category: Technical
priority: Medium
starred: None
created: 2025-07-18T12:41:38.499414
updated: 2025-07-21T12:44:17.982417
dg-publish: true
---
# ★★DEEP Technical Timers 

**Priority:** Medium

## Conversation

### Assistant

All of your bell-times in this prototype are **absolute offsets** from the moment the session “anchor” was taken—not “play this next when the previous file finishes.” Concretely:

1. **Anchor Sample-Time**  
   When you called  
   ```swift
   if let pt = playerNode.playerTime(forNodeTime: nodeTime) {
     anchorSampleTime = pt.sampleTime
   }
   ```  
   you captured a clock tick—let’s call that **T₀**.

2. **Absolute Offsets**  
   Every time you do  
   ```swift
   schedule(sound: name, at: offsetSeconds)
   ```  
   under the hood you compute  
   ```
   fireSampleTime = T₀ + offsetSeconds × sampleRate
   ```  
   and tell the engine “start playing this file exactly when its internal sample counter hits `fireSampleTime`.”

3. **What that means for your 15 s bell**  
   - You scheduled the **first** bell at offset 0 s → it starts at T₀.  
   - That bell is 15 s long, so it finishes at **T₀ + 15 s**.  
   - You scheduled the **second** bell at offset 60 s → it will start at **T₀ + 60 s**, regardless of whether the first bell ended at 15 s or not.  

4. **Overlap vs. Chaining**  
   - If your second offset is **less** than 15 s (say you’d used offset 10 s), the engine would actually start playing the second file *while* the first is still sounding—it doesn’t wait for one to finish before beginning the next.  
   - If you want “play the next bell immediately after the previous one ends,” you’d either:  
     - Compute its offset as `(previousBellLength)`, or  
     - Use the player node’s `scheduleFile(_:at:completionHandler:)` and in that completion handler kick off the next bell with `at: nil` (i.e. “play as soon as possible”).

---

### In summary

- **Your offsets (0 s, 60 s, 120 s) are all measured from session start.**  
- The engine doesn’t chain them for you; it just starts each file at its designated absolute time.  
- To make a true “one after the other” sequence you either compute offsets dynamically based on file durations or use completion handlers to schedule each bell in turn.

---

