# who Command

The `who` command shows information about currently logged-in users, including their username, terminal, and login time.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-a` | Display all information, including system boot time |
| `-b` | Show last system boot time |
| `-u` | Show idle time for each user |
| `-H` | Display column headers |

## Examples

1. **List logged-in users**:
   ```bash
   who
   ```
   Output: Shows username, terminal, and login time (e.g., `alice pts/0 2023-06-01 10:00`).

2. **Show all details with headers**:
   ```bash
   who -aH
   ```
   Output: Detailed table with boot time, users, and idle status.

## Notes
- No root privileges required.
- Combine with `w` for more detailed session info.
- Useful for monitoring user activity on servers.

## References
- [man who](https://man7.org/linux/man-pages/man1/who.1.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)