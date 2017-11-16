# Using gdb

## dump the content of a register
```
$ p/x $rax
```

or
```
$ info registers
```

## write memory

```
set {int}0x83040 = 4
```


## breakpoints

### set a break point

```
# break xxxxx
```

### show breakpoint information

```
# info breakpoints
```

### disable breakpoints

```
# disable xxxx
```