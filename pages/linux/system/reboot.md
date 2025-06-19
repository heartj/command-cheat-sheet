# reboot Command

The `reboot` command restarts the system immediately or after a specified delay. It is used to apply updates, recover from issues, or reset system state.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `--halt` | Halt the system instead of rebooting |
| `-f` | Force immediate reboot (bypasses systemd) |
| `--reboot` | Explicitly specify reboot (default behavior) |
| `-p` | Power off after reboot (equivalent to shutdown) |

## Examples

1. **Reboot the system immediately**:
   ```bash
   sudo reboot
   ```
   Output: Initiates a system restart, closing all processes.

2. **Force reboot (emergency use)**:
   ```bash
   sudo reboot -f
   ```
   Output: Reboots without graceful shutdown, use with caution.

## Notes
- Requires root privileges (`sudo`).
- Ensure critical processes are saved before rebooting to avoid data loss.
- Use `systemctl reboot` for systemd-based systems for better integration.

## References
- [man reboot](https://man7.org/linux/man-pages/man8/reboot.8.html)
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)