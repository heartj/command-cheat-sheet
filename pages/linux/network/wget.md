# wget Command

Download files from the web

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-O <file>` | Save output to a specific file |
| `-c` | Resume a partially downloaded file |
| `-r` | Recursively download files |
| `-q` | Quiet mode, suppress output |

## Examples
1. **Run command**:
```bash
wget https://example.com/file.zip
```
Output: Downloads `file.zip` to the current directory

2. **Run command**:
```bash
wget -O custom.zip https://example.com/file.zip
```
Output: Saves the file as `custom.zip`

3. **Run command**:
```bash
wget -c https://example.com/largefile.iso
```
Output: Resumes downloading `largefile.iso`


## Notes
- Ideal for batch downloads compared to `curl`.
- Use `--limit-rate` to control download speed.

## References
- [man wget](https://man7.org/linux/man-pages/man1/wget.1.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)