# chown Command

Change file ownership

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-R` | Apply recursively to directories |
| `-v` | Verbose output, show changes |
| `<user>:<group>` | Specify owner and group |

## Examples
1. **Run command**:
```bash
chown alice file.txt
```
Output: Changes owner of file.txt to alice

2. **Run command**:
```bash
chown -R alice:staff /docs
```
Output: Changes owner and group of /docs recursively


## Notes
- Requires `sudo` for non-owned files
- Use `ls -l` to verify ownership

## References
- [man chown](https://man7.org/linux/man-pages/man1/chown.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)