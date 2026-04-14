---
title: Python for MBA Beginners
category: General
priority: Medium
starred: None
created: 2025-02-25T08:12:52.404929
updated: 2025-02-25T09:16:47.416902
dg-publish: true
---
# Python for MBA Beginners

**Priority:** Medium

## Conversation

### Assistant

Sure! Below is an expanded version of the dataset with more products and a few `NaN` (null) values in the `Price`, `Quantity Sold`, and `Total Revenue` columns to simulate real-world data issues.

---

### **Expanded Dataset: `sales_data.csv`**
```csv
Product,Category,Price,Quantity Sold,Total Revenue
Laptop,Electronics,800,5,4000
Phone,Electronics,600,10,6000
Tablet,Electronics,300,7,2100
Headphones,Accessories,100,15,1500
Charger,Accessories,20,30,600
Chair,Furniture,150,8,1200
Desk,Furniture,300,5,1500
Monitor,Electronics,200,,  # Missing Quantity Sold
Mouse,Accessories,50,20,1000
Keyboard,Accessories,70,,  # Missing Quantity Sold
Printer,Electronics,,4,1600  # Missing Price
TV,Electronics,1000,2,  # Missing Total Revenue
Bookshelf,Furniture,250,6,1500
Sofa,Furniture,700,3,  # Missing Total Revenue
```

---

### **Step 1: Load the Dataset**
```python
import pandas as pd

# Read the dataset (assuming saved as 'sales_data.csv')
df = pd.read_csv("sales_data.csv")

# Display the first few rows
print(df.head())
```

---

### **Step 2: Identify and Handle Missing Values**
```python
# Check for missing values in each column
print(df.isnull().sum())

# Fill missing values in 'Price' and 'Quantity Sold' with the column mean
df["Price"].fillna(df["Price"].mean(), inplace=True)
df["Quantity Sold"].fillna(df["Quantity Sold"].mean(), inplace=True)

# Fill missing values in 'Total Revenue' with computed Price * Quantity Sold
df["Total Revenue"].fillna(df["Price"] * df["Quantity Sold"], inplace=True)

print(df)
```

---

### **Step 3: Data Analysis & Selection**
```python
# Get basic statistics
print(df.describe())

# Select all products in Electronics category
electronics = df[df["Category"] == "Electronics"]
print(electronics)

# Select products with price above 300
expensive_products = df[df["Price"] > 300]
print(expensive_products)
```

---

### **Step 4: Data Visualization**
```python
import matplotlib.pyplot as plt

# Bar chart for Quantity Sold per Product
df.plot(kind="bar", x="Product", y="Quantity Sold", title="Products vs Quantity Sold")
plt.show()

# Pie chart for total revenue distribution across categories
df.groupby("Category")["Total Revenue"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Revenue Distribution by Category")
plt.ylabel("")  # Hide y-label
plt.show()
```

---

### **Outcome:**
1. **Introduces real-world data issues** – Missing values in `Price`, `Quantity Sold`, and `Total Revenue`.
2. **Demonstrates handling missing values** – Filling them using mean and computed values.
3. **Covers essential data operations** – Selection, filtering, and visualization.

This should make your class more engaging for an MBA student. Would you like me to add any business-related insights? 😊

---

