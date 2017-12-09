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

## symbols

```
$symbol-file foo.symbol
```

https://stackoverflow.com/questions/20380204/how-to-load-multiple-symbol-files-in-gdb

kernel debugging
http://sysprogs.com/VisualKernel/documentation/kernelsymbols


## ui

Using `Ctrl-x` `Ctrl-a` to enable TUI.

WebGUI: https://github.com/cs01/gdbgui