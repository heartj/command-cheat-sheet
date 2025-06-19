# shutdown Command

Schedule system shutdown or reboot

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-h` | Halt or power off after shutdown |
| `-r` | Reboot after shutdown |
| `-c` | Cancel a scheduled shutdown |
| `--show` | Show pending shutdown status |

## Examples
1. **Run command**:
```bash
sudo shutdown -h now
```
Output: Powers off the system immediately

2. **Run command**:
```bash
sudo shutdown -r +10
```
Output: Reboots in 10 minutes with a warning broadcast


## Notes
- Requires `sudo`.
- Use `-c` to cancel a scheduled shutdown.

## References
- [man shutdown](https://man7.org/linux/man-pages/man8/shutdown.8.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)