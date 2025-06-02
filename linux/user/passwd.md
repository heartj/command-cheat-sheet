# Linux `passwd` Command

The `passwd` command changes a user’s password or manages password attributes.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-l` | Lock a user’s account | `passwd -l john` (Lock `john`’s account) |
| `-u` | Unlock a user’s account | `passwd -u john` (Unlock `john`’s account) |
| `-d` | Delete a user’s password | `passwd -d john` (Remove `john`’s password) |
| `-S` | Show account status | `passwd -S john` (Show `john`’s password status) |
| `<username>` | Change specific user’s password | `passwd john` (Change `john`’s password) |

## Examples
1. **Change own password**:  
   `passwd`  
   Prompts for a new password for the current user.
2. **Change another user’s password**:  
   `sudo passwd john`  
   Changes `john`’s password.
3. **Lock a user account**:  
   `sudo passwd -l john`  
   Locks `john`’s account, preventing login.
4. **Check password status**:  
   `sudo passwd -S john`  
   Shows whether `john`’s account is locked or has a password.

## Notes
- Requires root privileges for other users (`sudo`).
- Passwords are stored in `/etc/shadow`.
- Use strong passwords to enhance security.

## References
- [man passwd](https://man7.org/linux/man-pages/man1/passwd.1.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
