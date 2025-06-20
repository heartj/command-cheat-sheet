# groupdel Command

Delete a group

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-f` | Force deletion even if group is primary for users |

## Examples
1. **Run command**:
```bash
groupdel developers
```
Output: Deletes the developers group

2. **Run command**:
```bash
groupdel -f staff
```
Output: Forcefully deletes the staff group


## Notes
- Requires `sudo` to execute.
- Cannot delete primary group of an existing user.

## References
- [man groupdel](https://man7.org/linux/man-pages/man8/groupdel.8.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)