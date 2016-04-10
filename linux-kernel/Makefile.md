# Linux Kernel Build system(Makefiles) Usage Tips

## How to Add your code to the build system

Assume your code is in `a.c` in `dir/sub/`, then there must be a file called `Makefile`
in `dir/sub/`, and at the same time, add the following line in the Makefile if you want
your file to be built inside the kernel.

```
obj-y += a.o 
```

If you have a whole sub directory called of source code(named `foo`), you need do the following:
1. Write a Makefile in that subdirectory;
2. add all the source code in that Makefile in the way describe above
3. in the Makefile of its parent directory, add the following line

```
obj-y += foo 
```

In this way, the build system will create a file called built-in.o in each directory recursively
from bottom to up and the built-in.o(built by running `ld -r`) contains all the object files under
it and its sub directories[^1].


## how to add your code to a module

If you want to build a module, you simply add that object to `obj-m`.
If that module contains only one file, you can do it by appending the object
to `obj-m`

```
obj-m += mod.o # mod.c is the source
```

If you have multiple source file in a module, add the name of the module(assume it to be `mod.o`)
to `obj-m`, and then add all object files to `mod-objs`

```
obj-m += mod.o # mod.o will be built by linking a.o b.o
mod-objs := a.o  b.o
```

## objects experting symbols

If an object exports symbols, you  need to add it to `export-objs`

```
export-objs := isdn_common.o
```

## Linux Build System Source Code

The impelementation of the build system is im the following makefiles

```
Makefile # Top level Makefile
...
scripts/
├── ...
├── Makefile
├── Makefile.asm-generic
├── Makefile.build
├── Makefile.clean
├── Makefile.dtbinst
├── Makefile.extrawarn
├── Makefile.fwinst
├── Makefile.headersinst
├── Makefile.help
├── Makefile.host
├── Makefile.kasan
├── Makefile.lib
├── Makefile.modbuiltin
├── Makefile.modinst
├── Makefile.modpost
├── Makefile.modsign
├── Makefile.ubsan
├── ...
└── xz_wrap.sh
```

[^1]: http://masahir0y.blogspot.com/2012/02/linuxmakefile-6.html
