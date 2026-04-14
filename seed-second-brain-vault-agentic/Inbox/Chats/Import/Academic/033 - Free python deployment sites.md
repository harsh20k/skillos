---
title: Free python deployment sites
category: Academic
priority: Medium
starred: None
created: 2025-11-03T19:16:08.741347
updated: 2025-11-08T14:50:25.228832
dg-publish: true
---
# Free python deployment sites

**Priority:** Medium

## Conversation

### Assistant

You can create or overwrite the `.env` file directly in shell using a *here-document*:  

```bash
cat > .env << 'EOF'
FLASK_ENV=production
DATABASE_URL=jdbc:mariadb://db-5308.cs.dal.ca:3306/CSCI5308_1_DEVINT

DB_HOST=db-5308.cs.dal.ca
DB_NAME=CSCI5308_1_DEVINT
DB_USER=CSCI5308_1_DEVINT_USER
DB_PASSWORD=Pohcoo5tig

AIRPORT_NAME=Halifax
EOF
```

Then check it:
```bash
cat .env
```

This writes exactly those lines into `.env` in your current directory.

---

