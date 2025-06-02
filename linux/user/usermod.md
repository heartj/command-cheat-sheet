# Linux `usermod` Command

The `usermod` command modifies attributes of an existing user account, such as home directory, shell, or group memberships.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-d <dir>` | Change home directory | `usermod -d /newhome/john john` (Change home directory) |
| `-m` | Move home directory contents | `usermod -m -d /newhome/john john` (Move contents) |
| `-s <shell>` | Change login shell | `usermod -s /bin/zsh john` (Set zsh as shell) |
| `-g <group>` | Change primary group | `usermod -g developers john` (Change primary group) |
| `-G <groups>` | Change secondary groups | `usermod -G wheel sudo john` (Set secondary groups) |
| `-l <newname>` | Change username | `usermod -l john_doe john` (Rename to `john_doe`) |

## Examples
1. **Change a user's shell**:  
   `sudo usermod -s /bin/bash john`  
   Sets `bash` as the login shell for `john`.
2. **Move and change home directory**:  
   `sudo usermod -m -d /home/john_doe john`  
   Moves `john`’s home directory to `/home/john_doe`.
3. **Add user to groups**:  
   `sudo usermod -aG developers,wheel john`  
   Adds `john` to `developers` and `wheel` groups (`-a` appends).
4. **Rename a user**:  
   `sudo usermod -l john_doe john`  
   Renames user `john` to `john_doe`.

## Notes
- Requires root privileges (`sudo`).
- Use `-a` with `-G` to append groups, otherwise existing groups are overwritten.
- Changes may affect running sessions; users may need to log out/in.

## References
- [man usermod](https://man7.org/linux/man-pages/man8/usermod.8.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
