---
tags:
  - concept
source: chatgpt
dg-publish: true
---
Yes—under the hood, almost every meditation‐timer app you’ve used is running its own internal clocking mechanism rather than trusting iOS notifications or system alarms to keep track of elapsed time. Here’s roughly how they do it:

1. **Software Timers for Elapsed-Time Tracking**
    
    - Most use either
        
        - **DispatchSourceTimer** (GCD timer) for high accuracy and low drift, or
            
        - **Timer** (Foundation.Timer) scheduled on the run-loop.
            
        
    - These timers fire at a regular interval—often once per second (or more frequently if you’re animating a smooth progress indicator)—and increment an internal counter of “seconds elapsed.”
        
    
2. **State Machine / Session Object**
    
    - There’s typically a small state object (e.g. a MeditationSession class) that knows:
        
        - The total length of each interval block.
            
        - How many seconds have elapsed in the current block.
            
        - Whether you’re paused, running, or finished.
            
        
    - When the timer callback runs, it updates that state, drives the UI (progress bars, labels), and decides when to fire the next bell.
        
    
3. **Bell Scheduling vs. Bulk Scheduling**
    
    - As we discussed, while you _can_ bulk-schedule all bells up front via AVAudioEngine, many apps instead schedule only the _next_ bell. In your timer callback, when elapsed == blockLength, you:
        
        1. Play your bell sound immediately (or with a tiny look-ahead).
            
        2. Reset elapsed = 0 and move to the next block.
            
        3. Continue the timer running in the background.
            
        
    - This keeps your scheduling window small, reduces drift, and recovers gracefully if the app is suspended and resumed.
        
    
4. **Background Modes & Audio Session**
    
    - To keep timers firing when the screen locks, they usually:
        
        - Declare the **“audio”** background mode in Info.plist,
            
        - Configure their AVAudioSession for playback, and
            
        - Keep a silent or looping audio track running (so the engine—and thus its GCD timers—stay active).
            
        
    
5. **Live Activities / Widgets (iOS 16+)**
    
    - Newer apps may also publish a Live Activity via ActivityKit. Under the hood, though, the app’s own timer is what feeds the Live Activity’s remaining‐time display.
        
    

---

### **In Practice**

- **User opens** the app and hits “Start.”
    
- You **create** a MeditationSession with your block durations.
    
- You **start** a DispatchSourceTimer that ticks every second (or more often).
    
- On each tick you:
    
    1. Increment your session’s elapsedTime.
        
    2. Update UI (progress ring, label).
        
    3. If elapsedTime reaches the block’s length → play bell, reset elapsedTime, advance block index.
        
    
- **When backgrounded**, your audio session keeps the engine (and therefore your timer) alive so those ticks still fire.
    

  

That’s essentially it—rather than scheduling _all_ bells minutes in advance, most meditation apps maintain their own elapsed-time clock and trigger each bell just in time. This design is robust, easy to debug, and handles background suspension gracefully.



## Popular Approaches

Here’s a quick overview of what you’ll find across popular timer-based apps (meditation, Pomodoro, alarms, etc.) in how they manage sessions under the hood:

  

Most use **in-process software timers** (rather than relying on notifications or system alarms alone), keep their audio engine alive via background-audio modes, and dynamically schedule only the _next_ alert rather than bulk-queuing long sequences. On Android, they fall back on **AlarmManager** or the newer **WorkManager** for longevity across reboots, while iOS apps leverage **DispatchSourceTimer** (or Timer) and an AVAudioSession in playback mode to survive backgrounding.

---

## **iOS Timer Patterns**
### **Timer Types: Timer vs DispatchSourceTimer vs asyncAfter**

Swift offers several ways to schedule delayed or repeating work.

- **Timer** (formerly NSTimer) lives on a run loop and is easy for UI-driven callbacks, but requires an active run loop.
    
- **DispatchSourceTimer** is a GCD‐based timer that doesn’t need a run loop and lets you specify a deadline, repeat interval, and leeway for energy‐efficient firing .
    
- **asyncAfter** on DispatchQueue is a one-shot delay; repeating via recursion can drift over time .
    
    For long-running timers (minutes or hours), most apps prefer DispatchSourceTimer for its flexibility and lower drift .

### **Background Audio to Keep Timers Alive**

To prevent iOS from suspending your app—and thus stopping your timers—apps typically:

1. Set their **AVAudioSession** category to .playback.
    
2. Add the “audio” mode to **UIBackgroundModes** in **Info.plist**.
    
    This ensures the audio engine (and any GCD timers tied to it) keep running even when the screen locks .
    

  

### **Dynamic Scheduling of “Next” Alerts**

Rather than scheduling dozens of future bells in one go (which can silently fail if the system clock or session changes), leading apps schedule only the _next_ bell when the previous one fires.

- For example, a Pomodoro‐style timer sets a DispatchSourceTimer for the next interval, then in its event handler schedules the subsequent one .
    
- This “chain the next event” pattern keeps look-ahead windows small, minimizes drift, and recovers gracefully if your app is briefly suspended.
    

---

## **Architectural Insights from Leading Meditation Apps**

- A [Stormotion guide](https://stormotion.io/blog/how-to-make-a-meditation-app-like-headspace/) underscores that Calm, Headspace, etc., layer a simple timer engine under a minimal UI, ensuring session state is tracked locally and bells play only when intended .
    
- Clones of Insight Timer emphasize using an internal **session state object** to track elapsed time, block lengths, and bell schedules, rather than trusting system notifications to survive all edge cases .    

---
## **Cross-Platform Best Practices**

1. **Maintain an internal clock/state machine** (seconds elapsed, current block, paused/running) updated via a reliable software timer.
    
2. **Trigger each bell “just in time”**—schedule the next alert only seconds ahead—so you avoid silent failures from system suspensions or audio‐session changes.
    
3. **Use native background modes**:
    
    - iOS → AVAudioSession playback + DispatchSourceTimer or Timer on a background queue.
        
    - Android → AlarmManager for exact alarms or WorkManager for durable periodic work.

4. **Keep timing logic simple and local**, coupling it with minimalist UI updates, to maximize reliability and minimize power impact.
    

  

Following these patterns ensures meditation timers (or any long-interval timer-based app) remain accurate, robust in the background, and resilient across platform quirks.