---
title: Spacing Audit 8pt Grid
category: Projects
priority: Medium
starred: None
created: 2025-07-31T03:45:17.172533
updated: 2025-07-31T03:45:36.695198
dg-publish: true
---
# Spacing Audit 8pt Grid

**Priority:** Medium

## Conversation

### Assistant

Here’s a **spacing audit and standardization** for your app screen based on an **8-point grid system**. The 8pt system uses increments of 4 or 8 (like 4, 8, 16, 24, 32, 40...) to ensure visual rhythm and consistency across your UI.

---

## 🔍 Audit Observations

### 1. **Top Section: Header ("Rituals")**
- **Vertical spacing** above and below header text should follow an 8pt multiple.
- ✅ *Looks like it's close to 32–40pt top margin.*
- ❗**Suggestion:** Ensure the spacing from top to header = `40pt` and from header to “Pinned Rituals” = `24pt`.

---

### 2. **Pinned Rituals Section**
- **Section title "Pinned Rituals"**
  - Vertical margin: should be `24pt` from the title “Rituals”
- **Pinned Ritual cards**:
  - Card size and internal padding: Verify horizontal/vertical padding is `16pt` or `24pt`.
  - **Spacing between the two pinned ritual cards**: looks like non-standard (possibly 12pt).
    - ❗**Suggestion:** Make it **`16pt`** gap.
- **Play icon size/padding**:
  - Align it vertically and horizontally centered within a `48pt` square if it’s a tap target.
  - Spacing between icon and text: at least `8pt`.

---

### 3. **Main Grid Cards ("Fast", "Only love", etc.)**
- **Card size**: Maintain consistent **padding = 16pt** on all sides inside cards.
- **Spacing between cards** (both horizontal and vertical): 
  - Looks close to 12–14pt currently.
  - ❗**Fix**: Standardize to `16pt`.
- **Icon → Text spacing inside card**: Looks okay; confirm it follows `8pt` or `12pt`.
- **Bottom margin of section before bottom bar**: needs to be at least `24–32pt`.

---

### 4. **Bottom Tab Bar**
- Top margin above the tab bar from last row of routines: Ensure it's at least `32pt`.
- Each icon + label cluster:
  - Should be center-aligned.
  - Ensure equal padding (e.g., `16pt`) between icons.

---

## 🧮 Suggested Standard Measurements (8pt Grid)

| Component                          | Spacing / Size |
|-----------------------------------|----------------|
| Top safe area to title            | 40pt           |
| Title to section label            | 24pt           |
| Section title to card grid        | 24pt           |
| Card internal padding             | 16pt           |
| Card spacing (horizontal/vertical)| 16pt           |
| Icon to label inside cards        | 8pt–12pt       |
| Bottom padding above tab bar      | 32pt           |
| Tab icon spacing                  | 16pt           |
| Tap target size (icon buttons)    | Minimum 44pt   |

---

## ✅ Next Step Suggestions

1. **Spacing constants**: Extract reusable `spacing` tokens:
   ```swift
   enum Spacing {
       static let xSmall: CGFloat = 4
       static let small: CGFloat = 8
       static let medium: CGFloat = 16
       static let large: CGFloat = 24
       static let xLarge: CGFloat = 32
   }
   ```

2. **Grid guidelines**: Use an `invisible 8pt baseline grid` in Figma or Xcode Preview overlays to align all spacing and type.

3. **Auto-layout**: Make sure SwiftUI stacks (`VStack`, `LazyVGrid`) use `.spacing = 16` where appropriate.

---

Would you like me to generate a **corrected wireframe/mockup** using these spacing rules?

---

