---
creation date: 2026-01-14 10:40
tags: [concept]
---
## **Professional React Native Standards**
A practical linting + patterns + architecture “team contract” you can drop into a repo and enforce in CI.

---
# **1) Tooling baseline (mandatory)**
## **1.1 TypeScript**
Rules:
- No new .js in app code (except configs/scripts).
- strict: true.
- noImplicitAny: true.
- Prefer unknown over any.
- Domain types live near domain (not in a global “types” dump).
tsconfig.json (core ideas):
```
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitAny": true,
    "exactOptionalPropertyTypes": true
  }
}
```
## **1.2 ESLint + Prettier**
Use ESLint for correctness + architectural boundaries, Prettier for formatting.
Install:
- eslint
- @typescript-eslint/eslint-plugin, @typescript-eslint/parser
- eslint-config-prettier, eslint-plugin-prettier
- eslint-plugin-import
- eslint-plugin-react, eslint-plugin-react-hooks
- eslint-plugin-unused-imports
- eslint-plugin-simple-import-sort
- eslint-plugin-jest (if using Jest)
- eslint-plugin-testing-library (if using RTL)
.eslintrc.js (template):
```
module.exports = {
  root: true,
  env: { es2021: true },
  parser: '@typescript-eslint/parser',
  plugins: [
    '@typescript-eslint',
    'react',
    'react-hooks',
    'import',
    'unused-imports',
    'simple-import-sort',
  ],
  extends: [
    'eslint:recommended',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    'plugin:@typescript-eslint/recommended',
    'prettier',
  ],
  rules: {
    // Formatting handled by Prettier; ESLint handles correctness & structure
    'react/react-in-jsx-scope': 'off',
    // Imports
    'unused-imports/no-unused-imports': 'error',
    'simple-import-sort/imports': 'error',
    'simple-import-sort/exports': 'error',
    // TS safety
    '@typescript-eslint/no-explicit-any': 'error',
    '@typescript-eslint/consistent-type-imports': 'error',
    '@typescript-eslint/no-floating-promises': 'error',
    // React rules
    'react-hooks/exhaustive-deps': 'error',
    // Prefer named exports for non-screen modules (optional)
    'import/prefer-default-export': 'off',
  },
  settings: { react: { version: 'detect' } },
};
```
.prettierrc:
```
{
  "singleQuote": true,
  "trailingComma": "all",
  "printWidth": 100
}
```
## **1.3 Git hooks: Husky + lint-staged**
- Block bad code before it hits CI.
lint-staged:
```
{
  "*.{ts,tsx,js,jsx}": ["eslint --fix", "prettier --write"],
  "*.{json,md,yml,yaml}": ["prettier --write"]
}
```
## **1.4 Commit rules (optional but common)**
- Conventional commits + commitlint to keep change history clean.
---
# **2) Architectural rules (team-wide)**
## **2.1 Layered architecture (simple + enforceable)**
Pick a small set of layers and do not violate them:
**UI Layer**
- screens
- components (presentational)
- navigation
**Application Layer**
- hooks (screen logic)
- state (store)
- use-cases (business operations)
**Domain Layer**
- entities/types
- pure business rules
- validation (pure)
**Data Layer**
- API client
- repositories (data access)
- persistence (storage/cache)
**Rule: dependencies only point downward**
- UI → Application → Domain → Data (or UI → App → Data for simpler apps)
- Domain never imports from UI, navigation, storage, react-native, etc.
## **2.2 Feature-first folder structure**
Avoid “utils dumping ground”. Prefer feature modules.
Example:
```
src/
  app/                 # app bootstrap, providers, navigation root
  features/
    timer/
      ui/              # screens/components for this feature
      hooks/
      domain/
      data/
      index.ts
    auth/
    profile/
  shared/
    ui/                # reusable UI primitives (Button, Input, etc.)
    hooks/
    domain/
    data/
    config/
    utils/
```
**Rule:** shared code must be truly cross-feature. If only one feature uses it, keep it inside that feature.
## **2.3 Module boundaries (enforce with ESLint)**
Use path aliases and restrict imports.
tsconfig.json paths:
```
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@app/*": ["src/app/*"],
      "@features/*": ["src/features/*"],
      "@shared/*": ["src/shared/*"]
    }
  }
}
```
Then add ESLint boundary rules (one practical approach uses import/no-restricted-paths):
```
// in rules:
'import/no-restricted-paths': [
  'error',
  {
    zones: [
      {
        target: './src/shared',
        from: './src/features',
        message: 'Shared must not import from features.'
      },
      {
        target: './src/features/**/domain',
        from: ['./src/features/**/ui', './src/features/**/data', './src/shared/**'],
        message: 'Domain must stay pure; do not import UI/data/shared UI directly.'
      }
    ]
  }
]
```
(Adjust zones to match your exact structure.)

