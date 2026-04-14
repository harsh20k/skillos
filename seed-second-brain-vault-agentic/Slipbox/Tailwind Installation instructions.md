---
creation date: 2025-10-16 11:39
tags: [concept]
dg-publish: true
---
Perfect! You've completed the installation. Now follow these remaining steps in order:

## Step 1: Configure tailwind.config.js

Open the `tailwind.config.js` file that was just created and replace its contents with:

```javascript
module.exports = {
  content: [
    "./app/**/*.{js,jsx,ts,tsx}",
    "./components/**/*.{js,jsx,ts,tsx}"
  ],
  presets: [require("nativewind/preset")],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## Step 2: Create global.css

Create a new file called `global.css` in your project root with this content:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

You can create it with this command:
```bash
echo '@tailwind base;
@tailwind components;
@tailwind utilities;' > global.css
```

## Step 3: Generate metro.config.js

```bash
npx expo customize metro.config.js
```

Then open `metro.config.js` and replace its contents with:

```javascript
const { getDefaultConfig } = require('expo/metro-config');
const { withNativeWind } = require('nativewind/metro');

const config = getDefaultConfig(__dirname);

module.exports = withNativeWind(config, { input: './global.css' });
```

## Step 4: Add TypeScript Support

Create `nativewind-env.d.ts` file in your root:

```bash
echo '/// <reference types="nativewind/types" />' > nativewind-env.d.ts
```

## Step 5: Import CSS in Root Layout

Open `app/_layout.tsx` and add this line **at the very top** (before all other imports):

```typescript
import "../global.css";
```

## Step 6: Install Axios (While You're At It)

```bash
npm install axios
```

## Step 7: Restart Your Dev Server

Stop any running dev server (Ctrl+C) and restart with cache cleared:

```bash
npx expo start -c
```

## Step 8: Test It Works

Edit `app/(tabs)/index.tsx` and replace the content to test:

```typescript
import "../global.css";
import { View, Text } from 'react-native';

export default function HomeScreen() {
  return (
    <View className="flex-1 items-center justify-center bg-blue-50">
      <Text className="text-3xl font-bold text-blue-600">
        ✅ NativeWind Working!
      </Text>
    </View>
  );
}
```

## Step 9: Commit Everything

Once you see the styled blue text:

```bash
git add .
git commit -m "Setup NativeWind and Axios - minimal starter configuration"
git push -u origin harshp
```

## Quick Checklist

- ✅ `tailwind.config.js` configured with content paths
- ✅ `global.css` created with Tailwind directives
- ✅ `metro.config.js` generated and configured
- ✅ `nativewind-env.d.ts` created
- ✅ `app/_layout.tsx` imports `global.css`
- ✅ Dev server restarted with `-c` flag

That's it! You now have a clean, minimal React Native Expo setup with NativeWind styling and Axios ready for API calls.

Sources

