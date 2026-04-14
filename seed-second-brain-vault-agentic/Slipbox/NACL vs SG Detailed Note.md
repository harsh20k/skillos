---
creation date: 2026-02-10 11:55
tags: [concept]
---
## **Scope difference:**

**NACLs (Network ACLs):**

- Apply at the **subnet level**
- Affect **all resources** in that subnet (EC2, RDS, Lambda, etc.)
- Act as a firewall for the entire subnet boundary

**Security Groups:**

- Apply at the **individual resource level** (ENI - Elastic Network Interface)
- Each EC2 instance, RDS database, load balancer, etc. can have its own security group
- More granular control

![[image-179.png]]
## **Think of it like building security:**

- **NACL** = Security gate at the neighborhood entrance (controls what enters/leaves the entire neighborhood)
- **Security Group** = Lock on each individual house door (controls access to specific homes)

## **Practical example:**

```
Subnet: 10.0.1.0/24
├─ NACL: Blocks all traffic from 203.0.113.0/24
│
├─ EC2 Web Server (sg-web)
│  └─ Security Group: Allow port 80 from 0.0.0.0/0
│
├─ EC2 Database (sg-db)
│  └─ Security Group: Allow port 3306 from sg-web only
│
└─ EC2 App Server (sg-app)
   └─ Security Group: Allow port 8080 from sg-web only
```

Even though the web server's security group allows traffic from anywhere, the NACL can still block specific IP ranges at the subnet level.

## **Key differences:**

| Feature    | NACL                         | Security Group          |
| ---------- | ---------------------------- | ----------------------- |
| Scope      | Subnet (broader)             | Instance/ENI (narrower) |
| Rules      | Allow AND Deny               | Allow only              |
| State      | Stateless*                   | Stateful**              |
| Rule order | Numbered, processed in order | All rules evaluated     |
| Default    | Allows all in/out            | Denies all inbound      |

*Stateless = You must explicitly allow both inbound and outbound traffic **Stateful = If you allow inbound, the response is automatically allowed out

## **When to use which level:**

**NACL (broader, subnet-level):**

- Block known malicious IP ranges
- Comply with regulations requiring network-level controls
- Explicit deny rules (security groups can't deny)
- Usually set once and rarely changed

**Security Group (narrower, instance-level):**

- Day-to-day access control
- Allow specific application ports
- Reference other security groups (like "allow from web tier")
- Changed frequently as architecture evolves

## **Defense in depth:**

Most AWS architectures use **both**:

- NACLs as the first, broad filter
- Security groups as the precise, instance-specific control

It's like having both a neighborhood gate AND individual door locks - two layers of security.

Does that clarify the "broader vs narrower" concept?