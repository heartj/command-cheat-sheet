# groupadd Command

Create a new group

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-g <gid>` | Specify group ID |
| `-r` | Create a system group |
| `-f` | Force creation, exit successfully if group exists |

## Examples
1. **Run command**:
```bash
groupadd developers
```
Output: Creates a group named developers

2. **Run command**:
```bash
groupadd -g 1001 staff
```
Output: Creates group staff with GID 1001


## Notes
- Requires `sudo` to execute.
- Groups are stored in /etc/group.

## References
- [man groupadd](https://man7.org/linux/man-pages/man8/groupadd.8.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)