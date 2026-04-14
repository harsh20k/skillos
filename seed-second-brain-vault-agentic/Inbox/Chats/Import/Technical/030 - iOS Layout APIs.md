---
title: iOS Layout APIs
category: Technical
priority: Medium
starred: None
created: 2025-03-12T10:52:52.344764
updated: 2025-03-12T10:55:39.688167
dg-publish: true
---
# iOS Layout APIs

**Priority:** Medium

## Conversation

### Assistant

### **What is `ViewThatFits` in SwiftUI?**
`ViewThatFits` is a SwiftUI container introduced in **iOS 16** that allows you to provide multiple views, and it will automatically choose the first one that fits within the available space.

This is useful when you want a responsive layout that adapts to different screen sizes without needing explicit condition checks.

---

### **Basic Example**
```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        ViewThatFits {
            Text("This is a long text that might not fit in small screens.")
                .font(.title)
                .padding()
            
            Text("Short Text") // Will be used if the first one doesn't fit.
                .font(.title)
                .padding()
        }
        .frame(width: 200) // Simulate limited space
        .border(Color.blue, width: 2)
    }
}
```
#### **Explanation:**
- `ViewThatFits` first tries to display `"This is a long text that might not fit in small screens."`
- If that text doesn't fit within the given width (`200` in this case), it falls back to the `"Short Text"` alternative.
- This makes it a great choice for adaptive layouts.

---

### **Example with Different Layouts**
```swift
import SwiftUI

struct ResponsiveView: View {
    var body: some View {
        ViewThatFits {
            HStack {
                Image(systemName: "star.fill")
                Text("Full Layout with Icon and Text")
            }
            .padding()
            
            Text("Compact Text Only") // Used if HStack doesn't fit
                .padding()
        }
        .frame(width: 150) // Simulating a constrained width
        .border(Color.red, width: 2)
    }
}
```
#### **How It Works:**
- The **HStack (icon + text)** will be displayed if it fits.
- If space is too tight, the fallback **text-only view** will be used.

---

### **Why Use `ViewThatFits`?**
✅ Automatically picks the best-fitting view.  
✅ No need for manual `if-else` conditions for different screen sizes.  
✅ Great for **dynamic text handling**, **adaptive UI**, and **responsive layouts**.

Would you like more advanced examples with animations or combined with `GeometryReader`? 🚀

---

