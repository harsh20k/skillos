---
title: Minutes of meeting
category: General
priority: Medium
starred: None
created: 2025-10-16T17:21:49.053073
updated: 2025-10-17T17:13:33.516544
dg-publish: true
---
# Minutes of meeting

**Priority:** Medium

## Conversation

### Assistant

Excellent question — and you’re thinking in exactly the right direction.  

When you have a **meeting recording (audio or transcript)**, AI can extract *structured information* and *contextual knowledge* far beyond just “who said what.”  
Here’s a full breakdown of what can be extracted — grouped by **type of intelligence** 👇  

---

## 🗓️ 1. **Temporal Information (Dates, Times, and Events)**
AI can automatically detect and structure **time-based data** mentioned during a meeting, such as:
- **Specific dates and times** — e.g., *“Let’s deploy on October 20th”* → `Deployment date: 2025-10-20`
- **Relative dates** — e.g., *“Next Friday”*, *“in two weeks”*, *“by end of Q4”* (AI can normalize these to calendar dates if the meeting date is known)
- **Event durations** — e.g., *“Testing will take three days”*
- **Meeting scheduling** — e.g., *“Follow-up meeting next Monday at 2 PM”*

✅ *Use case:* Automatically populate a **timeline**, **calendar**, or **project plan** from the transcript.  

---

## 👥 2. **People and Roles (Named Entity Recognition)**
AI can identify:
- **Attendees / Speakers**
- **Mentioned people or organizations** — e.g., *“Dr. McAllister,” “Registrar’s Office,” “IBM Cloud”*
- **Roles and responsibilities** — e.g., *“Harsh will handle API integration,” “Mootez leads frontend”*

✅ *Use case:* Build **attendance lists**, assign **action owners**, or tag **stakeholders**.  

---

## 💬 3. **Action Items and Decisions**
AI can detect actionable statements such as:
- **Tasks / to-dos** — *“We need to send the API by Friday”*
- **Decisions made** — *“We decided to use dummy data for now”*
- **Pending actions / questions** — *“We still need confirmation from the client”*

✅ *Use case:* Auto-generate **action summaries** or update **project boards (e.g., Jira, Trello)**.

---

## 📚 4. **Knowledge References (External Mentions)**
AI can extract and classify references such as:
- **Books, research papers, or authors**
- **Movies, shows, or cultural references**
- **Websites, tools, APIs, frameworks, or datasets**

Example:
> “Let’s use the dataset from Kaggle — the Titanic competition.”  
→ Detected as: `Reference: Kaggle (Titanic Dataset)`

✅ *Use case:* Build a **“Knowledge Graph”** of cited or relevant materials from the meeting.  

---

## 🧠 5. **Thematic and Contextual Summaries**
AI can cluster discussions into **topics** and **themes**, such as:
- Login system / API integration  
- Data privacy  
- Sprint planning  
- Testing and deployment  

✅ *Use case:* Create **section-wise summaries** or generate **meeting minutes automatically.**  

---

## 📊 6. **Sentiment and Tone Analysis**
Detects **tone** or **emotion** in speech:
- Positive / negative / neutral sentiment
- Frustration, agreement, urgency, etc.

✅ *Use case:* Evaluate **team mood**, **meeting dynamics**, or **client satisfaction trends** over time.  

---

## 🔐 7. **Confidential or Sensitive Mentions**
AI can flag:
- Mentions of **personal data**, **financial info**, or **confidential terms**
- Compliance risks (GDPR, HIPAA, etc.)

✅ *Use case:* Automatic **privacy filtering** or **compliance review** of recorded calls.  

---

## 🧩 8. **Cross-Meeting Intelligence (Knowledge Graphs)**
When you process multiple meeting recordings, AI can:
- Link **recurring topics** (“API delays” across weeks)  
- Identify **dependencies** between tasks or decisions  
- Track **progress and blockers** over time  

✅ *Use case:* Generate an evolving **organizational knowledge base** from all discussions.  

---

### 💡 Example Output Schema (for one meeting)
| Category | Extracted Info |
|-----------|----------------|
| **Date Mentioned** | “Deployment on Oct 20, 2025” |
| **Event** | “Sprint 2 starts next week” |
| **People** | Harsh (Dev), Mootez (Lead), Dr. McAllister (Faculty) |
| **Decisions** | Use dummy data until API available |
| **Action Items** | Devanshu → integrate login API |
| **References** | “Slate” system, “Registrar’s Office” |
| **Sentiment** | Neutral, collaborative |
| **Next Meeting** | “Plan sprint milestone next Monday” |

---

Would you like me to show you **how this could be modeled as a JSON structure** (for automation, e.g., feeding into Notion or a database)?  
That’s often the next step after extracting all this information.

---

