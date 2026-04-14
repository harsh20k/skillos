---
title: Write comments in Bash
category: Projects
priority: Medium
starred: None
created: 2025-10-16T09:55:38.447053
updated: 2025-10-16T11:02:26.750429
dg-publish: true
---
# Write comments in Bash

**Priority:** Medium

## Conversation

### Assistant

In **React Native**, **Redux** is a **state management library** that helps you manage and organize the data (or “state”) of your app in a predictable, centralized way — especially when your app becomes complex and has many components sharing or updating data.

---

### 🧠 The Core Idea

In React (and React Native), components have their own internal state and can share data via props.  
But when the app grows, passing data between many components can get messy — this is where **Redux** helps.

Redux provides:
- **One central store** for all your app’s state.
- **A predictable flow** for how data changes.

---

### ⚙️ The Three Core Principles of Redux

1. **Single Source of Truth**  
   All your app’s state lives in a single **store** (a plain JavaScript object).

2. **State is Read-Only**  
   You can’t directly change the state.  
   You must **dispatch an action** (an object that describes *what happened*).

3. **Changes are Made with Pure Functions (Reducers)**  
   A **reducer** takes the current state and an action, and returns a **new state**.

---

### 🧩 Redux Flow Diagram

```
Component (UI)
   ↓ dispatches
Action  → describes what happened
   ↓ handled by
Reducer → updates the state
   ↓
Store → holds the global state
   ↓
Component (UI re-renders)
```

---

### 🛠 Example

#### 1. Install Redux libraries
```bash
npm install @reduxjs/toolkit react-redux
```

#### 2. Create a store

```js
// store.js
import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './counterSlice';

export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
});
```

#### 3. Create a slice (state + reducers)

```js
// counterSlice.js
import { createSlice } from '@reduxjs/toolkit';

export const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1 },
    decrement: (state) => { state.value -= 1 },
  },
});

export const { increment, decrement } = counterSlice.actions;
export default counterSlice.reducer;
```

#### 4. Connect Redux to your app

```js
// App.js
import React from 'react';
import { Provider } from 'react-redux';
import { store } from './store';
import CounterScreen from './CounterScreen';

export default function App() {
  return (
    <Provider store={store}>
      <CounterScreen />
    </Provider>
  );
}
```

#### 5. Use Redux in a component

```js
// CounterScreen.js
import React from 'react';
import { View, Text, Button } from 'react-native';
import { useSelector, useDispatch } from 'react-redux';
import { increment, decrement } from './counterSlice';

export default function CounterScreen() {
  const count = useSelector((state) => state.counter.value);
  const dispatch = useDispatch();

  return (
    <View>
      <Text>Count: {count}</Text>
      <Button title="+" onPress={() => dispatch(increment())} />
      <Button title="-" onPress={() => dispatch(decrement())} />
    </View>
  );
}
```

---

### 🚀 Why Use Redux in React Native?

✅ Helps manage **complex global state** (auth, user data, theme, etc.)  
✅ Makes debugging easier (predictable flow)  
✅ Encourages cleaner and more testable code  
✅ Works across React (web) and React Native (mobile)

---

Would you like me to explain **when to use Redux vs React Context** (so you don’t overcomplicate your app)?

---

