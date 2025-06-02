# Linux `sudo` Command

The `sudo` command allows users to execute commands with superuser (root) privileges or as another user, based on permissions defined in `/etc/sudoers`.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-u <user>` | Run as specific user | `sudo -u john ls` (Run `ls` as `john`) |
| `-i` | Start an interactive shell | `sudo -i` (Start root shell) |
| `-s` | Start a shell as root | `sudo -s` (Start root shell) |
| `-l` | List allowed commands | `sudo -l` (Show user’s sudo permissions) |
| `-k` | Invalidate cached credentials | `sudo -k` (Force password prompt) |
| `-e` | Edit files with root privileges | `sudo -e /etc/hosts` (Edit `/etc/hosts`) |

## Examples
1. **Run a command as root**:  
   `sudo apt update`  
   Updates package lists with root privileges.
2. **Start a root shell**:  
   `sudo -i`  
   Opens an interactive root shell.
3. **Run command as another user**:  
   `sudo -u john touch /home/john/file.txt`  
   Creates `file.txt` as `john`.
4. **Check sudo permissions**:  
   `sudo -l`  
   Lists commands the user can run with `sudo`.

## Notes
- Requires configuration in `/etc/sudoers` (edit with `visudo`).
- Use `-k` to force password re-entry for security.
- Be cautious, as `sudo` grants powerful access.

## References
- [man sudo](https://man7.org/linux/man-pages/man8/sudo.8.html)
- [sudoers Manual](https://www.sudo.ws/man/sudoers.man.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
