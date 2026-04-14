---
title: Meeting intelligence extraction
category: General
priority: Medium
starred: None
created: 2025-10-13T08:48:33.797265
updated: 2025-10-13T08:48:44.013139
dg-publish: true
---
# Meeting intelligence extraction

**Priority:** Medium

## Conversation

### Assistant

Here’s the **user story** for your second feature — the Meeting Bot’s **intelligence gathering and summary extraction** after recording a meeting:  

---

### **User Story: Meeting Intelligence Extraction**

**Description:**  
As a registered user, I want the Meeting Bot to automatically analyze the meeting recording and extract key information — such as important dates, upcoming events, attendees, and summarized discussion points — so that I can quickly review what happened without rewatching the entire recording.

---

### **Acceptance Criteria (AC):**

#### **AC 1: Automatic Meeting Analysis**
- **Given** the meeting recording and transcript are available after the meeting ends.  
- **When** the recording is processed by the bot.  
- **Then** the bot automatically analyzes the meeting content.  
- **And** it extracts key details such as:
  - Important **dates, events, or deadlines**
  - **Attendees** and their participation context  
  - **Decisions made**
  - **Action items** with owners and due dates  
  - **Topics discussed**

---

#### **AC 2: Summary and Highlights Generation**
- **Given** the extracted information from the meeting.  
- **When** the analysis is complete.  
- **Then** the bot generates a structured meeting summary including:  
  - A short **executive summary** (2–3 sentences)  
  - A **list of attendees**  
  - **Key discussion points** grouped by topic  
  - **Next steps / action items**  
  - **Important dates or deadlines**

---

#### **AC 3: Storage and Access**
- **Given** the analysis output is ready.  
- **When** the user opens the meeting summary interface (or dashboard).  
- **Then** the extracted data should be visible and searchable.  
- **And** users can export or share it in formats like **PDF, DOCX, or via email**.

---

#### **AC 4: Error and Missing Data Handling**
- **Given** the meeting recording or transcript is incomplete or corrupted.  
- **When** the bot cannot extract meaningful insights.  
- **Then** it logs the issue.  
- **And** notifies the user with a clear message describing what went wrong (e.g., “Audio quality too low to identify speakers”).

---

Would you like me to **add another version written in Gherkin syntax** (Given–When–Then format) suitable for BDD tools like *Cucumber or Jira Xray*?

---

