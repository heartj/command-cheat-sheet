# Linux `chage` Command

The `chage` command manages user password and account expiration policies in a Linux system. It is used to set or modify password aging parameters and account expiry dates for user accounts.

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-m <days>` | Set minimum password age | `chage -m 7 john` (Require password change every 7 days) |
| `-M <days>` | Set maximum password age | `chage -M 90 john` (Password expires after 90 days) |
| `-d <date>` | Set last password change date | `chage -d 2025-01-01 john` (Set last change to Jan 1, 2025) |
| `-E <date>` | Set account expiration date | `chage -E 2025-12-31 john` (Account expires on Dec 31, 2025) |
| `-I <days>` | Set inactive days after password expiry | `chage -I 10 john` (Disable account 10 days after expiry) |
| `-l` | List password aging info | `chage -l john` (Show `john`’s password policy) |
| `-W <days>` | Set warning days before expiry | `chage -W 7 john` (Warn 7 days before password expiry) |

## Examples
1. **Set password expiration policy**:  
   `sudo chage -M 90 -m 7 -W 7 john`  
   Sets `john`’s password to expire every 90 days, with a minimum of 7 days between changes and a 7-day warning.
2. **Set account expiration date**:  
   `sudo chage -E 2025-12-31 john`  
   Makes `john`’s account expire on December 31, 2025.
3. **View user’s password policy**:  
   `sudo chage -l john`  
   Displays `john`’s password aging and account expiration details.
4. **Force immediate password change**:  
   `sudo chage -d 0 john`  
   Forces `john` to change their password at next login.

## Notes
- Requires root privileges (`sudo`).
- Password aging info is stored in `/etc/shadow`.
- Use with `passwd` to enforce strong password policies.
- Be cautious with `-E`, as it can lock users out after the expiry date.

## References
- [man chage](https://man7.org/linux/man-pages/man1/chage.1.html)

[Back to User Commands](../user.md) | [Back to Main Index](../../README.md)
