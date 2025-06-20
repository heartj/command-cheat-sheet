# curl Command

Transfer data to or from a server using various protocols

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-o <file>` | Save output to a file |
| `-H <header>` | Add custom HTTP header |
| `-X <method>` | Specify HTTP method (e.g., -X POST) |
| `-d <data>` | Send data in a POST request |
| `-L` | Follow redirects |

## Examples
1. **Run command**:
```bash
curl https://example.com
```
Output: Fetches and displays the content of `example.com`

2. **Run command**:
```bash
curl -o output.html https://example.com
```
Output: Saves `example.com` content to `output.html`

3. **Run command**:
```bash
curl -X POST -d "key=value" http://api.example.com
```
Output: Sends a POST request with data to an API

4. **Run command**:
```bash
curl -H "Authorization: Bearer token" https://api.example.com

```
Output: Sends a request with a custom authorization header


## Notes
- Supports HTTP, HTTPS, FTP, and more.
- Use `--verbose` for detailed request info.

## References
- [man curl](https://man7.org/linux/man-pages/man1/curl.1.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)