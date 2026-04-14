---
creation date: 2026-03-31 18:08
tags:
description:
---
## Module 1: Authentication & 3FA System (AWS)

# **Overview & Problem Statement**

- Implemented secure multi-factor authentication beyond standard password protection
- Addresses the need for progressive authentication with session state management

# **Architecture Components**

- **Cognito User Pool**: Email-based authentication with password policies
- **HTTP API Gateway v2**: RESTful endpoints with CORS support for SPA integration
- **9 Lambda Functions**: Serverless handlers for each authentication step
- **4 DynamoDB Tables**: Users (MFA config), Tokens (bearer with TTL), Sessions (F1/F2/F3 flags), Challenges (Caesar cipher with TTL)
- **SNS Topic**: User alerts for authentication events

**3-Factor Authentication Flow**
- **Factor 1**: Cognito password authentication (email + password)
- **Factor 2**: Security question verification (stored in users table)
- **Factor 3**: Caesar cipher challenge (random shift, time-limited)
- Progressive unlock: Each factor must be completed sequentially

# **Key Technical Decisions**

- Chose DynamoDB for low-latency session lookups with automatic TTL expiration
- Used HTTP API v2 (not REST API) for better performance and lower cost
- Implemented stateful sessions to track multi-step authentication progress
- Bearer tokens with TTL for post-authentication API access

# **Security Features**

- Password policy enforcement via Cognito
- Time-limited challenges prevent replay attacks
- Session state prevents factor skipping
- IAM policies follow least-privilege principle

---

## Module 6: Frontend (GCP Cloud Run)

**Overview & Architecture**
- React + TypeScript SPA deployed as containerized service on GCP Cloud Run
- Containerized with Docker, served via Nginx
- Auto-scaling serverless container platform

**Deployment Strategy**
- **Build Process**: Multi-stage Docker build (Node.js build → Nginx serve)
- **Container Registry**: Google Artifact Registry
- **CI/CD**: Cloud Build with automated deployments
- **Environment Configuration**: Build-time injection of API endpoints via Docker args

**Cross-Platform Integration**
- Integrates with AWS Module 1 Auth API (HTTP API v2)
- Connects to AWS Module 2 Lex Chatbot (REST API)
- Calls AWS Module 4 Notification API (REST API)
- Uses GCP Module 3 Cloud Functions (concerns management)
- Consumes GCP Module 5 Cloud Functions (feedback system)

**Key Features Implemented**
- **Authentication UI**: Multi-step 3FA flow with real-time validation
- **Operator Dashboard**: Admin analytics and session management
- **Security Question Setup**: Custom MFA configuration during signup
- **Caesar Cipher Challenge UI**: Interactive Factor 3 verification
- **Profile Management**: User profile and MFA settings

**Technical Highlights**
- Used Vite for fast development and optimized production builds
- Implemented API client with centralized error handling
- CORS-compliant requests to cross-cloud APIs
- Responsive design for mobile and desktop
- Environment-based configuration for multi-environment deployments

**Why Cloud Run over S3?**
- Server-side capabilities (if needed for future SSR)
- Unified deployment model across GCP services
- Auto-scaling with pay-per-use pricing
- Better integration with GCP ecosystem (IAM, logging, monitoring)
- Container portability (can run locally or on other platforms)