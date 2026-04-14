---
title: Change button color
category: Technical
priority: Medium
starred: None
created: 2025-08-19T03:17:11.207735
updated: 2025-08-19T05:55:35.643591
dg-publish: true
---
# Change button color

**Priority:** Medium

## Conversation

### Assistant

In Obsidian, **“Bases”** is a powerful **core plugin**—recently added in version 1.9—that brings native database-like capabilities directly into your vault. Here's what they are and how they work:

---

###  What Are Bases?

- **Bases = Database views on your notes**  
  Bases let you **turn any set of your Obsidian notes into an interactive database**, displaying them in a table (with more view types like cards or Kanban on the roadmap) citeturn0search0turn0search4.

- **They leverage your existing Markdown + YAML**  
  Rather than storing things in a separate database, Bases use your notes’ **YAML frontmatter ("properties")** and metadata (like tags, dates, etc.) as the data source citeturn0search0turn0search12.

- **No code required**  
  Unlike community plugins like Dataview—which require learning query syntax—Bases offer a **visual GUI**. You can define filters, select which properties to view, and even edit metadata directly in the table citeturn0search3turn0search4.

---

###  Key Features at a Glance

| Feature                      | Description |
|------------------------------|-------------|
| **View Types**               | Currently supports **tables**, with more types (cards, Kanban) planned citeturn0search4turn0search7turn0search6. |
| **Filtering & Sorting**      | Define filters using YAML properties (e.g., tags, dates) and sort by any column citeturn0search4turn0search3. |
| **Inline Editing**           | Modify properties directly within the Base view—no need to open each note citeturn0search1turn0search8. |
| **GUI-Centric**              | Create and customize views through a graphical interface—far more approachable than writing queries citeturn0search3turn0search12. |
| **Built on core functionality** | Bases are first-party, maintained by Obsidian, not a third-party plugin citeturn0search12turn0search0. |
| **Lightweight and local**    | Works entirely offline on your Markdown files—your data stays in your vault citeturn0search12. |

---

###  Why It Matters

- **Obsidian becomes more like Notion—but with your files stored as plain text.**  
  You get database-style organization without sacrificing portability and control citeturn0search12turn0search8.

- **More powerful than simple searching.**  
  Instead of manually filtering or searching tags, Bases provide dynamic views that auto-update as you edit your notes—filtering and sorting happen live citeturn0news13turn0search8.

- **A user-friendly alternative to Dataview.**  
  If Dataview’s query language feels daunting, Bases deliver similar functionality (tables, filters, properties) through a much smoother interface citeturn0search12turn0search1turn0search4.

- **Continuously evolving.**  
  More view types, better layouts, and even plugin APIs are planned citeturn0search7turn0search6.

---

###  What Users Are Saying

From discussions on Hacker News:

> “Bases provides filtered and sortable table and card views of note Properties and Tags.” citeturn0search6  
> “It’s really just that, basically... a database-view, where the vault is the database and the rows are your files.” citeturn0search6

This sums up how Bases feel: structured, powerful, and integrated into your vault, without a steep learning curve.

---

###  How to Get Started

1. **Enable it:** Go to **Settings → Core Plugins** and toggle on **Bases**. (Enable **Properties** too, as it's complementary.) citeturn0search3  
2. **Create a Base:**  
   - Use the Command Palette (`Ctrl/Cmd+P`) and select **Bases: Create new base**.  
   - Or right-click a folder and choose **New base**.  
   - You can also **insert a Base** into an existing note via the palette citeturn0search4turn0search3.
3. **Build your view:**  
   - Open the Base and add filters (e.g., `tag is “reading”` or `date > 2025-06-01`).  
   - Select which properties to display as columns (e.g., title, status, date).  
   - Sort by clicking any column header citeturn0search4turn0search3.

---

###  Summary

**"Bases" in Obsidian** = A built-in plugin that transforms your notes into **live, interactive databases** using your existing metadata. You can filter, sort, and edit note properties in a nice GUI—no SQL-style queries needed. It’s ideal for trackers, reading logs, project dashboards, glossaries, and more—and all with your notes still staying in Markdown, offline, and under your control.

Let me know if you’d like help building your first Base (e.g., tracking books, projects, journals)—I’d be happy to walk you through it!

---

