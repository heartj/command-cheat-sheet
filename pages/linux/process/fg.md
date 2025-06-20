# fg Command

Bring a background job to the foreground

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `<job_id>` | Specify the job ID to bring to foreground (e.g., %1) |

## Examples
1. **Run command**:
```bash
fg %1
```
Output: Brings job 1 to the foreground

2. **Run command**:
```bash
fg
```
Output: Brings the most recent background job to the foreground


## Notes
- Use `jobs` to find job IDs.
- Ctrl+Z suspends a foreground job.

## References
- [man fg](https://man7.org/linux/man-pages/man1/fg.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)