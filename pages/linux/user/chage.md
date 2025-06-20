# chage Command

Change user password expiry information

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | List password expiry details |
| `-E <date>` | Set account expiration date (e.g., -E 2025-12-31) |
| `-m <days>` | Set minimum days between password changes |
| `-M <days>` | Set maximum days before password change |

## Examples
1. **Run command**:
```bash
chage -l alice
```
Output: Shows password expiry details for alice

2. **Run command**:
```bash
chage -M 90 bob
```
Output: Sets bob’s password to expire after 90 days

3. **Run command**:
```bash
chage -E 2025-12-31 alice
```
Output: Sets alice’s account to expire on 2025-12-31


## Notes
- Requires `sudo` to execute.
- Useful for managing account security policies.

## References
- [man chage](https://man7.org/linux/man-pages/man1/chage.1.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)