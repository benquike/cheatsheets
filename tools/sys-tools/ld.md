# Using gnu ld

## reading command options from a file

use `@`, e.g:

```
$gcc ... @libGLESv2.so.rsp ...
```
will cause the linker to read command options from libGLESv2.so.rsp.

## -B, specifying where to find executables

For each subprogram to run, the driver will first try to locate the executable with the prefix specified by `-B`,
If the executable can not be found there, it will try the standard prefixes `/usr/lib/gcc/` and `/usr/local/lib/gcc/`

## specifying where to find the headers and libraries

`--sysroot`
