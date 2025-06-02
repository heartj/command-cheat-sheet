# Linux `groupadd` Command

The `groupadd` command creates a new group in a Linux system, which can be assigned to users for access control.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-g <gid>` | Specify group ID | `groupadd -g 1001 developers` (Create group with GID 1001) |
| `-r` | Create a system group | `groupadd -r sysgroup` (Create system group) |
| `-f` | Force creation (ignore existing group) | `groupadd -f developers` (Force create group) |

## Examples
1. **Create a new group**:  
   `sudo groupadd developers`  
   Creates group `developers` with an auto-assigned GID.
2. **Create a system group**:  
   `sudo groupadd -r sysgroup`  
   Creates a system group with a low GID.
3. **Create a group with specific GID**:  
   `sudo groupadd -g 1001 developers`  
   Creates `developers` with GID 1001.
4. **Force create a group**:  
   `sudo groupadd -f developers`  
   Creates `developers` even if it exists.

## Notes
- Requires root privileges (`sudo`).
- Group info is stored in `/etc/group` and `/etc/gshadow`.
- Use `usermod -aG` to add users to the group.

## References
- [man groupadd](https://man7.org/linux/man-pages/man8/groupadd.8.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
