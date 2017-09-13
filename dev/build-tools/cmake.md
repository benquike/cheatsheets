# cmake usage

## show the commands for building source files

Ref[^1]

```
$ make VERBOSE=1
```

or

```
$ cmake -DCMAKE_VERBOSE_MAKEFILE=ON ...
```

## Add customized options

```
$ cmake ... -DCMAKE_C_FLAGS='flags'  -DCMAKE_CXX_FLAGS='flags' ...
```

[^1]: http://stackoverflow.com/questions/2670121/using-cmake-with-gnu-make-how-can-i-see-the-exact-commands
* https://stackoverflow.com/questions/25207619/make-cmake-pass-command-line-variable-to-compiler