---
# **3) Strict coding patterns (what “good RN” looks like)**
## **3.1 Components: Presentational vs Container**
**Presentational (UI-only)**
- Pure props in, UI out
- No networking, no storage, no navigation, no timers
**Container (screen / hook)**
- Orchestrates data fetching, state transitions, navigation actions
- Calls use-cases / repositories
**Rule:** screens must be thin—prefer a useXxxScreen() hook for logic.
## **3.2 Hooks rules**
- One hook = one responsibility (timer, fetch profile, etc.)
- Hooks return a stable API: { state, actions }
- Never export raw setState from hooks.
Example shape:
```
return {
  state: { remainingSeconds, isRunning },
  actions: { start, pause, reset, setMinutes },
};
```
## **3.3 State management rules**
Pick one:
- Small apps: React state + hooks
- Medium/large: Zustand / Redux Toolkit (RTK) / MobX (choose one)
Rules if using a store:
- Store contains serializable state only.
- Side effects go in thunks/sagas/use-cases, not in reducers.
- State changes are via actions only (no direct mutation outside store layer).
## **3.4 Networking + data access**
- No fetch/axios inside screens/components.
- Use an API client + repository layer.
Example:
- data/apiClient.ts
- data/userRepository.ts
- application/useCases/fetchUser.ts
## **3.5 Error handling standard**
- All async boundaries must handle:
    - loading
    - error (typed)
    - empty state
- Standardize error shape:
```
type AppError =
  | { kind: 'Network'; message: string }
  | { kind: 'Auth'; message: string }
  | { kind: 'Validation'; message: string }
  | { kind: 'Unknown'; message: string };
```
## **3.6 Styling standards**
Choose one:
- StyleSheet.create + theme tokens
- Tailwind RN (NativeWind)
- Restyle
Rules (if StyleSheet):
- No hardcoded colors in feature screens; use theme tokens.
- Spacing uses scale (4, 8, 12, 16…)
- Avoid “magic numbers” for layout.
## **3.7 Navigation rules**
- Navigation types live in one place (TypeScript).
- Screens do not deep-link-string-litter. Use typed routes.
## **3.8 Testing pyramid**
- Unit: domain + pure functions (fast, lots)
- Integration: repositories/use-cases (moderate)
- UI: React Native Testing Library for key flows (few)
- E2E: Detox (critical paths only)
Rules:
- No snapshots for complex screens (brittle). Prefer behavior assertions.
---
# **4) CI enforcement (non-negotiable)**
In CI, run:
- yarn lint (eslint)
- yarn typecheck (tsc –noEmit)
- yarn test
- optional: yarn test:e2e on nightly / main
Example package.json scripts:
```
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx",
    "typecheck": "tsc --noEmit",
    "test": "jest"
  }
}
```
---
# **5) “Red flags” rules (ban list)**
- any (unless isolated to a 3rd-party typing workaround, documented)
- Networking inside UI components
- “utils” folder growing without ownership
- Cross-feature imports (feature A importing feature B internals)
- useEffect doing business logic without a dedicated hook/use-case
- Timers/intervals sprinkled in screens without encapsulation
---
# **6) Optional: add a measurable “definition of clean”**
A PR is acceptable only if:
- ESLint/Prettier/Typecheck pass
- Feature boundaries respected
- New code is typed
- Tests exist for domain/use-case changes
- Screens remain thin (logic extracted)
---
If you want, paste your current RN repo structure (top-level src/ tree) and I’ll rewrite these rules into an exact, enforceable version for your project (including import/no-restricted-paths zones that match your folders and a ready-to-copy ESLint config).