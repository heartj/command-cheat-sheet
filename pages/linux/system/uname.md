# uname Command

Display system information (OS, kernel, architecture)

[Back to System Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-a` | Display all system information |
| `-r` | Show kernel release version |
| `-m` | Show machine hardware name (e.g., x86_64) |
| `-n` | Show network node hostname |
| `-s` | Show kernel name (e.g., Linux) |

## Examples
1. **Run command**:
```bash
uname -a
```
Output: Shows `Linux hostname 5.15.0-73-generic x86_64 GNU/Linux`

2. **Run command**:
```bash
uname -r
```
Output: Displays `5.15.0-73-generic`


## Notes
- No root privileges required.
- Useful for scripting system detection.

## References
- [man uname](https://man7.org/linux/man-pages/man1/uname.1.html)

[Back to System Commands](../index.md) | [Back to Main Index](../../README.md)