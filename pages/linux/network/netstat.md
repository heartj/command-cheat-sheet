# netstat Command

Display network connections, routing tables, and interface statistics

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-t` | Show TCP connections |
| `-u` | Show UDP connections |
| `-l` | Show listening sockets |
| `-n` | Show numerical addresses instead of hostnames |
| `-r` | Show routing table |

## Examples
1. **Run command**:
```bash
netstat -tuln
```
Output: Lists listening TCP and UDP ports with numerical addresses

2. **Run command**:
```bash
netstat -r
```
Output: Displays the kernel routing table

3. **Run command**:
```bash
netstat -an | grep ESTABLISHED
```
Output: Shows established network connections


## Notes
- May require `net-tools` package (`sudo apt install net-tools`).
- Replaced by `ss` in modern systems for some use cases.

## References
- [man netstat](https://man7.org/linux/man-pages/man8/netstat.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)