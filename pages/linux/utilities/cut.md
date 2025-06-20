# cut Command

Extract sections from lines of text

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-d <delimiter>` | Specify delimiter (e.g., -d ",") |
| `-f <fields>` | Select fields (e.g., -f 1,3) |
| `-c <characters>` | Select specific characters |

## Examples
1. **Run command**:
```bash
cut -d ":" -f 1 /etc/passwd
```
Output: Extracts usernames from /etc/passwd

2. **Run command**:
```bash
cut -c 1-10 file.txt
```
Output: Extracts first 10 characters of each line in file.txt


## Notes
- Simpler than `awk` for basic field extraction.
- Use with pipes (e.g., `ls -l | cut -d " " -f 1`).

## References
- [man cut](https://man7.org/linux/man-pages/man1/cut.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)