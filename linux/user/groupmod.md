# Linux `groupmod` Command

The `groupmod` command modifies attributes of an existing group, such as its name or group ID.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-n <newname>` | Change group name | `groupmod -n devs developers` (Rename to `devs`) |
| `-g <gid>` | Change group ID | `groupmod -g 1002 developers` (Change GID to 1002) |
| `-o` | Allow non-unique GID | `groupmod -o -g 1001 developers` (Allow duplicate GID) |

## Examples
1. **Rename a group**:  
   `sudo groupmod -n devs developers`  
   Renames group `developers` to `devs`.
2. **Change a group’s GID**:  
   `sudo groupmod -g 1002 developers`  
   Changes GID of `developers` to 1002.
3. **Allow non-unique GID**:  
   `sudo groupmod -o -g 1001 developers`  
   Sets `developers` to share GID 1001.
4. **Verify changes**:  
   `grep devs /etc/group`  
   Checks updated group info.

## Notes
- Requires root privileges (`sudo`).
- Changes affect files owned by the group; update permissions if needed.
- Check `/etc/group` to verify modifications.

## References
- [man groupmod](https://man7.org/linux/man-pages/man8/groupmod.8.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
