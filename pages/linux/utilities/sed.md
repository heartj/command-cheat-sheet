# sed Command

Stream editor for text transformation

[Back to Utilities Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-i` | Edit files in-place |
| `-e <script>` | Specify a script to execute |
| `-n` | Suppress automatic printing |

## Examples
1. **Run command**:
```bash
sed 's/old/new/g' file.txt
```
Output: Replaces all "old" with "new" in file.txt

2. **Run command**:
```bash
sed -i 's/error/warning/' log.txt
```
Output: Replaces "error" with "warning" in log.txt in-place

3. **Run command**:
```bash
sed -n '10,20p' file.txt
```
Output: Prints lines 10 to 20 from file.txt


## Notes
- Use `sed -i.bak` to create a backup.
- Common for batch text edits.

## References
- [man sed](https://man7.org/linux/man-pages/man1/sed.1.html)

[Back to Utilities Commands](../index.md) | [Back to Main Index](../../README.md)