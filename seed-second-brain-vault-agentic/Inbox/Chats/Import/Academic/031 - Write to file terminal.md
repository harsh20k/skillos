---
title: Write to file terminal
category: Academic
priority: Medium
starred: None
created: 2025-11-09T20:11:57.851766
updated: 2025-11-09T20:12:09.425767
dg-publish: true
---
# Write to file terminal

**Priority:** Medium

## Conversation

### Assistant

Yes. You can use `echo` with redirection:  
```bash
echo "FLASK_ENV=production
DATABASE_URL=jdbc:mariadb://db-5308.cs.dal.ca:3306/CSCI5308_1_DEVINT

DB_HOST=db-5308.cs.dal.ca
DB_NAME=CSCI5308_1_DEVINT
DB_USER=CSCI5308_1_DEVINT_USER
DB_PASSWORD=Pohcoo5tig

AIRPORT_NAME=Halifax (YHZ)" > .env
```

Then confirm it’s written correctly:  
```bash
cat .env
```

---

