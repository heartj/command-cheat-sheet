# jobs Command

List active jobs in the current shell session

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | Show detailed information, including PIDs |
| `-p` | Show only PIDs of jobs |
| `-r` | Show only running jobs |

## Examples
1. **Run command**:
```bash
jobs
```
Output: Lists jobs with their status (e.g., `[1]+ Running sleep 100 &`)

2. **Run command**:
```bash
jobs -l
```
Output: Shows jobs with PIDs and detailed status


## Notes
- Works in interactive shells like bash.
- Use `bg` or `fg` to manage listed jobs.

## References
- [man jobs](https://man7.org/linux/man-pages/man1/jobs.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)