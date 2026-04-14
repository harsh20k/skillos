---
title: What is Terraform
category: Technical
priority: Medium
starred: None
created: 2025-12-02T07:52:59.982227
updated: 2025-12-02T07:53:13.452731
dg-publish: true
---
# What is Terraform

**Priority:** Medium

## Conversation

### Assistant

Terraform is an **Infrastructure as Code (IaC)** tool used to **create, manage, and version cloud infrastructure** using simple configuration files.

## Core idea
You write instructions in **.tf (HCL)** files describing what you want:
- virtual machines  
- databases  
- networks  
- load balancers  
- Kubernetes clusters  
- DNS records  
- storage buckets  

Then Terraform talks to cloud providers (AWS, Azure, GCP, DigitalOcean, etc.) and **creates or updates everything automatically**.

## Why it’s useful
1. **Infrastructure as code**  
   Your infrastructure is written like code → easy to version control and review.

2. **Reusable and consistent**  
   Same configuration can deploy to multiple environments (dev, staging, prod).

3. **Plan before applying**  
   Terraform shows a **plan** (what changes will happen) before making them.

4. **State management**  
   It tracks what exists to avoid recreating or deleting things accidentally.

5. **Multi-cloud**  
   Works with many providers, not tied to one cloud.

## Simple example

```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "harsh-demo-bucket"
}
```

Run:
```
terraform init
terraform plan
terraform apply
```

Terraform creates the S3 bucket.

## When to use it
- Cloud infrastructure provisioning  
- Automated dev/test environments  
- Production deployments  
- Multi-cloud architecture  
- Managing DNS, SSL certificates, and networking

If you want, I can also explain:  
- how Terraform compares to Ansible / Pulumi  
- a real example for AWS / GCP / Azure  
- installing Terraform on macOS or Linux

---

