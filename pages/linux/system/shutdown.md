# shutdown Command

The `shutdown` command schedules a system shutdown or restart, allowing a grace period for users to save work.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-h` | Halt or power off after shutdown |
| `-r` | Reboot after shutdown |
| `<time>` | Specify shutdown time (e.g., `now`, `+5` for 5 minutes) |
| `-c` | Cancel a pending shutdown |

## Examples

1. **Shut down immediately**:
   ```bash
   sudo shutdown -h now
   ```
   Output: Powers off the system immediately.

2. **Schedule reboot in 10 minutes**:
   ```bash
   sudo shutdown -r +10
   ```
   Output: Broadcasts a warning and reboots in 10 minutes.

## Notes
- Requires `sudo`.
- Use `-c` to cancel a scheduled shutdown.
- Ensure critical processes are saved to avoid data loss.

## References
- [man shutdown](https://man7.org/linux/man-pages/man8/shutdown.8.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)