# nslookup Command

Query DNS servers to resolve domain names or IP addresses

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-type=<type>` | Specify query type (e.g., -type=MX for mail servers) |
| `-query=<server>` | Specify DNS server to query (e.g., -query=8.8.8.8) |
| `-timeout=<seconds>` | Set query timeout |
| `-debug` | Enable debug output |

## Examples
1. **Run command**:
```bash
nslookup example.com
```
Output: Resolves `example.com` to its IP address (e.g., 93.184.216.34)

2. **Run command**:
```bash
nslookup -type=MX example.com
```
Output: Lists mail servers for `example.com`

3. **Run command**:
```bash
nslookup -query=8.8.8.8 example.com
```
Output: Queries Google DNS (8.8.8.8) for `example.com`

4. **Run command**:
```bash
nslookup -type=A www.google.com
```
Output: Resolves A record for `www.google.com`


## Notes
- Non-interactive mode is preferred for scripting.
- Use `dig` for more detailed DNS queries.

## References
- [man nslookup](https://man7.org/linux/man-pages/man1/nslookup.1.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)