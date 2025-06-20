# ping Command

Test network connectivity by sending ICMP echo requests

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-c <count>` | Specify number of packets to send (e.g., -c 4) |
| `-i <interval>` | Set interval between packets in seconds |
| `-s <size>` | Set packet size in bytes |
| `-t <ttl>` | Set time-to-live for packets |

## Examples
1. **Run command**:
```bash
ping -c 4 google.com
```
Output: Sends 4 packets to `google.com`, shows round-trip times

2. **Run command**:
```bash
ping -i 0.5 example.com
```
Output: Sends packets every 0.5 seconds to `example.com`


## Notes
- Requires `sudo` for some options (e.g., `-s`).
- High latency or packet loss indicates network issues.

## References
- [man ping](https://man7.org/linux/man-pages/man8/ping.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)