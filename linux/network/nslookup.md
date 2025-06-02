# Linux `nslookup` Command

The `nslookup` command queries DNS servers to retrieve domain name or IP address information. It is used for troubleshooting DNS resolution issues.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `<domain>` | Query DNS for a domain | `nslookup example.com` (Resolve `example.com`) |
| `-type=<type>` | Specify query type (e.g., A, MX, NS) | `nslookup -type=MX example.com` (Get mail servers) |
| `-query=<type>` | Alias for `-type` | `nslookup -query=A example.com` (Get A records) |
| `-timeout=<sec>` | Set query timeout | `nslookup -timeout=5 example.com` (5-second timeout) |
| `<server>` | Specify DNS server to query | `nslookup example.com 8.8.8.8` (Use Google DNS) |

## Examples
1. **Resolve a domain**:  
   `nslookup example.com`  
   Shows IP addresses for `example.com`.
2. **Query mail servers**:  
   `nslookup -type=MX example.com`  
   Lists mail exchanger records for `example.com`.
3. **Use a specific DNS server**:  
   `nslookup example.com 1.1.1.1`  
   Queries Cloudflare’s DNS server.
4. **Check name servers**:  
   `nslookup -type=NS example.com`  
   Lists name servers for `example.com`.

## Notes
- Interactive mode is available by running `nslookup` without arguments.
- Consider `dig` for more detailed DNS queries.
- DNS servers may block excessive queries; use `-timeout` to adjust.

## References
- [man nslookup](https://man7.org/linux/man-pages/man1/nslookup.1.html)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
