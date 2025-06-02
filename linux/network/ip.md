# Linux `ip` Command

The `ip` command is a modern tool for managing network interfaces, addresses, routes, and other network configurations. It is part of the `iproute2` suite and replaces older tools like `ifconfig` and `route`.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `link show` | Display network interfaces | `ip link show` (List all interfaces) |
| `addr show` | Show IP addresses | `ip addr show` (List IP addresses) |
| `addr add` | Add IP address to interface | `ip addr add 192.168.1.100/24 dev eth0` (Add IP to `eth0`) |
| `link set <dev> up` | Activate an interface | `ip link set eth0 up` (Enable `eth0`) |
| `link set <dev> down` | Deactivate an interface | `ip link set eth0 down` (Disable `eth0`) |
| `route show` | Display routing table | `ip route show` (Show routing table) |
| `route add` | Add a route | `ip route add default via 192.168.1.1` (Set default gateway) |

## Examples
1. **List all interfaces**:  
   `ip link show`  
   Shows all network interfaces and their status.
2. **Assign an IP address**:  
   `ip addr add 192.168.1.100/24 dev eth0`  
   Assigns IP `192.168.1.100` with a /24 subnet to `eth0`.
3. **Add a default route**:  
   `ip route add default via 192.168.1.1`  
   Sets the default gateway to `192.168.1.1`.
4. **Show specific interface details**:  
   `ip addr show dev eth0`  
   Displays IP and status for `eth0`.

## Notes
- Requires root privileges for configuration changes (e.g., `sudo ip link set eth0 up`).
- Use `ip -s link` for interface statistics.
- `ip` is more powerful and flexible than `ifconfig` and `route`.

## References
- [man ip](https://man7.org/linux/man-pages/man8/ip.8.html)
- [iproute2 Documentation](https://www.kernel.org/doc/html/latest/networking/iproute2.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
