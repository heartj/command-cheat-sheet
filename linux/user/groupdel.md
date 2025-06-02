# Linux `groupdel` Command

The `groupdel` command deletes an existing group from a Linux system.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| (none) | Delete the specified group | `groupdel developers` (Delete `developers`) |

## Examples
1. **Delete a group**:  
   `sudo groupdel developers`  
   Removes the `developers` group.
2. **Verify deletion**:  
   `grep developers /etc/group`  
   Confirms `developers` is removed.
3. **Delete a system group**:  
   `sudo groupdel sysgroup`  
   Removes the system group `sysgroup`.

## Notes
- Requires root privileges (`sudo`).
- Cannot delete a group if it is a user’s primary group; change the user’s group first.
- Check `/etc/group` to ensure deletion.

## References
- [man groupdel](https://man7.org/linux/man-pages/man8/groupdel.8.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
