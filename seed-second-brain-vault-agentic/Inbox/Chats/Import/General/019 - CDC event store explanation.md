---
title: CDC event store explanation
category: General
priority: Medium
starred: None
created: 2025-12-14T20:27:03.081222
updated: 2025-12-15T11:07:14.551004
dg-publish: true
---
# CDC event store explanation

**Priority:** Medium

## Conversation

### Assistant

Yes.  
You **can merge PDFs in Python**, and **yes — it requires a library**. Python’s standard library **cannot** manipulate PDFs.

Below is a **clear, practical breakdown** and a **ready-to-use script**.

---

## 1. Do you need special libraries?
**Yes.** PDFs are binary, structured documents.

The most commonly used libraries:

### ✅ Recommended
- **`pypdf`** (modern, maintained)
- **`PyPDF2`** (older, still works)

### ⚠️ Optional / advanced
- `pdfplumber` → text extraction (not merging)
- `reportlab` → PDF creation
- `fitz` / `PyMuPDF` → advanced editing, heavy dependency

For **simple merging**, use **`pypdf`**.

---

## 2. Install the library

```bash
pip install pypdf
```

---

## 3. Simple PDF merge script (interactive)

This script:
- Asks for folder containing PDFs
- Asks for output PDF name
- Merges PDFs in **alphabetical order**

### ✅ `merge_pdfs.py`

```python
from pathlib import Path
from pypdf import PdfMerger

def main():
    folder_input = input("Enter path to folder containing PDFs:\n> ").strip()
    folder = Path(folder_input).expanduser()

    if not folder.exists() or not folder.is_dir():
        print("❌ Invalid folder path.")
        return

    output_name = input("Enter output PDF name (without .pdf):\n> ").strip()
    if not output_name:
        print("❌ Output name cannot be empty.")
        return

    output_file = folder / f"{output_name}.pdf"

    pdf_files = sorted(folder.glob("*.pdf"))

    if not pdf_files:
        print("❌ No PDF files found.")
        return

    merger = PdfMerger()

    for pdf in pdf_files:
        print(f"➕ Adding: {pdf.name}")
        merger.append(pdf)

    merger.write(output_file)
    merger.close()

    print(f"\n✅ Merged {len(pdf_files)} PDFs into:")
    print(f"📄 {output_file}")

if __name__ == "__main__":
    main()
```

---

## 4. Advanced version (date-aware like your notes)
If your PDFs follow the same pattern:
```
5100 08-10-2025.pdf
```

You can reuse **the same date-extraction logic** and:
- Sort PDFs chronologically
- Append undated PDFs last

(Exactly like your Markdown script.)

I can provide this version if you want.

---

## 5. Comparison: Markdown vs PDF merging

| Task | Markdown | PDF |
|----|----|----|
| Native Python | ✅ | ❌ |
| Needs library | ❌ | ✅ |
| Ordering control | Easy | Easy |
| Content editing | Easy | Hard |
| Best tool | Python stdlib | `pypdf` |

---

## 6. When NOT to merge PDFs in Python
Don’t use Python if:
- You need OCR
- You need page-level annotations
- You need layout changes

Use:
- Preview (macOS)
- PDF Expert
- Adobe Acrobat

---

## 7. Mental model
> Markdown merging = text concatenation  
> PDF merging = structural document manipulation  

That’s why a library is required.

---

If you want next:
- One **unified script**: merge `.md` + `.pdf`
- Date-aware PDF merge
- Folder-recursive merge
- Insert blank page separators
- Add TOC page

Say which one.

---

