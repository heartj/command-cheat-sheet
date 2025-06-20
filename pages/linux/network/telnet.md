# telnet Command

Connect to a remote host on a specified port

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-a` | Attempt automatic login |
| `-l <user>` | Specify user for login |
| `-r` | Emulate rlogin behavior |

## Examples
1. **Run command**:
```bash
telnet example.com 80
```
Output: Connects to `example.com` on port 80

2. **Run command**:
```bash
telnet -l alice 192.168.1.100 23
```
Output: Attempts to connect as `alice` to port 23


## Notes
- Insecure; use `ssh` for secure connections.
- Useful for testing port connectivity.

## References
- [man telnet](https://man7.org/linux/man-pages/man1/telnet.1.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)