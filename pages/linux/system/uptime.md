# uptime Command

The `uptime` command shows how long the system has been running, the number of logged-in users, and the system load averages for the past 1, 5, and 15 minutes.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-p` | Display uptime in a pretty format (e.g., "2 days, 3 hours") |
| `-s` | Show the system start time |
| `-V` | Display version information |

## Examples

1. **Display system uptime and load averages**:
   ```bash
   uptime
   ```
   Output: `12:00:00 up 2 days,  3:15,  1 user,  load average: 0.25, 0.30, 0.35`

2. **Show uptime in human-readable format**:
   ```bash
   uptime -p
   ```
   Output: `up 2 days, 3 hours, 15 minutes`

## Notes
- Load averages indicate system demand; values above CPU core count suggest high load.
- Combine with `w` or `who` for detailed user information.
- No root privileges required.

## References
- [man uptime](https://man7.org/linux/man-pages/man1/uptime.1.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)