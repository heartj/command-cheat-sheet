# usermod Command

Modify an existing user account

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-aG <groups>` | Add user to supplementary groups (append) |
| `-s <shell>` | Change the user's login shell |
| `-l <newname>` | Change the user's login name |
| `-L` | Lock the user account |
| `-U` | Unlock the user account |

## Examples
1. **Run command**:
```bash
usermod -aG docker alice
```
Output: Adds alice to the docker group

2. **Run command**:
```bash
usermod -s /bin/zsh bob
```
Output: Changes bob's shell to zsh

3. **Run command**:
```bash
usermod -L alice
```
Output: Locks alice's account


## Notes
- Requires `sudo` to execute.
- Use `-a` with `-G` to avoid overwriting groups.

## References
- [man usermod](https://man7.org/linux/man-pages/man8/usermod.8.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)