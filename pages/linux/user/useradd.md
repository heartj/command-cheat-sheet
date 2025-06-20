# useradd Command

Create a new user

[Back to User Commands](./index.md) | [Back to Main Index](../../README.md)

## Common Options

| Option | Description |
|--------|-------------|
| `-m` | Create a home directory for the user |
| `-s <shell>` | Specify the user's login shell (e.g., -s /bin/bash) |
| `-G <groups>` | Add user to supplementary groups |
| `-u <uid>` | Specify user ID |

## Examples
1. **Run command**:
```bash
useradd -m alice
```
Output: Creates user alice with a home directory

2. **Run command**:
```bash
useradd -m -s /bin/zsh -G sudo bob
```
Output: Creates user bob with zsh shell and sudo group

3. **Run command**:
```bash
useradd -u 1001 guest
```
Output: Creates user guest with UID 1001


## Notes
- Requires `sudo` to execute.
- Use `passwd` to set the user’s password.

## References
- [man useradd](https://man7.org/linux/man-pages/man8/useradd.8.html)

[Back to User Commands](../index.md) | [Back to Main Index](../../README.md)