# Expo EAS — Client Sharing & Push Notification Testing Flow

## Overview
EAS (Expo Application Services) provides a streamlined way to build, share, and test React Native apps — including full push notification support — without going through the App Store.

---

## Methods

### 1. EAS Update (OTA — Fastest)
For JavaScript/UI-only changes:
```bash
eas update --branch preview --message "Client review build"
```
- Client opens via **Expo Go** or a preview URL
- No reinstall needed for subsequent JS updates

### 2. EAS Build — Internal Distribution (Recommended for clients)
```bash
eas build --profile preview --platform all
```
- Generates a **shareable install link** from the Expo dashboard
- Client installs directly (no App Store required)
- ✅ Push notifications work fully
- **Android:** Seamless APK download
- **iOS:** Requires client's UDID added to provisioning profile (one-time setup)

### 3. EAS Submit — App Store / Play Store
```bash
eas submit --platform ios
```
- For final UAT via **TestFlight** or **Google Play Internal Testing**

---

## Recommended Flow

```
Dev → eas build --profile preview → Share Expo dashboard link → Client installs
                    ↓ (JS-only changes)
              eas update → Client sees changes instantly (no reinstall)
```

---

## Push Notification Testing

| Method | Simulator | Real Push | Needs Credentials |
|---|---|---|---|
| Local Notifications | ✅ | ❌ | ❌ |
| Expo Push Tool | ❌ | ✅ | ✅ |
| EAS Build + Device | ❌ | ✅ | ✅ |

### Expo Push Tool
- Get token: `Notifications.getExpoPushTokenAsync()`
- Send test at: https://expo.dev/notifications

### Local Notifications (dev/simulator)
```js
await Notifications.scheduleNotificationAsync({
  content: { title: 'Test', body: 'Local notification' },
  trigger: { seconds: 2 },
});
```

---

## Notes
- `preview` profile in `eas.json` = production-like build, internally distributed
- iOS APNs credentials + Android `google-services.json` required for real push
- Physical device required for real push notifications
