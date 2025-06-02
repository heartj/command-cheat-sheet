# Linux `wget` Command

The `wget` command downloads files from the web using HTTP, HTTPS, or FTP. It is designed for robust file retrieval, supporting recursive downloads and resuming interrupted transfers.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-O <file>` | Save output to a file | `wget -O page.html https://example.com` (Save as `page.html`) |
| `-c` | Continue interrupted download | `wget -c https://example.com/largefile.zip` (Resume download) |
| `-r` | Recursive download | `wget -r https://example.com/docs/` (Download directory) |
| `--limit-rate=<rate>` | Limit download speed | `wget --limit-rate=200k https://example.com/file` (Limit to 200 KB/s) |
| `-P <dir>` | Save files to specified directory | `wget -P /downloads https://example.com/file.txt` (Save to `/downloads`) |
| `-q` | Quiet mode (suppress output) | `wget -q https://example.com/file.txt` (Download silently) |
| `-i <file>` | Download URLs from a file | `wget -i urls.txt` (Download from list in `urls.txt`) |

## Examples
1. **Download a single file**:  
   `wget https://example.com/file.txt`  
   Downloads `file.txt` to the current directory.
2. **Resume a partial download**:  
   `wget -c https://example.com/largefile.zip`  
   Resumes downloading `largefile.zip`.
3. **Download a directory recursively**:  
   `wget -r -np https://example.com/docs/`  
   Downloads `docs/` without parent directories (`-np`).
4. **Download multiple URLs from a file**:  
   `wget -i urls.txt`  
   Downloads all URLs listed in `urls.txt`.

## Notes
- Use `-np` (`--no-parent`) with `-r` to avoid downloading parent directories.
- Combine with `--spider` to check if a URL exists without downloading.
- `wget` is better suited for downloading files than `curl`, but less flexible for custom HTTP requests.

## References
- [GNU wget Manual](https://www.gnu.org/software/wget/manual/wget.html)
- [man wget](https://man7.org/linux/man-pages/man1/wget.1.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)