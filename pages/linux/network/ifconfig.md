# ifconfig Command

Configure and display network interfaces

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-a` | Show all interfaces, including inactive ones |
| `<interface> up` | Activate a network interface |
| `<interface> down` | Deactivate a network interface |
| `<interface> <address>` | Assign an IP address to an interface |

## Examples
1. **Run command**:
```bash
ifconfig -a
```
Output: Shows all network interfaces and their details

2. **Run command**:
```bash
ifconfig eth0 192.168.1.100
```
Output: Assigns IP address 192.168.1.100 to eth0


## Notes
- Deprecated in favor of `ip` in modern systems.
- Requires `sudo` for configuration changes.

## References
- [man ifconfig](https://man7.org/linux/man-pages/man8/ifconfig.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)