# zsh

## the problem of being too slow used in nfs files system


When there is a git repo in an nfs backed system, it is very slow.

Solution: uncomment the following line in `~/.zshrc`

```
DISABLE_UNTRACKED_FILES_DIRTY="true"
```
