# Linux `traceroute` Command

The `traceroute` command traces the route packets take to a network host, showing each hop along the path. It is used to diagnose network routing issues.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-n` | Show numerical IP addresses (no DNS) | `traceroute -n google.com` (Show IPs only) |
| `-m <max_hops>` | Set maximum number of hops | `traceroute -m 15 example.com` (Limit to 15 hops) |
| `-w <sec>` | Set timeout per hop (seconds) | `traceroute -w 3 google.com` (3s timeout per hop) |
| `-q <num>` | Set number of queries per hop | `traceroute -q 1 example.com` (Send 1 probe per hop) |
| `-I` | Use ICMP instead of UDP | `traceroute -I google.com` (Use ICMP packets) |
| `-T` | Use TCP instead of UDP | `traceroute -T example.com` (Use TCP packets) |

## Examples
1. **Trace route to a host**:  
   `traceroute google.com`  
   Shows each hop to `google.com` with latency.
2. **Use numerical IPs**:  
   `traceroute -n 8.8.8.8`  
   Traces route to Google’s DNS server without resolving names.
3. **Limit hops**:  
   `traceroute -m 10 example.com`  
   Stops after 10 hops.
4. **Use ICMP probes**:  
   `traceroute -I google.com`  
   Uses ICMP packets for tracing.

## Notes
- Requires root privileges for some options (e.g., `-I`, `-T`).
- Firewalls may block probes, causing `*` in output for unreachable hops.
- Use `mtr` for a real-time, interactive alternative to `traceroute`.

## References
- [man traceroute](https://man7.org/linux/man-pages/man8/traceroute.8.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
