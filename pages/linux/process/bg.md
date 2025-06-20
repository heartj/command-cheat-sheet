# bg Command

Resume a suspended job in the background

[Back to Process Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `<job_id>` | Specify the job ID to resume (e.g., %1) |

## Examples
1. **Run command**:
```bash
bg %1
```
Output: Resumes job 1 in the background

2. **Run command**:
```bash
bg
```
Output: Resumes the most recently suspended job


## Notes
- Use `jobs` to find job IDs.
- Suspended jobs are created with Ctrl+Z.

## References
- [man bg](https://man7.org/linux/man-pages/man1/bg.1.html)

[Back to Process Commands](../index.md) | [Back to Main Index](../../README.md)