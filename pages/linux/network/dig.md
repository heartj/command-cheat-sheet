# dig Command

Perform detailed DNS lookups with flexible output

[Back to Network Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `+short` | Display only the answer section |
| `@<server>
` | Specify DNS server (e.g., @8.8.8.8) |
| `-t <type>` | Specify query type (e.g., -t MX) |
| `-x <ip>` | Perform reverse lookup for an IP address |
| `-4` | Force IPv4 query |
| `-6` | Force IPv6 query |

## Examples
1. **Run command**:
```bash
dig example.com
```
Output: Shows detailed DNS records for `example.com`

2. **Run command**:
```bash
dig +short example.com
```
Output: Displays only the IP address (e.g., 93.184.216.34)

3. **Run command**:
```bash
dig @8.8.8.8 -t MX example.com
```
Output: Queries Google DNS for mail servers of `example.com`

4. **Run command**:
```bash
dig -x 8.8.8.8
```
Output: Performs reverse lookup, returns `dns.google`


## Notes
- Preferred over `nslookup` for advanced DNS troubleshooting.
- Use `+short` for concise output in scripts.

## References
- [man dig](https://man7.org/linux/man-pages/man1/dig.1.html)

[Back to Network Commands](../index.md) | [Back to Main Index](../../README.md)