# Linux `ping` Command

The `ping` command tests network connectivity by sending ICMP echo requests to a host and measuring response times. It is used to diagnose network reachability and latency.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-c <count>` | Send a specific number of packets | `ping -c 4 google.com` (Send 4 packets) |
| `-i <interval>` | Set interval between packets (seconds) | `ping -i 0.5 google.com` (Send every 0.5s) |
| `-s <size>` | Set packet size (bytes) | `ping -s 100 google.com` (Send 100-byte packets) |
| `-t <ttl>` | Set time-to-live for packets | `ping -t 64 google.com` (Set TTL to 64) |
| `-q` | Quiet mode (show only summary) | `ping -q -c 4 google.com` (Show summary only) |
| `-W <timeout>` | Wait time for response (seconds) | `ping -W 2 google.com` (Wait 2s per packet) |

## Examples
1. **Basic ping test**:  
   `ping google.com`  
   Sends continuous pings to `google.com` until stopped (`Ctrl+C`).
2. **Send limited pings**:  
   `ping -c 5 8.8.8.8`  
   Sends 5 pings to Google’s DNS server.
3. **Adjust packet size**:  
   `ping -s 500 localhost`  
   Sends 500-byte packets to `localhost`.
4. **Quiet ping with summary**:  
   `ping -q -c 10 example.com`  
   Sends 10 pings and shows only the summary.

## Notes
- Requires root privileges for some options (e.g., `-s`, `-f` for flood ping).
- Use `Ctrl+C` to stop continuous pings.
- Firewalls may block ICMP, causing “unreachable” errors even if the host is up.

## References
- [man ping](https://man7.org/linux/man-pages/man8/ping.8.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
