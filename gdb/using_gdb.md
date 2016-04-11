# Using gdb

## dump the content of a register
```
$d/x $rax
```

or
```
$ info registers
```

## write memory

```
set {int}0x83040 = 4
```
