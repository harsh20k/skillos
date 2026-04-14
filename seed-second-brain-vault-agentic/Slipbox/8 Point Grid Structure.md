---
dg-publish: true
---

# 📐 What Is an “8-Point Grid” Structure?

The **8-point grid** is a design system convention where all dimensions—margins, padding, gaps, component sizes—are multiples of **8 pixels** (or points, in iOS). It brings consistency, rhythm, and visual harmony to your layouts.

---

## 🔍 Core Principles

1. **Uniform Spacing**  
   - Every horizontal and vertical gap (inside cards, between buttons, around text) is 8 pt, 16 pt, 24 pt, 32 pt, etc.

2. **Consistent Sizing**  
   - Component heights/widths snap to 8 pt increments (e.g. a button might be 48 × 120 pt, an icon container 32 × 32 pt).

3. **Aligned Layout**  
   - Elements sit on an invisible 8 pt grid—columns, rows, and gutters all align to that grid.

---

## 🎯 Why Use It?

- **[[Visual Rhythm]] & Clarity**  
  Repeating spacing units create a predictable, balanced feel.

- **Simplified Design & Handoff**  
  Designers and developers share one spacing scale—no guesswork about “Is this 12 pt or 14 pt?”

- **Responsive Foundations**  
  When scaling up for different screen sizes, you can multiply the base grid (e.g. 16 pt for small, 24 pt for medium, 32 pt for large) while staying coherent.

---

## 🚀 How to Apply

- **Layout Grids:**  
  - Define columns and gutters in multiples of 8 pt (e.g. 4-column grid with 16 pt gutters).  
- **Spacing Tokens:**  
  - Create design tokens (SPACING_1 = 8 pt, SPACING_2 = 16 pt, etc.) and reuse them everywhere.  
- **Component Dimensions:**  
  - Button heights: 40 pt → 48 pt → 56 pt (jump in 8 pt steps).
  - Icon containers: 24 pt → 32 pt → 40 pt.

---

## 📚 Example

| Token       | Value | Usage                       |
|-------------|-------|-----------------------------|
| `S1`        | 8 pt   | Small gap between icons     |
| `S2`        | 16 pt  | Padding inside cards        |
| `S3`        | 24 pt  | Vertical space between text |
| `S4`        | 32 pt  | Margin around screen edges  |

---

By anchoring your UI to this **8-point rhythm**, you ensure every element feels thoughtfully placed, and your app gains a polished, professional look—perfect for a calm, structured meditation experience.  

### Related Articles

[[UI Design]]
[[UX Design]]
[[Application Design]]
[[Visual Rhythm]]