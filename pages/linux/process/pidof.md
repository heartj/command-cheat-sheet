# pidof Command

Find the process ID of a running program

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-s` | Return a single PID |
| `-x` | Include scripts (e.g., shell scripts) |
| `-o <pid>` | Omit specified PID |

## Examples
1. **Run command**:
```bash
pidof nginx
```
Output: Returns PIDs of all `nginx` processes (e.g., 1234 5678)

2. **Run command**:
```bash
pidof -s firefox
```
Output: Returns a single PID for `firefox`


## Notes
- Useful for scripting with `kill` or `pkill`.
- May return multiple PIDs for multi-process programs.

## References
- [man pidof](https://man7.org/linux/man-pages/man8/pidof.8.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)