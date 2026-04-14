---
title: Scale button on tap
category: General
priority: Medium
starred: None
created: 2025-07-18T23:39:07.682809
updated: 2025-07-18T23:39:15.898380
dg-publish: true
---
# Scale button on tap

**Priority:** Medium

## Conversation

### Assistant

To add a `.95` scale effect on tap/touch in SwiftUI, you can use the `.gesture` modifier with a `DragGesture` or more simply use the `.buttonStyle` modifier with a custom style that scales on press.

Here’s the cleanest and most reusable way using a **custom `ButtonStyle`**:

### ✅ Step 1: Define a ScalableButtonStyle

```swift
struct ScalableButtonStyle: ButtonStyle {
    var scaleAmount: CGFloat = 0.95

    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? scaleAmount : 1)
            .animation(.easeInOut(duration: 0.1), value: configuration.isPressed)
    }
}
```

### ✅ Step 2: Apply it to your button

Update your button like this:

```swift
Button(action: onPlay) {
    HStack(spacing: AppTheme.Spacing.small) {
        Image(systemName: "play.fill")
            .font(.system(size: 14, weight: .bold))
        Text(LocalizedStringKey("button.play"))
            .font(.system(size: 16, weight: .semibold, design: .rounded))
    }
    .foregroundColor(.white)
    .padding(.horizontal, AppTheme.Spacing.large)
    .padding(.vertical, AppTheme.Spacing.small)
    .background(
        Capsule()
            .fill(AppTheme.accentColor)
    )
}
.buttonStyle(ScalableButtonStyle(scaleAmount: 0.95))
```

This approach keeps your view clean and adds nice feedback on press.

Let me know if you want the scale effect to animate with a bounce or spring!

---

