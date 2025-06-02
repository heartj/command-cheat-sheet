# Linux `dig` Command

The `dig` command is an advanced DNS lookup tool that queries DNS servers for detailed information about domains, such as IP addresses, mail servers, or name servers.

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Purpose | Example |
|--------|---------|---------|
| `<domain>` | Query DNS for a domain | `dig example.com` (Resolve `example.com`) |
| `+short` | Show only the answer | `dig +short example.com` (Show only IPs) |
| `<type>` | Specify query type (e.g., A, MX, NS) | `dig MX example.com` (Get mail servers) |
| `@<server>` | Specify DNS server to query | `dig @8.8.8.8 example.com` (Use Google DNS) |
| `+trace` | Trace DNS delegation path | `dig +trace example.com` (Show resolution path) |
| `+nocmd` | Suppress command line in output | `dig +nocmd example.com` (Cleaner output) |

## Examples
1. **Basic DNS query**:  
   `dig example.com`  
   Shows detailed DNS records for `example.com`.
2. **Get only IP addresses**:  
   `dig +short example.com`  
   Lists IP addresses without extra details.
3. **Query mail servers**:  
   `dig MX example.com`  
   Shows mail exchanger records.
4. **Trace DNS resolution**:  
   `dig +trace google.com`  
   Displays the full DNS delegation path.

## Notes
- `dig` provides more detailed output than `nslookup`, ideal for debugging.
- Use `+short` for scripting to extract answers easily.
- Combine with `grep` or `awk` to parse specific fields, e.g., `dig +short example.com | head -n 1`.

## References
- [dig Manual](https://man7.org/linux/man-pages/man1/dig.1.html)
- [BIND dig Documentation](https://bind9.readthedocs.io/en/latest/manpages.html#dig)

[Back to Network Commands](../network.md) | [Back to Main Index](../../README.md)
