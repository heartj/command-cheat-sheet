# ls Command

List directory contents

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-l` | Use long listing format |
| `-a` | Show hidden files |
| `-h` | Show human-readable file sizes |
| `-R` | List directories recursively |

## Examples
1. **Run command**:
```bash
ls -la
```
Output: Lists all files, including hidden, in long format

2. **Run command**:
```bash
ls -lh /var
```
Output: Lists /var contents with human-readable sizes

3. **Run command**:
```bash
ls -R ~/docs
```
Output: Recursively lists all files in ~/docs


## Notes
- Hidden files start with: .bashrc
- Combine flags (e.g., -lah) for multiple options

## References
- [man ls](https://man7.org/linux/man-pages/man1/ls.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)