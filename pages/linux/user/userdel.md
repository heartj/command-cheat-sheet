# Linux `userdel` Command

The `userdel` command deletes a user account and optionally its home directory and mail spool.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-r` | Remove home directory and mail spool | `userdel -r john` (Delete `john` and home directory) |
| `-f` | Force deletion (even if logged in) | `userdel -f john` (Force delete `john`) |
| `-Z` | Remove SELinux user mapping | `userdel -Z john` (Remove SELinux mapping) |

## Examples
1. **Delete a user without removing home directory**:  
   `sudo userdel john`  
   Removes user `john` but keeps `/home/john`.
2. **Delete a user and home directory**:  
   `sudo userdel -r john`  
   Removes `john` and deletes `/home/john`.
3. **Force delete a logged-in user**:  
   `sudo userdel -f -r john`  
   Forces deletion of `john` and removes home directory.
4. **Remove SELinux mapping**:  
   `sudo userdel -Z john`  
   Deletes `john` and its SELinux user mapping.

## Notes
- Requires root privileges (`sudo`).
- Use `-r` cautiously, as it permanently deletes user data.
- Check `/etc/passwd` and `/etc/shadow` to verify deletion.

## References
- [man userdel](https://man7.org/linux/man-pages/man8/userdel.8.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
