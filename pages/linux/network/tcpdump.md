# tcpdump Command

Capture and analyze network packets

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-i <interface>` | Specify interface to capture (e.g., -i eth0) |
| `-w <file>` | Save packets to a file |
| `-c <count>` | Capture a specific number of packets |
| `-n` | Show numerical addresses |

## Examples
1. **Run command**:
```bash
tcpdump -i eth0
```
Output: Captures packets on the eth0 interface

2. **Run command**:
```bash
tcpdump -c 10 -w capture.pcap
```
Output: Captures 10 packets and saves to `capture.pcap`

3. **Run command**:
```bash
tcpdump -n port 80
```
Output: Captures packets on port 80 with numerical addresses


## Notes
- Requires `sudo` to capture packets.
- Use `wireshark` to analyze `.pcap` files.

## References
- [man tcpdump](https://man7.org/linux/man-pages/man8/tcpdump.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)