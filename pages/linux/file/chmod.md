# chmod Command

Change file permissions

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-R` | Apply recursively to directories |
| `-v` | Verbose output, show changes |
| `755` | Set permissions to rwxr-xr-x |

## Examples
1. **Run command**:
```bash
chmod 755 script.sh
```
Output: Sets script.sh to rwxr-xr-x

2. **Run command**:
```bash
chmod -R u+w /docs
```
Output: Adds write permission for user to /docs recursively


## Notes
- Numeric mode: r=4, w=2, x=1 (e.g., 755 = rwxr-xr-x)
- Symbolic mode: u=user, g=group, o=others

## References
- [man chmod](https://man7.org/linux/man-pages/man1/chmod.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)