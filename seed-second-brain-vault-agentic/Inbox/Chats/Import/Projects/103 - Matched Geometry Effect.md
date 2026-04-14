---
title: Matched Geometry Effect
category: Projects
priority: Medium
starred: None
created: 2024-07-03T13:13:55.814542
updated: 2024-07-03T13:53:52.830409
dg-publish: true
---
# Matched Geometry Effect

**Priority:** Medium

## Conversation

### Assistant

Sure! Here’s the complete code with `ContentView` included:

```swift
import SwiftUI

@main
struct MatchedGeometryEffectApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

struct ContentView: View {
    var body: some View {
        MatchedGeometryEffectExample()
    }
}

struct MatchedGeometryEffectExample: View {
    @Namespace private var animation
    @State private var isExpanded = false
    
    var body: some View {
        VStack {
            if isExpanded {
                RoundedRectangle(cornerRadius: 25)
                    .fill(Color.blue)
                    .matchedGeometryEffect(id: "rectangle", in: animation)
                    .frame(width: 300, height: 200)
            } else {
                RoundedRectangle(cornerRadius: 25)
                    .fill(Color.blue)
                    .matchedGeometryEffect(id: "rectangle", in: animation)
                    .frame(width: 100, height: 100)
            }
            
            Button("Toggle") {
                withAnimation {
                    isExpanded.toggle()
                }
            }
        }
        .padding()
    }
}

struct MatchedGeometryEffectExample_Previews: PreviewProvider {
    static var previews: some View {
        MatchedGeometryEffectExample()
    }
}
```

### Explanation:

1. **`MatchedGeometryEffectApp`**: The entry point for the SwiftUI application.
2. **`ContentView`**: The main view that is displayed in the app's window. It includes the `MatchedGeometryEffectExample` view.
3. **`MatchedGeometryEffectExample`**: The view demonstrating the use of `matchedGeometryEffect`.
4. **Namespace**: A `@Namespace` property wrapper to create a unique namespace for the matched geometry effect.
5. **State**: The `@State` property wrapper to manage the state of the view (expanded or not).
6. **matchedGeometryEffect**: Applied to both instances of the `RoundedRectangle` to link their geometry.
7. **Animation**: The `withAnimation` block to animate the transition between states.
8. **Button**: A button to toggle the state.

When you run this code in a SwiftUI project, tapping the "Toggle" button will animate the transition between the two sizes of the rectangle.

---

