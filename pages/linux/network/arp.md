# Linux `arp` Command

The `arp` command manages and displays the Address Resolution Protocol (ARP) cache, which maps IP addresses to MAC addresses for devices on a local network. It is used to troubleshoot network connectivity and manage ARP entries.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-n` | Show numerical addresses (no DNS resolution) | `arp -n` (Display IPs instead of hostnames) |
| `-a` | Display ARP cache (BSD-style output) | `arp -a` (List ARP table entries) |
| `-d <address>` | Delete an ARP entry | `arp -d 192.168.1.100` (Remove entry for `192.168.1.100`) |
| `-s <address> <mac>` | Set a static ARP entry | `arp -s 192.168.1.100 00:11:22:33:44:55` (Add static entry) |
| `-i <interface>` | Specify network interface | `arp -i eth0` (Show ARP for `eth0`) |
| `-v` | Verbose output | `arp -v` (Show detailed ARP table) |

## Examples
1. **Display ARP cache**:  
   `arp -a`  
   Shows the ARP table with IP-to-MAC mappings.
2. **Show ARP for specific interface**:  
   `arp -i eth0 -n`  
   Lists ARP entries for `eth0` with numerical IPs.
3. **Delete an ARP entry**:  
   `arp -d 192.168.1.100`  
   Removes the ARP entry for `192.168.1.100`.
4. **Add a static ARP entry**:  
   `arp -s 192.168.1.200 00:11:22:33:44:55`  
   Sets a static mapping for `192.168.1.200`.

## Notes
- Requires root privileges for modifying ARP entries (e.g., `sudo arp -s`).
- Use `ip neigh` as a modern alternative for managing ARP tables.
- Combine with `grep` to filter entries, e.g., `arp -a | grep 192.168.1`.

## References
- [man arp](https://man7.org/linux/man-pages/man8/arp.8.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
