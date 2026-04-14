---
creation date: 2026-01-30 09:19
tags: [concept]
---
The Terraform state file is **Terraform’s memory** of your infrastructure—without it, safe and incremental infrastructure changes are impossible.


- Maps Terraform configuration to real cloud resources
- Stores resource IDs, attributes, and dependencies
- Enables plan to calculate changes safely
- Prevents unnecessary destroy/recreate actions
- Can be local or remote (remote preferred for teams)

