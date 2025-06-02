# Linux `id` Command

The `id` command displays a user’s UID, GID, and group memberships.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-u` | Show only UID | `id -u john` (Show `john`’s UID) |
| `-g` | Show only primary GID | `id -g john` (Show `john`’s primary GID) |
| `-G` | Show all group IDs | `id -G john` (Show all GIDs for `john`) |
| `-n` | Show names instead of IDs | `id -ng john` (Show primary group name) |
| `<username>` | Show info for specific user | `id john` (Show `john`’s details) |

## Examples
1. **Show current user’s details**:  
   `id`  
   Displays UID, GID, and groups for the current user.
2. **Show another user’s details**:  
   `id john`  
   Shows `john`’s UID, GID, and groups.
3. **Show only UID**:  
   `id -u john`  
   Outputs `john`’s UID.
4. **Show group names**:  
   `id -nG john`  
   Lists names of all groups `john` belongs to.

## Notes
- No root privileges required for own user; `sudo` needed for others.
- Useful for scripting to verify user permissions.
- Group info is stored in `/etc/group`.

## References
- [man id](https://man7.org/linux/man-pages/man1/id.1.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
