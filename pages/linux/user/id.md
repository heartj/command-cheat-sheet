# id Command

Display user and group information

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-u` | Show user ID only |
| `-g` | Show primary group ID only |
| `-G` | Show all group IDs |
| `-n` | Show names instead of IDs |

## Examples
1. **Run command**:
```bash
id alice
```
Output: Shows UID, GID, and groups for alice

2. **Run command**:
```bash
id -u bob
```
Output: Shows bob’s user ID

3. **Run command**:
```bash
id -nG alice
```
Output: Shows names of all groups alice belongs to


## Notes
- Useful for verifying user permissions.
- No `sudo` needed for own user.

## References
- [man id](https://man7.org/linux/man-pages/man1/id.1.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)