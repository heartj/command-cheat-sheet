# su Command

Switch to another user or root

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | Start a login shell |
| `-c <command>` | Execute a single command |

## Examples
1. **Run command**:
```bash
su - alice
```
Output: Switches to user alice with login shell

2. **Run command**:
```bash
su -c "whoami" bob
```
Output: Runs whoami as user bob


## Notes
- Requires target user’s password.
- Use `sudo -i` for root without password prompt.

## References
- [man su](https://man7.org/linux/man-pages/man1/su.1.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)