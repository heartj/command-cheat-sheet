# tar Command

Archive files into a tarball or extract them

[Back to File Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-c` | Create a new archive |
| `-x` | Extract files from an archive |
| `-f <file>` | Specify archive file name |
| `-z` | Use gzip compression |
| `-v` | Verbose output |

## Examples
1. **Run command**:
```bash
tar -czf backup.tar.gz /docs
```
Output: Creates a compressed archive of /docs

2. **Run command**:
```bash
tar -xzf backup.tar.gz
```
Output: Extracts backup.tar.gz to current directory

3. **Run command**:
```bash
tar -tvf backup.tar.gz
```
Output: Lists contents of backup.tar.gz


## Notes
- Common extensions: .tar (uncompressed), .tar.gz (gzip)
- Use `-j` for bzip2 compression

## References
- [man tar](https://man7.org/linux/man-pages/man1/tar.1.html)

[Back to File Commands](../index.md) | [Back to Main Index](../../README.md)