---
title: Create SwiftUI view
category: Projects
priority: Medium
starred: None
created: 2025-07-29T02:53:39.854908
updated: 2025-07-29T06:31:33.941075
dg-publish: true
---
# Create SwiftUI view

**Priority:** Medium

## Conversation

### Assistant

Using a pre-rendered image for that pill background will certainly cut down on real-time drawing work—your SwiftUI view then just has to blit one bitmap instead of compositing gradients, shadows, and overlays every frame. But you’ll trade off:  

| | SwiftUI Shape Approach | Image Asset Approach |
|---|---|---|
| **Flexibility** | Fully dynamic: can change colors, sizes, blurs, shadows, even animate them at runtime or adapt to dark mode. | Fixed at the size, color, lighting and corner-radius baked into the PNG/PDF. You need separate assets for each variant (e.g. dark/light, different widths/heights). |
| **Scalability** | Resolution-independent vector drawing ensures perfect crispness at any device scale. | Bitmaps can blur or pixelate if stretched; you’ll need @1x/@2x/@3x (or a single PDF vector asset) to cover all device scales. |
| **Performance** | Modern iOS hardware and Apple’s Metal-backed SwiftUI renderer will GPU-accelerate gradients and shadows. Unless you have dozens of these on screen or you’re animating them constantly, you’re unlikely to notice any CPU/GPU cost. You can also apply `.drawingGroup()` or `.compositingGroup()` to rasterize complex shapes once and cache them. | One simple draw call to put the image on screen—minimal work. Good if you absolutely must minimize draw complexity (e.g. in a heavy, scroll-janky list). |
| **Maintenance** | All in code—no extra asset files to version-control. Tweaks are just parameter changes. | You must generate, name, and manage image assets for every size/color variant you need. Designers must re-export if you tweak the look. |

---

### When to reach for an image:
- You’re populating a **long list** of these pills (e.g. hundreds in a `LazyVStack`) and profiling shows that the real-time shadows/overlays are causing stutter.
- You absolutely need pixel-perfect consistency with a designer-supplied mockup, and you’re not planning any runtime color/theme changes.
- You’ve already baked a high-quality PNG/PDF in your asset catalog and you don’t mind the extra maintenance.

### When to stay in SwiftUI:
- You want your pill to **adapt** at runtime (e.g. change hue when selected, animate brightness on press, switch to dark mode).
- You only have a handful on screen, or you’re not seeing any performance issues in Instruments.
- You prefer the **single source of truth** in code rather than juggling multiple image variants.

---

#### A third option: Vector PDF asset
If you do need an “asset” but still want resolution independence, you can export your pill as a single-page **PDF** from Sketch/Figma, add it to your asset catalog, and then:

```swift
Image("BreathworkPill")
   .resizable(capInsets: EdgeInsets(top: 20, leading: 60, bottom: 20, trailing: 60), resizingMode: .stretch)
   .frame(height: 60)
```

- This gives you one file, scales perfectly, and still GPUs it as a single bitmap draw call.

---

**Bottom line:** unless profiling tells you this one view is your rendering bottleneck, stick with the SwiftUI version for flexibility and maintainability. If you do hit a performance wall, switch to a static image (or vector PDF) and measure again.

---

