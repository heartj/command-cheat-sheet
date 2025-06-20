# ip Command

Manage network interfaces, routes, and addresses

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `addr` | Show or manage IP addresses |
| `link` | Show or manage network interfaces |
| `route` | Show or manage routing table |
| `-s` | Show detailed statistics |

## Examples
1. **Run command**:
```bash
ip addr show
```
Output: Lists all network interfaces with IP addresses

2. **Run command**:
```bash
ip route
```
Output: Displays the routing table

3. **Run command**:
```bash
ip link set eth0 up
```
Output: Enables the eth0 interface


## Notes
- Replaces `ifconfig` and `route` in modern systems.
- Requires `sudo` for configuration changes.

## References
- [man ip](https://man7.org/linux/man-pages/man8/ip.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)