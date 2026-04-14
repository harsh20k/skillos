---
title: iOS Image Library App
category: Projects
priority: Medium
starred: None
created: 2025-05-19T02:37:26.340731
updated: 2025-05-19T02:40:20.579778
dg-publish: true
---
# iOS Image Library App

**Priority:** Medium

## Conversation

### Assistant

You can achieve this image library design in SwiftUI by combining a few key elements:

- A **scrollable grid** of images.
- A **top background image** that blurs as you scroll.
- A **full-screen image viewer** that appears on tap and dismisses on swipe down.

Here's a basic implementation of this concept using SwiftUI:

---

### ✅ **Step-by-step SwiftUI Code**

```swift
import SwiftUI

struct ImageLibraryView: View {
    let images = ["image1", "image2", "image3", "image4", "image5", "image6"] // Replace with your asset names
    
    @State private var selectedImage: String? = nil
    @State private var scrollOffset: CGFloat = 0

    var body: some View {
        ZStack {
            if let firstImage = images.first {
                GeometryReader { geo in
                    Image(firstImage)
                        .resizable()
                        .scaledToFill()
                        .frame(width: geo.size.width, height: 300)
                        .clipped()
                        .blur(radius: min(scrollOffset / 10, 20))
                        .overlay(Color.black.opacity(0.25))
                        .ignoresSafeArea()
                }
                .frame(height: 300)
            }
            
            ScrollView {
                GeometryReader { geo in
                    Color.clear
                        .preference(key: ScrollOffsetKey.self, value: geo.frame(in: .global).minY)
                }
                .frame(height: 0)
                
                LazyVGrid(columns: [GridItem(.adaptive(minimum: 100), spacing: 10)], spacing: 10) {
                    ForEach(images, id: \.self) { image in
                        Image(image)
                            .resizable()
                            .scaledToFill()
                            .frame(height: 100)
                            .clipped()
                            .cornerRadius(8)
                            .onTapGesture {
                                selectedImage = image
                            }
                    }
                }
                .padding()
            }
            .onPreferenceChange(ScrollOffsetKey.self) { value in
                scrollOffset = -value
            }
            
            if let selected = selectedImage {
                FullScreenImageView(imageName: selected) {
                    selectedImage = nil
                }
            }
        }
    }
}

struct FullScreenImageView: View {
    var imageName: String
    var onDismiss: () -> Void

    @GestureState private var dragOffset = CGSize.zero

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            Image(imageName)
                .resizable()
                .scaledToFit()
                .padding()
                .background(Color.black)
                .cornerRadius(10)
                .shadow(radius: 10)
                .offset(y: dragOffset.height)
                .gesture(
                    DragGesture()
                        .updating($dragOffset) { value, state, _ in
                            state = value.translation
                        }
                        .onEnded { value in
                            if value.translation.height > 100 {
                                onDismiss()
                            }
                        }
                )
        }
        .transition(.move(edge: .bottom))
        .animation(.spring(), value: dragOffset)
    }
}

// Scroll offset helper
struct ScrollOffsetKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = nextValue()
    }
}

// Preview
struct ImageLibraryView_Previews: PreviewProvider {
    static var previews: some View {
        ImageLibraryView()
    }
}
```

---

### 🧪 Replace with Your Images
Make sure you add your images to the **Assets** folder in Xcode and update the `images` array with the appropriate names.

---

### ✨ Features Covered:
- Grid of images with lazy loading.
- Top image as background that blurs when scrolling.
- Tap-to-expand full image with swipe down to dismiss.

Would you like help adding:
- Network images support (via `URL` and `AsyncImage`)?
- Zooming in the full-screen image view?
- Support for dark/light mode?

Let me know and I can expand this code.

---

