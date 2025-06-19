# hostnamectl Command

The `hostnamectl` command manages the system hostname and related settings, such as transient and static hostnames.

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `set-hostname <name>` | Set the system hostname |
| `status` | Show current hostname and related info |
| `--transient` | Set transient hostname only |
| `--static` | Set static hostname only |

## Examples

1. **Set a new hostname**:
   ```bash
   sudo hostnamectl set-hostname server1
   ```
   Output: Changes the hostname to `server1`.

2. **Check hostname status**:
   ```bash
   hostnamectl status
   ```
   Output: Shows static, transient, and pretty hostnames.

## Notes
- Requires `sudo` to modify hostnames.
- Update `/etc/hosts` if needed to reflect hostname changes.
- Reboot may be required for some changes to take effect.

## References
- [man hostnamectl](https://man7.org/linux/man-pages/man1/hostnamectl.1.html)
- [systemd Documentation](https://www.freedesktop.org/wiki/Software/systemd/)

[Back to System Commands](../system.md) | [Back to Main Index](../../README.md)