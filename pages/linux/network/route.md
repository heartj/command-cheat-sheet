# route Command

Display or manipulate the IP routing table

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n` | Show numerical addresses |
| `add` | Add a new route |
| `del` | Delete a route |
| `-F` | Display FIB routing table |

## Examples
1. **Run command**:
```bash
route -n
```
Output: Shows the routing table with numerical addresses

2. **Run command**:
```bash
route add default gw 192.168.1.1
```
Output: Adds a default gateway via 192.168.1.1


## Notes
- Deprecated in favor of `ip route`.
- Requires `sudo` for modifications.

## References
- [man route](https://man7.org/linux/man-pages/man8/route.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)