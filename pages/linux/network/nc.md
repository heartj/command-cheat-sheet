# nc Command

Establish TCP or UDP connections for network testing

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | Listen for incoming connections |
| `-u` | Use UDP instead of TCP |
| `-p <port>` | Specify source port |
| `-v` | Verbose output |

## Examples
1. **Run command**:
```bash
nc -l 12345
```
Output: Listens for connections on port 12345

2. **Run command**:
```bash
nc 192.168.1.100 80
```
Output: Connects to port 80 on 192.168.1.100

3. **Run command**:
```bash
nc -u 8.8.8.8 53
```
Output: Sends UDP packets to port 53 on 8.8.8.8


## Notes
- Also known as `netcat`, a versatile networking tool.
- Use `Ctrl+C` to exit.

## References
- [man nc](https://man7.org/linux/man-pages/man1/nc.1.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)