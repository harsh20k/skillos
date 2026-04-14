---
title: Circular Window Shape SwiftUI
category: Projects
priority: Medium
starred: None
created: 2024-06-29T16:15:26.338494
updated: 2024-06-30T00:07:13.139754
dg-publish: true
---
# Circular Window Shape SwiftUI

**Priority:** Medium

## Conversation

### Assistant

Certainly! This SwiftUI code defines a macOS application with a custom-shaped window. Let's break it down step by step:

### Main Application Structure

```swift
@main
struct CustomShapedWindowTestApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .frame(width: 400, height: 400)
                .background(WindowAccessor { window in
                    if let window = window {
                        window.title = "Circular Window"
                        window.isOpaque = false
                        window.backgroundColor = .clear
                        window.standardWindowButton(.closeButton)?.isHidden = true
                        window.standardWindowButton(.miniaturizeButton)?.isHidden = true
                        window.standardWindowButton(.zoomButton)?.isHidden = true
                        window.styleMask.remove(.titled)
                        window.styleMask.insert(.fullSizeContentView)
                    }
                })
        }
    }
}
```

### Explanation:

1. **@main**: This attribute marks the entry point of the application.
   
2. **CustomShapedWindowTestApp**: This struct conforms to the `App` protocol, which is the main structure of the application.
   
3. **body**: The body property defines the content of the app. It uses a `WindowGroup` to manage the main window.
   
4. **WindowGroup**: This scene type manages a group of windows for the app. In this case, it contains one window with a `ContentView`.

5. **ContentView**:
   - The `ContentView` is the main view of the application.
   - The `.frame(width: 400, height: 400)` modifier sets the size of the content view.
   - The `.background(WindowAccessor { window in ... })` modifier adds a background that uses the `WindowAccessor` to customize the window's properties.

### Window Customization

```swift
struct WindowAccessor: NSViewRepresentable {
    var callback: (NSWindow?) -> Void

    func makeNSView(context: Context) -> NSView {
        return NSView()
    }

    func updateNSView(_ nsView: NSView, context: Context) {
        DispatchQueue.main.async {
            self.callback(nsView.window)
        }
    }
}
```

### Explanation:

1. **WindowAccessor**: This struct conforms to the `NSViewRepresentable` protocol, allowing it to interface with AppKit (the underlying framework for macOS UI).

2. **callback**: A closure that takes an optional `NSWindow` and performs custom actions on it.

3. **makeNSView(context: Context) -> NSView**:
   - This method creates an `NSView` instance. It's part of the `NSViewRepresentable` protocol and is required to bridge SwiftUI with AppKit.
   - It returns a simple `NSView` instance, which doesn't display anything itself but gives access to the window.

4. **updateNSView(_ nsView: NSView, context: Context)**:
   - This method is called whenever the SwiftUI view hierarchy needs to update the `NSView`.
   - It uses `DispatchQueue.main.async` to ensure the `callback` is executed on the main thread, where UI updates must occur.
   - The `callback` is provided with the window (`nsView.window`) to perform the customizations.

### Customizations in the Callback

```swift
window.title = "Circular Window"
window.isOpaque = false
window.backgroundColor = .clear
window.standardWindowButton(.closeButton)?.isHidden = true
window.standardWindowButton(.miniaturizeButton)?.isHidden = true
window.standardWindowButton(.zoomButton)?.isHidden = true
window.styleMask.remove(.titled)
window.styleMask.insert(.fullSizeContentView)
```

1. **window.title**: Sets the window title to "Circular Window".

2. **window.isOpaque = false**: Makes the window non-opaque, allowing transparency.

3. **window.backgroundColor = .clear**: Sets the background color of the window to clear, making it transparent.

4. **window.standardWindowButton(...).isHidden = true**: Hides the standard window buttons (close, miniaturize, zoom).

5. **window.styleMask.remove(.titled)**: Removes the titled style mask, which typically provides the title bar.

6. **window.styleMask.insert(.fullSizeContentView)**: Inserts the full-size content view style mask, allowing the content view to occupy the entire window area.

### Summary

This code defines a macOS application with a custom-shaped, transparent window that hides standard window controls and title bar. The `WindowAccessor` struct facilitates customizing the window by interfacing with the underlying AppKit framework. The main application struct (`CustomShapedWindowTestApp`) sets up the main content view and applies the window customizations.

---

