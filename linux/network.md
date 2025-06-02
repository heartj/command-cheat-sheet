# Linux Network Commands

This page provides a quick reference for Linux commands related to network operations. These commands are essential for tasks like downloading files, testing connectivity, analyzing network traffic, and querying DNS. Each command has a dedicated page with detailed usage.

[Back to Main Index](../README.md)

## Commands

| Command | Purpose | Link |
|---------|---------|------|
| `curl` | Transfer data to or from a server (e.g., HTTP, FTP) | [Details](./network/curl.md) |
| `wget` | Download files from the web | [Details](./network/wget.md) |
| `ping` | Test network connectivity to a host | [Details](./network/ping.md) |
| `netstat` | Display network connections and statistics | [Details](./network/netstat.md) |
| `nslookup` | Query DNS for domain information | [Details](./network/nslookup.md) |
| `dig` | Advanced DNS lookup tool | [Details](./network/dig.md) |
| `traceroute` | Trace the route packets take to a host | [Details](./network/traceroute.md) |
| `ss` | Display socket statistics (modern `netstat` replacement) | [Details](./network/ss.md) |
| `ifconfig` | Display or configure network interfaces (legacy) | [Details](./network/ifconfig.md) |
| `ip` | Manage network interfaces, routes, and addresses | [Details](./network/ip.md) |
| `tcpdump` | Capture and analyze network packets | [Details](./network/tcpdump.md) |
| `arp` | Manage and display ARP cache (IP to MAC mapping) | [Details](./network/arp.md) |
| `nc` | Read/write data across network connections (TCP/UDP) | [Details](./network/nc.md) |

## References
- [curl Documentation](https://curl.se/docs/manpage.html)
- [wget Manual](https://www.gnu.org/software/wget/manual/wget.html)
- [man ping](https://man7.org/linux/man-pages/man8/ping.8.html)

## Notes
- Use `man <command>` (e.g., `man curl`) to view detailed documentation for any command.
- Some commands (e.g., `netstat`, `ifconfig`) may require installation on minimal systems.
- Root privileges may be needed for certain options (e.g., `tcpdump`, `arp -s`).

[Back to Main Index](../README.md)
