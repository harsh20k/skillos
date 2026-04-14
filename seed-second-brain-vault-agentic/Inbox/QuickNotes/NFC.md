---
source: https://developer.android.com/develop/connectivity/nfc
tags:
  - "#inbox/fleetingNotes"
created: 2024-12-13
dg-publish: true
---
Near Field Communication (NFC) is a set of short-range wireless technologies, typically requiring a distance of 4 cm or less to initiate a connection. NFC lets you share small payloads of data between an NFC tag and an Android-powered device, or between two Android-powered devices.

Tags can range in complexity. Simple tags offer just read and write semantics, sometimes with one-time-programmable areas to make the card read-only. More complex tags offer math operations, and have cryptographic hardware to authenticate access to a sector. The most sophisticated tags contain operating environments, allowing complex interactions with code executing on the tag. The data stored in the tag can also be written in a variety of formats, but many of the Android framework APIs are based around a [NFC Forum](http://www.nfc-forum.org/) standard called NDEF (NFC Data Exchange Format).