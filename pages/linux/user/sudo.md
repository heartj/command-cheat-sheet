# sudo Command

Execute commands as another user (typically root)

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-u <user>` | Run as specified user |
| `-i` | Run an interactive login shell |
| `-s` | Run a shell as the target user |

## Examples
1. **Run command**:
```bash
sudo apt update
```
Output: Runs apt update as root

2. **Run command**:
```bash
sudo -u bob whoami
```
Output: Prints bob as the effective user


## Notes
- Requires user to be in sudoers file.
- Use `visudo` to edit sudoers safely.

## References
- [man sudo](https://man7.org/linux/man-pages/man8/sudo.8.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)