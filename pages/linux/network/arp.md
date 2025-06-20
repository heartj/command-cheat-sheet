# arp Command

Display or manipulate the ARP cache

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-a` | Show all ARP entries |
| `-d <address>` | Delete an ARP entry |
| `-s <address> <hwaddr>` | Add a static ARP entry |
| `-n` | Show numerical addresses |

## Examples
1. **Run command**:
```bash
arp -a
```
Output: Displays the ARP table with IP and MAC addresses

2. **Run command**:
```bash
arp -d 192.168.1.100
```
Output: Removes the ARP entry for 192.168.1.100


## Notes
- Requires `sudo` for modifying the ARP cache.
- Useful for troubleshooting LAN connectivity.

## References
- [man arp](https://man7.org/linux/man-pages/man8/arp.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)