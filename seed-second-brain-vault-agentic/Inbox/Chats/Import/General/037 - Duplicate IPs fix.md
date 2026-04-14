---
title: Duplicate IPs fix
category: General
priority: Medium
starred: None
created: 2025-12-02T11:26:05.980171
updated: 2025-12-02T11:31:06.843441
dg-publish: true
---
# Duplicate IPs fix

**Priority:** Medium

## Conversation

### Assistant

Good, this clarifies it.

For the two VMs you just showed:

```text
VM A enp0s9:
    link/ether 08:00:27:e2:93:ce

VM B enp0s9:
    link/ether 08:00:27:70:0d:51
```

The MAC addresses are **different**, so my earlier “same MAC” hypothesis is wrong.

However, both of their `ip -4 addr show` outputs have:

```text
enp0s9: ...
    inet 192.168.1.103/24 ... valid_lft forever preferred_lft forever
```

Notice:

- `10.0.2.15` on `enp0s8` is marked `dynamic` → from DHCP (NAT adapter).
- `192.168.1.103` on `enp0s9` is **not** marked `dynamic` → this is a **manually configured static IP** inside each VM.

So right now you have:

- Different MACs (fine).
- The **same static IP (`192.168.1.103`) manually assigned to enp0s9 on more than one VM** (not fine if they are on the same network).

That is why you are seeing:

```text
192.168.1.101
192.168.1.102
192.168.1.103
192.168.1.103   ← duplicate
```

Two VMs are simply configured to the same address.

---

## What this means in practice

If those VMs are on the same L2 network (same VirtualBox host-only/bridged network), you will get:

- ARP conflicts
- “flapping” connectivity (sometimes you hit VM1, sometimes VM2, or pings drop)

If they are on **different** host-only networks that both use `192.168.1.0/24`, then they are actually isolated and there is no real conflict, but from your perspective it looks confusing.

---

## How to fix it (pick one approach)

### Option 1: Give each VM a unique static IP on `enp0s9`

For example:

- VM1 → `192.168.1.101/24`
- VM2 → `192.168.1.102/24`
- VM3 → `192.168.1.103/24`

On each VM (Ubuntu with Netplan), your config file is typically in `/etc/netplan/*.yaml`, e.g. `/etc/netplan/01-netcfg.yaml` or `/etc/netplan/50-cloud-init.yaml`.

Example static config snippet (per VM, with different `addresses`):

```yaml
network:
  version: 2
  ethernets:
    enp0s9:
      dhcp4: no
      addresses:
        - 192.168.1.101/24   # change to .102, .103 on other VMs
      gateway4: 192.168.1.1   # if needed
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
```

Then apply:

```bash
sudo netplan apply
```

Check:

```bash
ip -4 addr show enp0s9
```

---

### Option 2: Let `enp0s9` use DHCP instead of static

If your VirtualBox network (bridged or host-only) has DHCP enabled and you don’t care about fixed IPs, turn DHCP on for `enp0s9` in the guest.

Netplan example:

```yaml
network:
  version: 2
  ethernets:
    enp0s9:
      dhcp4: yes
```

Apply:

```bash
sudo netplan apply
```

Temporarily, you can also do:

```bash
sudo ip addr flush dev enp0s9
sudo dhclient enp0s9
```

Then verify each VM gets a different `192.168.1.x` address.

---

## Quick sanity checklist

On each VM, you eventually want:

```bash
ip -4 addr show enp0s9
```

to show:

- VM1: `inet 192.168.1.101/24 ...`
- VM2: `inet 192.168.1.102/24 ...`
- VM3: `inet 192.168.1.103/24 ...`

with **no duplicates**.

If you paste the `/etc/netplan/*.yaml` for one VM, I can tell you exactly what to change line by line.

---

