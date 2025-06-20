# uniq Command

Remove or report duplicate lines

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-c` | Count occurrences of each line |
| `-i` | Ignore case |
| `-u` | Show only unique lines |

## Examples
1. **Run command**:
```bash
sort file.txt | uniq
```
Output: Removes duplicate lines from sorted file.txt

2. **Run command**:
```bash
uniq -c data.txt
```
Output: Counts occurrences of each line in data.txt


## Notes
- Requires sorted input for proper duplicate removal.
- Often used after `sort`.

## References
- [man uniq](https://man7.org/linux/man-pages/man1/uniq.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)