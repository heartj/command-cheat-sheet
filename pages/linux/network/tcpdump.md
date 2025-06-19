# Linux `tcpdump` Command

The `tcpdump` command captures and analyzes network packets on a specified interface. It is a powerful tool for troubleshooting network issues and inspecting traffic in real time.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-i <interface>` | Capture packets on specific interface | `tcpdump -i eth0` (Capture on `eth0`) |
| `-c <count>` | Capture a specific number of packets | `tcpdump -c 10` (Capture 10 packets) |
| `-w <file>` | Write packets to a file | `tcpdump -w capture.pcap` (Save to `capture.pcap`) |
| `-r <file>` | Read packets from a file | `tcpdump -r capture.pcap` (Read from `capture.pcap`) |
| `-n` | Show numerical addresses (no DNS) | `tcpdump -n` (Use IPs instead of hostnames) |
| `-v` | Verbose output | `tcpdump -v` (Show detailed packet info) |
| `<filter>` | Filter packets by expression | `tcpdump host 8.8.8.8` (Capture packets to/from 8.8.8.8) |

## Examples
1. **Capture packets on an interface**:  
   `tcpdump -i eth0`  
   Captures all packets on `eth0` until stopped (`Ctrl+C`).
2. **Save packets to a file**:  
   `tcpdump -i eth0 -c 100 -w capture.pcap`  
   Captures 100 packets on `eth0` and saves to `capture.pcap`.
3. **Filter HTTP traffic**:  
   `tcpdump -i eth0 port 80`  
   Captures packets on port 80 (HTTP).
4. **Read captured packets**:  
   `tcpdump -r capture.pcap`  
   Displays packets from `capture.pcap`.

## Notes
- Requires root privileges (e.g., `sudo tcpdump`).
- Use Wireshark to analyze `.pcap` files saved with `-w`.
- Be cautious with large captures, as they can consume significant disk space.

## References
- [tcpdump Manual](https://www.tcpdump.org/manpages/tcpdump.8.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
