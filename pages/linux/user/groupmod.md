# groupmod Command

Modify an existing group

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n <newname>` | Rename the group |
| `-g <gid>` | Change the group ID |

## Examples
1. **Run command**:
```bash
groupmod -n devteam developers
```
Output: Renames group developers to devteam

2. **Run command**:
```bash
groupmod -g 1002 staff
```
Output: Changes staff group’s GID to 1002


## Notes
- Requires `sudo` to execute.
- Verify GID availability before changing.

## References
- [man groupmod](https://man7.org/linux/man-pages/man8/groupmod.8.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)