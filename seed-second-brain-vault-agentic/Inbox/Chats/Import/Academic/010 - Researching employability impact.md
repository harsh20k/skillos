---
title: Researching employability impact
category: Academic
priority: Medium
starred: None
created: 2025-12-21T12:06:20.788038
updated: 2025-12-21T13:02:56.169842
dg-publish: true
---
# Researching employability impact

**Priority:** Medium

## Conversation

### Assistant

Below is a **clean, Obsidian-ready Mermaid diagram** that **summarises the employability analysis**, **categorised by courses**, and shows how each course connects to **skills → roles → employers in Halifax**.

You can paste this directly into Obsidian / Markdown that supports Mermaid.

---

```mermaid
graph TD

%% =========================
%% COURSE LAYER
%% =========================
subgraph Courses
    C5409[CSCI 5409<br/>Advanced Cloud Computing]
    C5410[CSCI 5410<br/>Serverless Data Processing]
    C5709[CSCI 5709<br/>Advanced Web Development]
    C5708[CSCI 5708<br/>Mobile Computing]
    C6405[CSCI 6405<br/>Data Mining & Warehousing]
    C6409[CSCI 6409<br/>Process of Data Science]
    C6406[CSCI 6406<br/>Visualization]
    C6516[CSCI 6516<br/>Deep Learning]
    C6520[CSCI 6520<br/>NLP with Deep Learning]
    C6314[CSCI 6314<br/>Applied ML for SE]
end

%% =========================
%% SKILLS LAYER
%% =========================
subgraph Skills
    Cloud[Cloud: AWS · Azure · Docker · Kubernetes]
    Web[Web: React · Angular · REST APIs · Security]
    DataEng[Data: SQL · ETL · Warehousing · Pipelines]
    DataSci[Data Science: E2E Projects · Experimentation]
    Viz[Visualization: Dashboards · Storytelling]
    DL[Deep Learning: CNN · RNN · Transformers]
    NLP[NLP: Text Models · LLMs · Language AI]
    Mobile[Mobile: Android · iOS · React Native]
    MLSE[ML for Software: Code Analysis · Automation]
end

%% =========================
%% ROLE LAYER
%% =========================
subgraph Roles
    SE[Software Engineer]
    FSD[Full-Stack / Backend Dev]
    CE[Cloud / DevOps Engineer]
    DE[Data Engineer]
    DA[Data Analyst]
    DS[Data Scientist / ML Engineer]
    MD[Mobile Developer]
end

%% =========================
%% EMPLOYER LAYER
%% =========================
subgraph Halifax Employers
    Banks[Banks<br/>RBC · TD · Scotiabank]
    Consult[Consulting / IT<br/>CGI · IBM · Cognizant]
    Gov[Government / Crown Corps]
    Startups[Startups & Scaleups]
    AIcos[AI / R&D Orgs]
end

%% =========================
%% COURSE → SKILLS
%% =========================
C5409 --> Cloud
C5410 --> Cloud
C5410 --> DataEng
C5709 --> Web
C5708 --> Mobile
C6405 --> DataEng
C6405 --> DataSci
C6409 --> DataSci
C6406 --> Viz
C6516 --> DL
C6520 --> DL
C6520 --> NLP
C6314 --> MLSE

%% =========================
%% SKILLS → ROLES
%% =========================
Cloud --> CE
Cloud --> SE
Cloud --> FSD

Web --> FSD
Web --> SE

DataEng --> DE
DataEng --> DA

DataSci --> DS
DataSci --> DA

Viz --> DA

DL --> DS
NLP --> DS

Mobile --> MD

MLSE --> DS

%% =========================
%% ROLES → EMPLOYERS
%% =========================
SE --> Banks
SE --> Consult
SE --> Startups

FSD --> Banks
FSD --> Consult
FSD --> Startups

CE --> Banks
CE --> Consult

DE --> Banks
DE --> Consult
DE --> Gov

DA --> Banks
DA --> Gov
DA --> Consult

DS --> Banks
DS --> AIcos

MD --> Consult
MD --> Startups
```

---

### How to read this diagram (quickly)
- **Top → Bottom flow**:  
  **Course → Skills → Job Roles → Halifax Employers**
- Courses higher in demand (Cloud, Web, Data) connect to **more roles and more employers**
- Specialized courses (NLP, ML for SE, Mobile) connect to **fewer but niche paths**
- This visually explains **why Cloud + Web + Data courses rank highest for employability**

---

### If you want next
I can:
- Create a **second Mermaid diagram showing recommended course bundles**
- Convert this into an **Obsidian MOC page**
- Add **weighting labels** (High / Medium / Low demand) on edges
- Produce a **one-page visual decision chart** for final course selection

Tell me what you want next.

---

