# userdel Command

Delete a user account

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-r` | Remove the user's home directory and mail spool |
| `-f` | Force deletion even if user is logged in |

## Examples
1. **Run command**:
```bash
userdel alice
```
Output: Deletes user alice without removing home directory

2. **Run command**:
```bash
userdel -r bob
```
Output: Deletes user bob and their home directory


## Notes
- Requires `sudo` to execute.
- Check for running processes before deletion.

## References
- [man userdel](https://man7.org/linux/man-pages/man8/userdel.8.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)