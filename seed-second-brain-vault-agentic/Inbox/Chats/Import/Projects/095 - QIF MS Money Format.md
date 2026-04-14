---
title: QIF MS Money Format
category: Projects
priority: Medium
starred: None
created: 2024-12-07T23:03:29.849333
updated: 2024-12-07T23:03:41.356943
dg-publish: true
---
# QIF MS Money Format

**Priority:** Medium

## Conversation

### Assistant

The **QIF (Quicken Interchange Format)** is a file format developed by Intuit for its Quicken personal finance software. It is commonly used to transfer financial data between different programs or financial institutions. The format is plain-text and designed to be human-readable.

### Characteristics of QIF Format
- **Text-based:** The file is structured using plain text, making it easy to view and edit in a text editor.
- **Line-based structure:** Each record consists of multiple lines, with each line starting with a specific character that identifies the type of data.
- **Headers and Fields:** A header line (e.g., `!Type:Bank`) defines the type of account or transaction that follows. The data lines provide the details of transactions, such as dates, amounts, and categories.

### Usage in MS Money
Microsoft Money was a popular personal finance management tool, and it supported the QIF format for importing and exporting financial data. This allowed users to move their data between MS Money and other software (like Quicken) or financial institutions.

### Common Applications of QIF Files
1. **Data Transfer:** Sharing financial data between different accounting or budgeting tools.
2. **Backup:** Saving financial data for archival purposes.
3. **Editing:** Making manual changes to transactions or categories using a text editor.
4. **Integration with Banks:** Importing downloaded bank or credit card statements into financial software.

### Key Components of a QIF File
- **Account Type Header:** Specifies the type of transactions (e.g., bank, credit card, etc.).
  Example: `!Type:Bank`
- **Transaction Details:**
  - Date: `D[MM/DD/YYYY]`
  - Amount: `T[amount]`
  - Payee: `P[Payee Name]`
  - Memo: `M[Memo Text]`
  - Category: `L[Category Name]`
  - Cleared Status: `C[*|X]`
- **End of Transaction:** Denoted by a single `^` character.

### Example QIF File
```plaintext
!Type:Bank
D12/08/2024
T-200.00
PJohn Doe
MElectricity Bill
LUtilities
^
D12/09/2024
T1500.00
PEmployer
MSalary
LIncome:Salary
^
```

This example represents:
1. A $200 withdrawal for an electricity bill on December 8, 2024.
2. A $1,500 deposit as salary on December 9, 2024.

### Limitations
- **Compatibility Issues:** Some modern financial software no longer supports QIF files, as newer formats like OFX (Open Financial Exchange) have become more popular.
- **Limited Validation:** Because QIF is text-based, errors in formatting can easily occur during manual editing.

If you need to use QIF files with modern tools, some converters or legacy support options might be necessary.

---

