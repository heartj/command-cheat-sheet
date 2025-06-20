# renice Command

Alter the priority of running processes

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n <value>` | Specify the new nice value (e.g., -n 10) |
| `-p <pid>` | Specify the process ID to adjust |
| `-u <user>` | Adjust all processes for a specific user |

## Examples
1. **Run command**:
```bash
renice 10 -p 1234
```
Output: Sets nice value to 10 for process with PID 1234

2. **Run command**:
```bash
renice -5 -u alice
```
Output: Sets nice value to -5 for all processes owned by `alice`


## Notes
- Requires `sudo` for negative nice values or other users' processes.
- Check current nice value with `ps` or `top`.

## References
- [man renice](https://man7.org/linux/man-pages/man1/renice.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)