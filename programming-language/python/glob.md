# glob usage

```
import glob

x = glob.glob("./*.c")
# x is a list containing all matching files
```

glob does not support `**` operator, if we want
to use it, we should use glob2.
https://github.com/miracle2k/python-glob2