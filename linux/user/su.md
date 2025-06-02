# Linux `su` Command

The `su` command switches to another user account, typically root, by starting a new shell with the target user’s privileges.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-` | Start a login shell | `su - john` (Switch to `john` with login shell) |
| `-c <command>` | Run a single command | `su -c "ls /root" root` (Run `ls /root` as root) |
| `<username>` | Switch to specific user | `su john` (Switch to `john`) |

## Examples
1. **Switch to root**:  
   `su -`  
   Switches to root with a login shell, loading root’s environment.
2. **Switch to another user**:  
   `su - john`  
   Switches to `john` with their environment.
3. **Run a command as root**:  
   `su -c "apt update" root`  
   Runs `apt update` as root.
4. **Switch without login shell**:  
   `su john`  
   Switches to `john` without loading their full environment.

## Notes
- Requires the target user’s password (unlike `sudo`).
- Use `-` for a full login shell to load the user’s environment.
- `sudo -i` or `sudo -s` is often preferred over `su` for root access.

## References
- [man su](https://man7.org/linux/man-pages/man1/su.1.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
