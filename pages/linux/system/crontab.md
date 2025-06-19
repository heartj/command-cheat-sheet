# crontab Command

Manage user crontab files for scheduling tasks

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-e` | Edit the user's crontab file |
| `-l` | List the user's crontab file |
| `-r` | Remove the user's crontab file |
| `-u <user>` | Specify the user for crontab operations (e.g., -u alice) |

## Examples
1. **Run command**:
```bash
crontab -e
```
Output: Opens the crontab file in the default editor to add tasks

2. **Run command**:
```bash
crontab -l
```
Output: Shows scheduled tasks for the current user


## Notes
- Requires `sudo` for other users' crontabs.
- Test scripts before scheduling to prevent errors.

## References
- [man crontab](https://man7.org/linux/man-pages/man1/crontab.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)