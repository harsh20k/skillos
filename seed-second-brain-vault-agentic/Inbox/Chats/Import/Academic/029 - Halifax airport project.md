---
title: Halifax airport project
category: Academic
priority: Medium
starred: None
created: 2025-11-05T23:03:20.581177
updated: 2025-11-10T16:47:30.523022
dg-publish: true
---
# Halifax airport project

**Priority:** Medium

## Conversation

### Assistant

Sure — here’s a clean, natural markdown version of your report written in plain, human-style language, ready to paste into **Obsidian**.  

---

# ✈️ Project Report – Halifax Airport Traveler App

## Overview

This report explains the story points, the work required for each feature, and the risks or uncertainties that come with them. It also describes how the team plans to handle those risks and what changes were made to the product backlog based on the client’s feedback.

The main focus of this sprint was to implement **passenger login**, **arrivals page**, and **departures page** features in the backend and mobile app.  
Additionally, we made one major change in response to the client — adding **guest login** access for users who don’t have a ticket.

---

## 🧩 Changes Based on Client Feedback

Originally, the client wanted to limit the app’s functionality only to logged-in passengers. After our discussion, they realized that showing basic airport information (arrivals, departures) to guests would improve usability and attract more users.

So we made this change:

- **Added Guest Login** — Users can now explore arrivals and departures without logging in.
- Logged-in passengers still have access to extra features like:
  - Real-time notifications
  - Airport navigation and shop info
  - Personalized flight tracking

This change added some new backend logic for authorization and required small adjustments in the front-end login flow.

---

## 🧾 Story Points and Rationale

### 1. Passenger Login – 5 Story Points

**User Story:**  
> As a passenger, I want to log in to the traveler app using my ticket number and last name so that I can access additional features in the app.

#### Why 5 points?
- Login involves multiple backend and frontend components:
  - Validation of ticket and flight data from the database  
  - Token generation and session handling  
  - Error handling for invalid credentials  
  - Logout and session persistence logic  
- It also connects directly with the notification system for flight alerts, which adds integration complexity.

Overall, this is a **moderately complex** story with **backend integration** and **security considerations**, which justifies 5 points.

#### Work Breakdown
- Create `/login` endpoint in backend (Flask)
- Add JWT-based token authentication middleware
- Front-end login screen (React Native)
- Session persistence and logout handling

#### Risks and Uncertainties
- Anyone with a valid ticket number could access extra features.  
  This might raise **privacy and cost concerns** if external users use system resources.
- Risk of token leakage or unauthorized access if not secured properly.

**Mitigation:**  
We plan to:
- Limit what data can be viewed even after login (no personal info).
- Add token expiration (24 hours).
- Consider adding OTP or additional validation later if needed.

---

### 2. Arrivals Page – 3 Story Points

**User Story:**  
> As a user, I want to track incoming flights and see specific flight details.

#### Why 3 points?
- Mostly **data retrieval and UI updates**.  
- Backend endpoint `/flights/arrivals` fetches and filters data.
- Includes some refresh and notification logic, but it reuses existing infrastructure.

#### Work Breakdown
- Build backend endpoint `/flights/arrivals`
- Create React Native page to display flights (flight number, time, gate, status)
- Implement auto-refresh every 30 seconds
- Add manual refresh button
- Add notification toggle per flight

#### Risks and Uncertainties
- Frequent refreshes may increase server load.  
- Push notifications for gate changes may occasionally fail if user unsubscribes or loses connection.

**Mitigation:**  
- Use lightweight database queries.  
- Cache flight data when possible.  
- Reconnect notification service automatically when network returns.

---

### 3. Departures Page – 3 Story Points

**User Story:**  
> As a user, I want to track outgoing flights and receive real-time updates.

#### Why 3 points?
- Similar structure and effort as arrivals page.  
- Only difference is data filtering (`departures` instead of `arrivals`).

#### Work Breakdown
- Implement `/flights/departures` endpoint
- UI with flight number, destination, time, status, gate
- Auto-refresh and manual refresh logic
- Notification toggle per flight

#### Risks and Uncertainties
- Data inconsistency if flight schedule changes frequently.
- Need to keep arrival/departure pages in sync with backend schema.

**Mitigation:**  
- Centralize backend data model for flights.  
- Use unified API response format to reduce maintenance overhead.

---

## ⚠️ Overall Project Risks

| Risk | Description | Impact | Mitigation |
|------|--------------|---------|-------------|
| **Unauthorized access** | Anyone with a valid ticket number might log in and use app features. | Medium | Limit feature scope and session duration. |
| **Data refresh load** | Auto-refreshing flight lists every 30 seconds increases DB calls. | Low | Use caching or polling intervals dynamically. |
| **Notification delivery** | Push notifications may fail for users offline or without permissions. | Low | Retry mechanism and token revalidation. |
| **Client changes** | Requirements can shift (like guest login). | Medium | Keep backlog flexible and estimate buffer points. |

---

## 📊 Workload Summary

| Feature | Story Points | Work Type | Dependencies |
|----------|---------------|------------|---------------|
| Passenger Login | 5 | Backend + Frontend + Auth | DB connection, JWT |
| Arrivals Page | 3 | Backend + UI | Flight data model |
| Departures Page | 3 | Backend + UI | Flight data model |
| Guest Login (new) | 2 | Backend update + Frontend flow | Based on client feedback |

Total = **13 Story Points**

---

## 🧠 Lessons Learned

- Keep **login and authorization logic flexible** for future changes.
- Implement **feature toggles** early for client-specific access control.
- Always confirm client requirements about data visibility (guest vs passenger) before starting development.
- Involve backend and frontend together when estimating story points — small UI changes can add hidden backend work.

---

## ✅ Conclusion

During this sprint, the team focused on building core backend endpoints and integrating them with the mobile app interface.  
The introduction of **guest login** improved user accessibility while maintaining passenger-only features behind authentication.  

The planned work is balanced in complexity — login being the highest effort area due to security and integration needs.  
Risks were identified early, and the team has clear mitigation steps to handle them.

Overall, the system is now well-structured to expand with new features like airport navigation, shops, and parking integration in upcoming iterations.

---

*(End of Report)*

---

