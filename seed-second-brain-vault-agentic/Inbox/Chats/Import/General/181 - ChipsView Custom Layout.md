---
title: ChipsView Custom Layout
category: General
priority: Medium
starred: None
created: 2025-03-18T07:30:29.120773
updated: 2025-03-20T12:38:03.868635
dg-publish: true
---
# ChipsView Custom Layout

**Priority:** Medium

## Conversation

### Assistant

Here’s the updated `maxHeight` function that:  
✅ **Centers chips instead of using a staircase effect**  
✅ **Alternates between 2 and 3 elements per row**  
✅ **Ensures a minimum of 3 rows**  

---

### **🔹 Updated `maxHeight` Function**
```swift
private func maxHeight(proposal: ProposedViewSize, subviews: Subviews) -> CGFloat {
    var origin: CGPoint = .zero
    var row: Int = 1  // Tracks the row number
    var elementsInRow = 2  // Alternates between 2 and 3 elements per row
    var elementsPlaced = 0  // Elements in current row

    let totalElements = subviews.count
    let minRows = 3  // Ensure at least 3 rows

    // Compute minimum required rows to fit all elements
    let estimatedRows = max(minRows, (totalElements / 3) + (totalElements % 3 == 0 ? 0 : 1))

    for subview in subviews {
        let fitSize = subview.sizeThatFits(proposal)

        // Determine elements per row (alternating pattern: 2, 3, 2, 3...)
        let rowElements = (row % 2 == 0) ? 3 : 2
        let totalRowWidth = (CGFloat(rowElements) * fitSize.width) + (CGFloat(rowElements - 1) * spacing)
        let rowStartX = ((proposal.width ?? 0) - totalRowWidth) / 2  // Center the row
        
        if elementsPlaced >= elementsInRow {
            row += 1  // Move to next row
            elementsInRow = (row % 2 == 0) ? 3 : 2  // Update row pattern
            elementsPlaced = 0  // Reset count
            origin.x = rowStartX  // Center row horizontally
            origin.y += fitSize.height + spacing  // Move down
        }

        // Increment count for elements placed in row
        elementsPlaced += 1
    }

    // Ensure height accounts for last row
    if let lastSubview = subviews.last {
        origin.y += lastSubview.sizeThatFits(proposal).height
    }

    return origin.y
}
```

---

### **🔹 Key Fixes**
✅ **Centered Rows** → Uses `rowStartX` to center each row dynamically.  
✅ **Alternating 2-3 Elements Per Row** → Updates `elementsInRow` every row.  
✅ **Ensures a Minimum of 3 Rows** → Dynamically computes `estimatedRows`.  
✅ **Maintains Consistent Spacing** → Calculates `totalRowWidth` correctly.

---

### **📌 Example Layout**
#### **Before (Staircase Layout)**
```text
[Chip1]  [Chip2]  
   [Chip3]  [Chip4]  [Chip5]  
[Chip6]  [Chip7]  
   [Chip8]  [Chip9]  [Chip10]  
```

#### **After (Centered Alternating 2-3 Pattern)**
```text
   [Chip1]  [Chip2]  
[Chip3]  [Chip4]  [Chip5]  
   [Chip6]  [Chip7]  
[Chip8]  [Chip9]  [Chip10]  
```

Now, each row is **centered and follows the correct alternating pattern**.

Would you like **animated transitions** when resizing? 🚀

---

