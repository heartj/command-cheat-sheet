# passwd Command

Change user password

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | Lock the password |
| `-u` | Unlock the password |
| `-d` | Delete the password (empty) |

## Examples
1. **Run command**:
```bash
passwd alice
```
Output: Prompts to set a new password for alice

2. **Run command**:
```bash
passwd -l bob
```
Output: Locks bob’s password


## Notes
- Requires `sudo` for other users.
- Passwords are stored in /etc/shadow.

## References
- [man passwd](https://man7.org/linux/man-pages/man1/passwd.1.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)