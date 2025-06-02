# Linux `netstat` Command

The `netstat` command displays network connections, routing tables, and interface statistics. It is used to monitor network activity and troubleshoot connectivity issues.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-a` | Show all connections (including listening) | `netstat -a` (List all connections) |
| `-t` | Show TCP connections | `netstat -t` (List TCP connections) |
| `-u` | Show UDP connections | `netstat -u` (List UDP connections) |
| `-n` | Show numerical addresses (no DNS resolution) | `netstat -an` (Show IPs, not hostnames) |
| `-p` | Show program name and PID | `netstat -ap` (Show associated programs) |
| `-r` | Display routing table | `netstat -r` (Show routing information) |
| `-i` | Display network interfaces | `netstat -i` (List interfaces) |

## Examples
1. **List all active connections**:  
   `netstat -an`  
   Shows all connections with numerical addresses.
2. **Show TCP listening ports**:  
   `netstat -tln`  
   Lists TCP ports in listening state with numerical addresses.
3. **Identify program using a port**:  
   `netstat -tunap | grep :80`  
   Shows programs using port 80.
4. **Display routing table**:  
   `netstat -r`  
   Shows the kernel routing table.

## Notes
- May require root privileges for `-p` to show all programs.
- On modern systems, consider `ss` as a faster alternative.
- Use with `grep` or `awk` to filter output, e.g., `netstat -an | grep ESTABLISHED`.

## References
- [man netstat](https://man7.org/linux/man-pages/man8/netstat.8.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
