---
title: Graph-based website examples
category: Academic
priority: Medium
starred: None
created: 2025-11-24T12:26:47.511977
updated: 2025-11-24T12:27:00.303631
dg-publish: true
---
# Graph-based website examples

**Priority:** Medium

## Conversation

### Assistant

Here are a few examples of websites and applications using graph/graph-database technology (via entity["software", "Neo4j", 0] or similar) — this should help you understand how “graph-based websites” work in practice:

---

### 1. entity["organization", "NBC News", 0]  
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["NBC News troll network Neo4j","NBC News graph database social media analysis","NBC News Neo4j community detection case study"],"num_per_query":2}  
- NBC News used Neo4j for social-media / network analysis: they mapped relationships between tweets, users, hashtags, etc., and applied graph algorithms (community detection, centrality) to surface troll networks. citeturn0search11  
- Insight: A graph database allows modelling of *entities + relationships* (users ↔ tweets ↔ hashtags ↔ sources) and then analysing connection-patterns rather than just flat tables.

---

### 2. Large enterprises via Neo4j’s “Who Uses Neo4j” list  
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Airbus Neo4j graph database use case","Uber Neo4j knowledge graph example","BNP Paribas Neo4j fraud detection graph"],"num_per_query":2}  
- Neo4j claims that more than 75% of the Fortune 100 organisations use their graph technology. citeturn0search0turn0search1  
- For example, companies in sectors such as airlines, banking, retail, telecommunication use graph databases for recommendations, fraud detection, network management, etc.  
- While not always “websites” in the sense of a publicly visible web-app, many backend services tied to websites or user-apps are graph-based.

---

### 3. Case study in “Top Graph Database Use Cases”  
image_group{"layout":"carousel","aspect_ratio":"1:1","query":["Neo4j recommendation engine graph database example","Neo4j supply chain digital twin graph example","Neo4j customer 360 graph model"],"num_per_query":2}  
- According to Neo4j’s blog, common use-cases include: real-time recommendations, customer 360 views, fraud detection, supply-chain end-to-end visibility. citeturn0search2turn0search3  
- For a website / web app, “recommendation engine” and “customer 360” are especially relevant: you might have a website that recommends items by traversing “customer → purchase → similar item → similar customer” graph paths.

---

If you like, I can pull together **5-10 specific public web apps** (for example social networks, e-commerce sites) that show case studies with Neo4j (or other graph DBs) and include details of how they use the graph model. Would that be helpful?

---

