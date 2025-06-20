# sort Command

Sort lines of text

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-n` | Sort numerically |
| `-r` | Reverse sort order |
| `-k <field>` | Sort by specific field |
| `-u` | Remove duplicates |

## Examples
1. **Run command**:
```bash
sort file.txt
```
Output: Sorts lines in file.txt alphabetically

2. **Run command**:
```bash
sort -n numbers.txt
```
Output: Sorts numbers.txt numerically

3. **Run command**:
```bash
sort -k 2 -t "," data.csv
```
Output: Sorts data.csv by second field


## Notes
- Case-sensitive by default.
- Use with `uniq` to remove duplicates.

## References
- [man sort](https://man7.org/linux/man-pages/man1/sort.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)