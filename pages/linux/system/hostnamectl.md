# hostnamectl Command

Manage system hostname and related settings

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `set-hostname <name>` | Set the system hostname |
| `status` | Show current hostname and related info |
| `set-icon-name <name>` | Set the system icon name |
| `set-chassis <type>` | Set the chassis type (e.g., server, laptop) |

## Examples
1. **Run command**:
```bash
sudo hostnamectl set-hostname server1
```
Output: Changes the hostname to `server1`

2. **Run command**:
```bash
hostnamectl status
```
Output: Shows static, transient, and pretty hostnames


## Notes
- Requires `sudo` to modify hostnames.
- Update `/etc/hosts` to reflect changes.

## References
- [man hostnamectl](https://man7.org/linux/man-pages/man1/hostnamectl.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)