# Linux `ifconfig` Command

The `ifconfig` command displays or configures network interfaces. It is a legacy tool for managing network settings, often replaced by `ip` on modern systems, but still widely used on older distributions.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `<interface>` | Display specific interface | `ifconfig eth0` (Show `eth0` details) |
| `up` | Activate a network interface | `ifconfig eth0 up` (Enable `eth0`) |
| `down` | Deactivate a network interface | `ifconfig eth0 down` (Disable `eth0`) |
| `<ip> netmask <mask>` | Set IP address and subnet mask | `ifconfig eth0 192.168.1.100 netmask 255.255.255.0` (Set IP and mask) |
| `-a` | Show all interfaces (including inactive) | `ifconfig -a` (List all interfaces) |
| `mtu <size>` | Set MTU (Maximum Transmission Unit) | `ifconfig eth0 mtu 1500` (Set MTU to 1500) |

## Examples
1. **Display all interfaces**:  
   `ifconfig -a`  
   Shows all network interfaces, including inactive ones.
2. **Configure an IP address**:  
   `ifconfig eth0 192.168.1.10 netmask 255.255.255.0`  
   Assigns IP `192.168.1.10` to `eth0`.
3. **Enable an interface**:  
   `ifconfig wlan0 up`  
   Activates the `wlan0` wireless interface.
4. **Check interface status**:  
   `ifconfig eth0 | grep "inet "`  
   Shows IP address and network details for `eth0`.

## Notes
- Requires root privileges for configuration changes (e.g., `sudo ifconfig eth0 up`).
- `ifconfig` is deprecated on many modern Linux distributions; consider `ip` for newer systems.
- Use `ip addr` as a modern alternative for viewing interface details.

## References
- [man ifconfig](https://man7.org/linux/man-pages/man8/ifconfig.8.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
