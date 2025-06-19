# who Command

Show currently logged-in users

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-a` | Display all information, including system boot time |
| `-u` | Show idle time for each user |
| `-b` | Show last system boot time |
| `-H` | Display column headers |
| `-q` | Show only usernames and user count |

## Examples
1. **Run command**:
```bash
who
```
Output: Shows username, terminal, and login time (e.g., `alice pts/0 2023-06-01 10:00`)

2. **Run command**:
```bash
who -aH
```
Output: Detailed table with boot time, users, and idle status


## Notes
- No root privileges required.
- Combine with `w` for detailed session info.

## References
- [man who](https://man7.org/linux/man-pages/man1/who.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)