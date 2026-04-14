---
title: See upstream git


category: General
priority: Medium
starred: None
created: 2025-12-10T08:45:50.313668
updated: 2025-12-10T09:17:10.584697
dg-publish: true
---
# See upstream git



**Priority:** Medium

## Conversation

### Assistant

To change the **IP address** of a VirtualBox VM, the method depends on how the VM’s network is configured. Here are the exact steps for all common cases.

---

# 1. Check the current network mode in VirtualBox
In VirtualBox Manager:

1. Select your VM  
2. Settings → **Network**  
3. Look at **Attached to:**  
   - NAT  
   - Bridged Adapter  
   - Host-only Adapter  
   - Internal Network  
   - NAT Network

Your ability to *change* the IP address depends on this mode.

---

# 2. If your VM is using **NAT**
You **cannot manually assign a public IP**.  
The VM always gets an IP like `10.0.2.15` (DHCP from VirtualBox).

If you want your VM to have a stable or custom IP, switch to **Bridged** or **Host-only**.

---

# 3. If your VM is using **Bridged Adapter**
Your VM behaves like a physical machine on your LAN.

To set static IP inside Ubuntu:

1. Edit Netplan config:

```sh
sudo nano /etc/netplan/01-netcfg.yaml
```

If this file doesn’t exist, it can be:

- `/etc/netplan/50-cloud-init.yaml`
- `/etc/netplan/00-installer-config.yaml`
- `/etc/netplan/01-network-manager-all.yaml`

Check with:

```sh
ls /etc/netplan/
```

2. Example static IP configuration:

```yaml
network:
  version: 2
  ethernets:
    enp0s3:
      dhcp4: no
      addresses: [192.168.1.50/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 1.1.1.1]
```

3. Apply changes:

```sh
sudo netplan apply
```

---

# 4. If your VM is using **Host-only Adapter**
VirtualBox runs DHCP on the host-only network.

To change IP inside VM:

```sh
sudo nano /etc/netplan/<filename>.yaml
```

Set static IP like:

```yaml
addresses: [192.168.56.10/24]
```

Apply:

```sh
sudo netplan apply
```

To change the **DHCP range** on the host:

VirtualBox → Preferences → Network → Host-only Networks → Edit

---

# 5. If using **NAT Network** (not NAT)
You *can* control the IP range.

1. VirtualBox → Tools → Network  
2. Select your **NAT Network** → Edit  
3. Change the network CIDR (e.g., `192.168.10.0/24`)

Restart VM; it receives a new DHCP IP.

---

# 6. Quick way to set a temporary IP (Linux)
This lasts until reboot:

```sh
sudo ip addr add 192.168.1.55/24 dev enp0s3
```

To remove:

```sh
sudo ip addr del 192.168.1.55/24 dev enp0s3
```

---

# Identify your netplan file
Run:

```sh
ls /etc/netplan
```

Tell me the filenames you see (e.g., `50-cloud-init.yaml`).  
I can give the exact edit for your system.

---

