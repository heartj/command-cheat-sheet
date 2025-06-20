# ss Command

Display socket statistics for network connections

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-t` | Show TCP sockets |
| `-u` | Show UDP sockets |
| `-l` | Show listening sockets |
| `-n` | Show numerical addresses |
| `-p` | Show process information |

## Examples
1. **Run command**:
```bash
ss -tuln
```
Output: Lists listening TCP and UDP ports with numerical addresses

2. **Run command**:
```bash
ss -tanp
```
Output: Shows TCP connections with process details

3. **Run command**:
```bash
ss -u
```
Output: Shows UDP sockets


## Notes
- Modern replacement for `netstat`.
- Faster and more detailed than `netstat`.

## References
- [man ss](https://man7.org/linux/man-pages/man8/ss.8.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)