---
title: Technical Interview Questions Prep
category: Career
priority: Medium
starred: None
created: 2024-12-23T02:28:03.615317
updated: 2024-12-23T02:32:57.865641
dg-publish: true
---
# Technical Interview Questions Prep

**Priority:** Medium

## Conversation

### Assistant

Here’s a detailed answer for every question shared earlier:

---

### **1. SQL Questions**

**1.1**: **Retrieve the top 5 performing items based on sales**
```sql
SELECT item_name, SUM(sales_amount) AS total_sales
FROM sales_table
GROUP BY item_name
ORDER BY total_sales DESC
LIMIT 5;
```

---

**1.2**: **Difference between JOINs**
- **INNER JOIN**: Returns records with matching values in both tables.
- **LEFT JOIN**: Returns all records from the left table and matching records from the right table. Non-matching rows have `NULL` values.
- **FULL JOIN**: Returns all records when there’s a match in either table and fills non-matching rows with `NULL`.

---

**1.3**: **Identify and remove duplicates**
```sql
-- Identify duplicates
SELECT col1, col2, COUNT(*)
FROM table_name
GROUP BY col1, col2
HAVING COUNT(*) > 1;

-- Remove duplicates
WITH CTE AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY col1, col2 ORDER BY id) AS row_num
    FROM table_name
)
DELETE FROM CTE
WHERE row_num > 1;
```

---

**1.4**: **Optimize a slow query**
Answer included above in expanded details.

---

**1.5**: **How indexing works**
- Indexes speed up data retrieval by creating a sorted data structure for faster lookups. They work like a table of contents for data.
- Use indexing for columns involved in `WHERE`, `JOIN`, or `GROUP BY` clauses but avoid over-indexing, which slows down `INSERT/UPDATE` operations.

---

**1.6**: **Design a schema for performance data**
```sql
CREATE TABLE performance_data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    kpi_name VARCHAR(100),
    kpi_value DECIMAL(10, 2),
    measured_date DATE,
    region VARCHAR(50),
    comments TEXT
);
```

---

### **2. Python Questions**

**2.1**: **Automation Example**
Example shared above.

---

**2.2**: **Using Pandas and NumPy**
- Pandas handles structured data efficiently using DataFrames.
- Example: Calculate the average of a column.
```python
import pandas as pd
import numpy as np

data = pd.DataFrame({'sales': [200, 450, 300]})
average_sales = np.mean(data['sales'])
print(average_sales)
```

---

**2.3**: **Connect Python to SQL**
Example shared above.

---

**2.4**: **Generate an automated report**
- Use `matplotlib` for visuals and `xlsxwriter` for Excel reports.
```python
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [200, 300, 250]})

# Plot
data.plot(x='Month', y='Sales', kind='bar')
plt.savefig('sales_chart.png')

# Write to Excel
data.to_excel('Sales_Report.xlsx', index=False)
```

---

### **3. Power BI Questions**

**3.1**: **Handling large datasets**
- Import only necessary data.
- Use data reduction techniques like aggregations.
- Optimize relationships between tables and disable auto-detect.

---

**3.2**: **Interactive dashboard design**
Example shared above.

---

**3.3**: **Performance optimization techniques**
- Avoid calculated columns; use measures instead.
- Pre-aggregate data at the database level.
- Use Power Query to filter unnecessary data.

---

**3.4**: **Ensuring data accuracy**
- Ensure the data source is reliable.
- Perform transformations to clean raw data.
- Use DAX functions like `ISBLANK()` to handle missing values.

---

### **4. VBA and Excel Questions**

**4.1**: **VBA automation**
Example shared above.

---

**4.2**: **Dynamic dashboard design**
- Use slicers for interactivity.
- Use Excel functions like `OFFSET` for dynamic range definitions.
- Example:
```vba
Private Sub Worksheet_Change(ByVal Target As Range)
    If Target.Address = "$A$1" Then
        Call UpdateDashboard
    End If
End Sub

Sub UpdateDashboard()
    ' Recalculate ranges or update visuals
End Sub
```

---

### **5. Data Analysis and MIS Reporting**

**5.1**: **Analyze trends**
Example: Use SQL window functions:
```sql
SELECT region, sales_amount, 
       LAG(sales_amount) OVER (PARTITION BY region ORDER BY date) AS previous_sales,
       (sales_amount - LAG(sales_amount) OVER (PARTITION BY region ORDER BY date)) AS growth
FROM sales_data;
```

---

**5.2**: **Ensure data quality**
Steps included above.

---

**5.3**: **Manage stakeholder ad hoc reports**
- Gather requirements.
- Use tools like Power BI for rapid visualization.
- Automate frequent requests with SQL views or stored procedures.

---

### **6. Automation**

**6.1**: **Example**
Details shared above.

---

### **7. General Problem Solving**

**7.1**: **Resolve conflict in a team**
- Identify the root cause.
- Mediate and facilitate an open discussion.
- Create an action plan that addresses concerns.

---

**7.2**: **Managing priorities**
- Use prioritization frameworks like Eisenhower Matrix.
- Communicate timelines clearly to stakeholders.
- Example: "In a prior role, I managed overlapping deadlines for reports and used automation to meet all deliverables."

---

### **8. Behavioral and Team Management**

**8.1**: **Handling team performance issues**
- Provide constructive feedback in private.
- Offer support and training.
- Example: "I coached a junior team member struggling with SQL, leading to a marked improvement in query efficiency."

---

Let me know if you need more elaboration or help on specific areas!

--------------------------------
If you enjoy using this GPT and need something more powerful, want to be a beta tester for new versions, or just wish to support us, please check out our new [SQL Expert PRO GPT](https://chatgpt.com/g/g-6740a711568c819189f561c15e0707e6-beta-sql-expert-pro) with a monthly subscription and follow GPT creator profile on LinkedIn [https://linkedin.com/in/khanukov/](https://linkedin.com/in/khanukov/)

---

