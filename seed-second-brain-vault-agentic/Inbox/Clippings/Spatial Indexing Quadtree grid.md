---
title: "(1) Post | LinkedIn"
source: "https://www.linkedin.com/posts/activity-7403810605305896960-CPpz/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEOWBPQBEqYpcTm-_KuHOh81MkmMYmyw0D8"
author:
published: 4d
created: 2025-12-12
description:
tags:
  - "clippings"
dg-publish: true
---
## Feed detail update

## Feed post

Building a "𝐍𝐞𝐚𝐫𝐛𝐲 𝐅𝐫𝐢𝐞𝐧𝐝𝐬" or "𝐑𝐢𝐝𝐞 𝐇𝐚𝐢𝐥𝐢𝐧𝐠" service? 📍  

Stop trying to use standard B-Tree indexes for latitude/longitude. It won't scale.  
When you build a Proximity Service (like Uber, Tinder, or Yelp), the challenge isn't storing the location - it's querying it efficiently.  
  
If you run 𝐒𝐄𝐋𝐄𝐂𝐓 \* 𝐅𝐑𝐎𝐌 𝐝𝐫𝐢𝐯𝐞𝐫𝐬 𝐖𝐇𝐄𝐑𝐄 𝐥𝐚𝐭 𝐁𝐄𝐓𝐖𝐄𝐄𝐍 𝐱 𝐀𝐍𝐃 𝐲... on a high-traffic app, you will kill your database.  
  
Here is how the top players handle geospatial system design, and which DB you should pick:  
1️⃣ 𝐓𝐡𝐞 𝐇𝐞𝐚𝐯𝐲𝐰𝐞𝐢𝐠𝐡𝐭: 𝐏𝐨𝐬𝐭𝐠𝐫𝐞𝐒𝐐𝐋 + 𝐏𝐨𝐬𝐭𝐆𝐈𝐒  
The Tech: Uses R-Trees (and GiST indexes) to organize data using Bounding Boxes.  
Best For: Complex queries ("Find me all coffee shops inside this specific 5-point polygon").  
Verdict: If your data is static (restaurants, buildings) and accuracy is key, this is the industry standard.  
  
2️⃣ 𝐓𝐡𝐞 𝐒𝐩𝐞𝐞𝐝 𝐃𝐞𝐦𝐨𝐧: 𝐑𝐞𝐝𝐢𝐬 (𝐆𝐞𝐨)  
The Tech: It uses Geohashing. It converts 2D coordinates (Lat/Long) into a single 52-bit integer and stores it in a Sorted Set (ZSET).  
The Magic: Because it’s a 1D number now, Redis can use simple range queries (ZPASS) to find nearby points instantly.  
Best For: High-velocity updates (e.g., Live tracking 50k moving drivers).  
Verdict: If your data moves (taxis, delivery riders), PostGIS writes might be too slow. Redis is O(log(N)) and entirely in-memory. ⚡  
  
3️⃣ 𝐓𝐡𝐞 𝐇𝐲𝐛𝐫𝐢𝐝: 𝐄𝐥𝐚𝐬𝐭𝐢𝐜𝐬𝐞𝐚𝐫𝐜𝐡  
The Tech: Uses BKD Trees (Block K-Dimensional trees).  
Best For: "Search + Location." Example: "Find 'Sushi' (Text Match) within '5km' (Geo Filter)."  
Verdict: Great for relevance scoring, but heavier than Redis.  
  
💡 𝐓𝐡𝐞 𝐒𝐞𝐜𝐫𝐞𝐭 𝐒𝐚𝐮𝐜𝐞: 𝐒𝐩𝐚𝐭𝐢𝐚𝐥 𝐈𝐧𝐝𝐞𝐱𝐢𝐧𝐠  
To make any of this work at scale, you need to understand Quadtrees or Google S2/H3. These algorithms divide the world into manageable grids (buckets).  
  
Instead of calculating the distance between you and 1,000,000 drivers, the DB only looks at the drivers in your specific "grid bucket."  
  
Check out the image below to visualize how spatial indexing works:  
The diagram illustrates a map divided into a Quadtree grid. A user (a blue dot) is at the center of a search radius (a transparent blue circle). Numerous red dots (representing other users or points of interest) are scattered across the map. The key feature is that only the grid cells that intersect with the search radius are highlighted in green, indicating that only these specific cells are queried by the database, while all other cells remain un-highlighted and are ignored.  
  
𝐒𝐲𝐬𝐭𝐞𝐦 𝐃𝐞𝐬𝐢𝐠𝐧 𝐓𝐢𝐩:  
\- Most scalable architectures use both.  
\- Use Redis to track the live location of the driver (ephemeral data), and sync it to Postgres every few seconds for persistence and analytics.  
  
𝐌𝐨𝐫𝐞 𝐚𝐛𝐨𝐮𝐭 𝐐𝐮𝐚𝐝𝐭𝐫𝐞𝐞:[https://lnkd.in/gEwRrQ23](https://lnkd.in/gEwRrQ23)  
  
[hashtag SystemDesign](https://www.linkedin.com/search/results/all/?keywords=%23systemdesign&origin=HASH_TAG_FROM_FEED) [hashtag Redis](https://www.linkedin.com/search/results/all/?keywords=%23redis&origin=HASH_TAG_FROM_FEED) [hashtag PostgreSQL](https://www.linkedin.com/search/results/all/?keywords=%23postgresql&origin=HASH_TAG_FROM_FEED) [hashtag Geospatial](https://www.linkedin.com/search/results/all/?keywords=%23geospatial&origin=HASH_TAG_FROM_FEED)### [Rahul Goswami • 1st](https://www.linkedin.com/in/rahulgoswami2000)

[

SDE-1 at Best Buy || AWS Solutions Architect || Student at Dalhousie University || ex-SDE @Silicon IT || Competitive Programmer || Cloud Enthusiast || Part Time Investor 💸

](https://www.linkedin.com/in/rahulgoswami2000)### [Jeelkumar Baraiya • 3rd+](https://www.linkedin.com/in/jeelrb30)

[

SSE @Sprinklr | React | Javascript | GraphQL | Node.js

](https://www.linkedin.com/in/jeelrb30)