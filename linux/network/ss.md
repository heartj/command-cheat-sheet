# Linux `ss` Command

The `ss` command displays socket statistics, providing information about network connections, similar to `netstat` but faster and more modern. It is used to monitor TCP, UDP, and Unix sockets.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-t` | Show TCP sockets | `ss -t` (List TCP connections) |
| `-u` | Show UDP sockets | `ss -u` (List UDP connections) |
| `-l` | Show listening sockets | `ss -l` (List listening ports) |
| `-n` | Show numerical addresses (no DNS) | `ss -tn` (Show TCP with IPs) |
| `-p` | Show associated processes | `ss -tp` (Show programs using sockets) |
| `-a` | Show all sockets (connected and listening) | `ss -a` (List all sockets) |
| `-s` | Show summary statistics | `ss -s` (Show socket summary) |

## Examples
1. **List all TCP connections**:  
   `ss -tn`  
   Shows TCP connections with numerical addresses.
2. **Show listening ports**:  
   `ss -tln`  
   Lists TCP ports in listening state.
3. **Identify process using a port**:  
   `ss -tp | grep :80`  
   Shows processes using port 80.
4. **Show socket summary**:  
   `ss -s`  
   Displays total socket statistics.

## Notes
- Requires root privileges for `-p` to show all processes.
- Faster than `netstat` due to direct kernel access.
- Use with `grep` or `awk` to filter output, e.g., `ss -tn | grep ESTAB`.

## References
- [man ss](https://man7.org/linux/man-pages/man8/ss.8.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
