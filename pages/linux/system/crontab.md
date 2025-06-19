# crontab Command

The `crontab` command manages user crontab files, allowing scheduling of recurring tasks or scripts.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-e` | Edit the user's crontab file |
| `-l` | List the user's crontab file |
| `-r` | Remove the user's crontab file |
| `-u <user>` | Specify a user (e.g., `-u john`) |

## Examples

1. **Edit crontab to schedule a task**:
   ```bash
   crontab -e
   ```
   Output: Opens the crontab file in the default editor to add tasks (e.g., `0 0 * * * /backup.sh`).

2. **List current crontab**:
   ```bash
   crontab -l
   ```
   Output: Shows scheduled tasks for the current user.

## Notes
- Requires `sudo` for other users' crontabs (`-u`).
- Ensure correct syntax to avoid silent failures (use `man 5 crontab`).
- Test scripts before scheduling to prevent errors.

## References
- [man crontab](https://man7.org/linux/man-pages/man1/crontab.1.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)