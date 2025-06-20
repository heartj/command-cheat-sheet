# nice Command

Set the priority of a new process

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n <value>` | Specify the nice value (e.g., -n 10, range -20 to 19) |
| `--adjustment=<value>` | Same as -n, set the nice value |

## Examples
1. **Run command**:
```bash
nice -n 10 tar -czf backup.tar.gz /data
```
Output: Runs `tar` with lower priority (nice value 10)

2. **Run command**:
```bash
nice -n -5 python script.py
```
Output: Runs `script.py` with higher priority (nice value -5)


## Notes
- Lower nice values (e.g., -20) increase priority; higher values (e.g., 19) decrease it.
- Requires `sudo` for negative nice values.

## References
- [man nice](https://man7.org/linux/man-pages/man1/nice.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)