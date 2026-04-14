---
title: Rename Git branch
category: General
priority: Medium
starred: None
created: 2025-12-04T11:21:50.150390
updated: 2025-12-04T12:24:27.250565
dg-publish: true
---
# Rename Git branch

**Priority:** Medium

## Conversation

### Assistant

Netplan files differ by Ubuntu version and VirtualBox image. They are usually found in:

```
/etc/netplan/
```

Run:

```
ls /etc/netplan
```

You will likely see one of these:

### Common filenames
- `00-installer-config.yaml`
- `01-netcfg.yaml`
- `01-network-manager-all.yaml`
- `50-cloud-init.yaml`
- `99_config.yaml`

Use whichever `.yaml` file exists.

Example:

```
sudo nano /etc/netplan/00-installer-config.yaml
```

or

```
sudo nano /etc/netplan/50-cloud-init.yaml
```

After edits:

```
sudo netplan apply
```

If you paste your `ls /etc/netplan` output, I can tell you the exact file to edit and what to put inside.

---

