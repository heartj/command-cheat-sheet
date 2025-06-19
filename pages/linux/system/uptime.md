# uptime Command

Show system uptime, user count, and load averages

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-p` | Display uptime in a human-readable format |
| `-s` | Show system start time |
| `-V` | Display version information |

## Examples
1. **Run command**:
```bash
uptime
```
Output: Shows uptime and load averages (e.g., `12:00:00 up 2 days, 3:15, 1 user`)

2. **Run command**:
```bash
uptime -p
```
Output: Displays `up 2 days, 3 hours, 15 minutes`


## Notes
- Load averages above CPU core count indicate high load.
- No root privileges required.

## References
- [man uptime](https://man7.org/linux/man-pages/man1/uptime.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)