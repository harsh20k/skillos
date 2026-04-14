---
title: Fix shape transition
category: Projects
priority: Medium
starred: None
created: 2025-07-24T10:41:04.346160
updated: 2025-07-24T11:55:48.400596
dg-publish: true
---
# Fix shape transition

**Priority:** Medium

## Conversation

### Assistant

Absolutely! Here's a clear explanation of the **flow and morphing logic** of the shapes in your `BeadsView.swift`:

---

## 🧭 Overview: What the View Represents
Your `BeadsView` shows a horizontal row of beads. Each bead represents a block in the current meditation routine.

Each bead can:
- Be a **circle** (default)
- Morph into a **capsule** (if it's the current block)
- Be **filled** (if completed or partially complete)
- Stay **empty** (if not yet started)

---

## 🔄 Shape Morphing Flow: Circle → Capsule

### 🔹 1. **Morph Trigger**
The morph is triggered by this condition in `BeadsView`:
```swift
isCurrentBlock(_ index: Int)
```
This checks if the bead index is the **current block** being executed *while* the routine is:
- selected (`isRoutineSelected`)
- and playing (`isPlaying`)

### 🔹 2. **Passing State to MorphingShape**
Each bead shape is created like this:
```swift
MorphingShape(
	isCurrentBlock: isCurrentBlock(index),
	fillColor: beadFillColor(for: index),
	capsuleWidth: capsuleWidth,
	beadSize: beadSize
)
```
This passes a `Bool` indicating if it is the *currently active block*.

### 🔹 3. **Internal State and Animation**
In `MorphingShape`:
```swift
@State private var morphProgress: Double = 0.0
```
This value is animated between:
- `0.0` → Circle
- `1.0` → Capsule

The transition happens here:
```swift
.onChange(of: isCurrentBlock) { _, newValue in
	withAnimation(.easeInOut(duration: 0.4)) {
		morphProgress = newValue ? 1.0 : 0.0
	}
}
```
If the bead **becomes the current block**, it animates to capsule by setting `morphProgress = 1.0`.

If it **stops being the current block**, it animates back to circle with `morphProgress = 0.0`.

### 🔹 4. **Shape Drawing**
In `MorphingPath`:
- If `morphProgress == 0.0` → draw a **perfect circle** with `addEllipse`
- If `morphProgress == 1.0` → draw a **capsule** with `addRoundedRect`
- In-between values create **interpolated shapes** — rounded rectangles that grow wider and less circular based on `morphProgress`.

---

## 📊 Visual Summary

| Condition                          | Shape         | Filled?          |
|-----------------------------------|---------------|------------------|
| Routine not selected              | Circle        | No               |
| Routine selected, not playing     | Circle        | No               |
| Routine playing, before block     | Circle        | No               |
| Routine playing, current block    | Morphing → Capsule | Partial or empty |
| Routine playing, past block       | Circle        | Fully filled     |

---

Would you like a visual diagram or animation sequence to represent this morphing? I can also help you add bounce/spring if you want the transition to feel more lively.

---

