# Linux User Commands

This page provides a quick reference for Linux commands related to user account, group, permission, and password policy management. These commands are essential for creating, modifying, and managing user accounts, their access rights, and account expiration policies in a Linux environment. Each command has a dedicated page with detailed usage.

[Back to Main Index](../README.md)

## Commands

| Command | Purpose | Link |
|---------|---------|------|
| `useradd` | Add a new user account | [Details](./user/useradd.md) |
| `usermod` | Modify user account attributes | [Details](./user/usermod.md) |
| `userdel` | Delete a user account | [Details](./user/userdel.md) |
| `groupadd` | Add a new group | [Details](./user/groupadd.md) |
| `groupmod` | Modify group attributes | [Details](./user/groupmod.md) |
| `groupdel` | Delete a group | [Details](./user/groupdel.md) |
| `passwd` | Change a user's password | [Details](./user/passwd.md) |
| `id` | Display user and group IDs | [Details](./user/id.md) |
| `whoami` | Display the current username | [Details](./user/whoami.md) |
| `sudo` | Execute commands with superuser privileges | [Details](./user/sudo.md) |
| `su` | Switch to another user account | [Details](./user/su.md) |
| `chage` | Manage user password and account expiration policies | [Details](./user/chage.md) |

## References
- [GNU Coreutils Documentation](https://www.gnu.org/software/coreutils/manual/coreutils.html)
- [man useradd](https://man7.org/linux/man-pages/man8/useradd.8.html)
- [man sudo](https://man7.org/linux/man-pages/man8/sudo.8.html)

## Notes
- Use `man <command>` (e.g., `man useradd`) to view detailed documentation.
- Most commands require root privileges (e.g., `sudo useradd`).
- Be cautious with commands like `userdel` or `sudo`, as they can have significant effects.

[Back to Main Index](../README.md)