# Linux `useradd` Command

The `useradd` command creates a new user account in a Linux system. It is used by administrators to set up user accounts with specific home directories, shells, and group memberships.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-m` | Create a home directory | `useradd -m john` (Create home directory for `john`) |
| `-d <dir>` | Specify home directory | `useradd -d /home/john john` (Set custom home directory) |
| `-s <shell>` | Specify login shell | `useradd -s /bin/zsh john` (Set zsh as shell) |
| `-g <group>` | Specify primary group | `useradd -g developers john` (Set primary group to `developers`) |
| `-G <groups>` | Add to secondary groups | `useradd -G wheel sudo john` (Add to `wheel` and `sudo`) |
| `-u <uid>` | Specify user ID | `useradd -u 1001 john` (Set UID to 1001) |

## Examples
1. **Create a user with default settings**:  
   `sudo useradd -m john`  
   Creates user `john` with a home directory in `/home/john`.
2. **Create a user with custom shell and groups**:  
   `sudo useradd -m -s /bin/bash -G developers,wheel john`  
   Creates `john` with bash shell and adds to `developers` and `wheel` groups.
3. **Create a system user without home directory**:  
   `sudo useradd -r -s /bin/false service`  
   Creates a system user `service` with no login.
4. **Specify custom UID and home directory**:  
   `sudo useradd -u 1001 -d /data/john john`  
   Creates `john` with UID 1001 and home directory `/data/john`.

## Notes
- Requires root privileges (`sudo`).
- Use `passwd` after `useradd` to set a password.
- Default settings are defined in `/etc/default/useradd` and `/etc/login.defs`.

## References
- [man useradd](https://man7.org/linux/man-pages/man8/useradd.8.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
