# Linux `curl` Command

The `curl` command transfers data to or from a server, supporting protocols like HTTP, HTTPS, FTP, and more. It is widely used for downloading files, testing APIs, and sending HTTP requests.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `-o <file>` | Save output to a file | `curl -o page.html https://example.com` (Save page to `page.html`) |
| `-O` | Save output with remote filename | `curl -O https://example.com/file.txt` (Save as `file.txt`) |
| `-L` | Follow redirects | `curl -L https://example.com` (Follow HTTP redirects) |
| `-X <method>` | Specify HTTP method (e.g., GET, POST) | `curl -X POST https://api.example.com` (Send POST request) |
| `-H <header>` | Add custom HTTP header | `curl -H "Authorization: Bearer token" https://api.example.com` (Add header) |
| `-d <data>` | Send data in POST request | `curl -d "key=value" https://api.example.com` (POST data) |
| `-v` | Verbose output (show request details) | `curl -v https://example.com` (Show detailed request info) |

## Examples
1. **Download a file**:  
   `curl -o output.txt https://example.com/file.txt`  
   Downloads `file.txt` and saves it as `output.txt`.
2. **Send a POST request**:  
   `curl -X POST -d '{"name":"user"}' -H "Content-Type: application/json" https://api.example.com`  
   Sends JSON data to an API endpoint.
3. **Follow redirects**:  
   `curl -L https://bit.ly/redirect`  
   Follows redirects to the final URL.
4. **Test an API with headers**:  
   `curl -H "Authorization: Bearer abc123" https://api.example.com/data`  
   Sends a request with an authorization header.

## Notes
- Use `-s` for silent mode to suppress progress output.
- Combine `-v` with `--trace-ascii` for detailed debugging of requests.
- Ensure URLs are properly escaped, especially with query parameters.

## References
- [curl Documentation](https://curl.se/docs/manpage.html)
- [man curl](https://man7.org/linux/man-pages/man1/curl.1.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
