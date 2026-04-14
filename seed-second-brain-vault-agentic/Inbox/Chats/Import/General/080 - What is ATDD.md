---
title: What is ATDD
category: General
priority: Medium
starred: None
created: 2025-10-28T09:43:38.151744
updated: 2025-10-28T09:54:18.638558
dg-publish: true
---
# What is ATDD

**Priority:** Medium

## Conversation

### Assistant

Here’s a summary of the key concepts from the article **“TDD Testing Patterns”** by entity["people", "Victor Elizalde", 0]. citeturn0view0

---

### Patterns covered  
1. **Child Test**  
   - If a test becomes too big, stop and ask “why did it grow so large?” citeturn0view0  
   - Delete the large test and replace it with smaller “child” tests. citeturn0view0  
   - Goal: ensure each test is quick to make green, and changes per test are minimal. citeturn0view0  

2. **Mock Object**  
   - Use fake (in-memory) versions of slow or complex resources (e.g., database) rather than the real thing. citeturn0view0  
   - Benefits: faster tests, more readable test context, decoupling from actual infrastructure. citeturn0view0  

3. **Self Shunt and Log String**  
   - *Self Shunt*: Replace the object your code expects with the test itself (via an interface) so you observe interactions. citeturn0view0  
   - *Log String*: When you want to verify the order or content of notifications/interactions, you log them via your test implementation of the interface. citeturn0view0  

4. **Crash Test Dummy**  
   - Similar to a mock object but specifically designed to *raise an error* scenario you don’t want to build out fully (e.g., system full). citeturn0view0  
   - Makes testing error handling simpler without heavy setup.  

5. **Broken Test (at session end)**  
   - At the end of a coding session you write a test that fails (intentionally) and leave it failing. citeturn0view0  
   - Purpose: capture where you left off, help you resume with context.  

6. **Clean Check-in (team environment)**  
   - When working in a team, you should **not** leave any failing tests at check-in. citeturn0view0  
   - Two strategies:  
     - Delete the work that caused the test to fail (so you check-in all green). citeturn0view0  
     - Allow a short fix attempt; if it doesn’t succeed quickly, revert to green state. citeturn0view0  

---

### Key takeaways  
- Testing isn’t just about getting green bars; it’s about structuring tests so they remain **fast**, **readable**, and **maintainable**.  
- Large monolithic tests conceal design smells — breaking them into smaller tests increases clarity.  
- Fake resources (mocks, shunts) help isolate code under test and avoid external dependencies slowing or confusing tests.  
- Testing the unhappy path (via Crash Test Dummy) is as important as testing the happy path.  
- In solo development you can leave a “broken test” overnight to pick up where you left off; in team settings you must keep the repository in a clean, passing state at all times (Clean Check-in).  
- The patterns help enforce the core principle of entity["book", "Test-Driven Development by Example", 0] (by entity["people", "Kent Beck", 0]) of small incremental changes and tests guiding design. citeturn0view0  

---

If you like, I can pull **specific code-snippets or examples** from the article and provide them (or adapt them) for your context.

---

