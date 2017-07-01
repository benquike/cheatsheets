# radare2 usage

## command format

```
[.][times][cmd][~grep][@[@iter]addr!size][|>pipe] ;
```


https://radare.gitbooks.io/radare2book/content/introduction/command_format.html


## General usage

Each kind of command starts with a letter,
all subcommands starts with that letter.
to get help, append a question mark after a the
prefix of the command.

For example, `s` is used to get and  change the current
seek position.

    [0x00000000]> s?
    |Usage: s  # Seek commands
    | s                 Print current address
    | s:pad             Print current address with N padded zeros (defaults to 8)
    | s addr            Seek to address
    | s-                Undo seek
    | s- n              Seek n bytes backward
    | s--               Seek blocksize bytes backward
    | s+                Redo seek
    | s+ n              Seek n bytes forward
    | s++               Seek blocksize bytes forward
    | s[j*=!]           List undo seek history (JSON, =list, *r2, !=names)
    | s/ DATA           Search for next occurrence of 'DATA'
    | s/x 9091          Search for next occurrence of \x90\x91
    | s.hexoff          Seek honoring a base from core->offset
    | sa [[+-]a] [asz]  Seek asz (or bsize) aligned to addr
    | sb                Seek aligned to bb start
    | sC[?] string      Seek to comment matching given string
    | sf                Seek to next function (f->addr+f->size)
    | sf function       Seek to address of specified function
    | sg/sG             Seek begin (sg) or end (sG) of section or file
    | sl[?] [+-]line    Seek to line
    | sn/sp             Seek to next/prev location, as specified by scr.nkey
    | so [N]            Seek to N next opcode(s)
    | sr pc             Seek to register
    | ss                Seek silently (without adding an entry to the seek history)


`a` is used to do analysis:


    [0x00000000]> a?
    |Usage: a[abdefFghoprxstc] [...]
    | ab [hexpairs]    analyze bytes
    | abb [len]        analyze N basic blocks in [len] (section.size by default)
    | aa[?]            analyze all (fcns + bbs) (aa0 to avoid sub renaming)
    | ac [cycles]      analyze which op could be executed in [cycles]
    | ad[?]            analyze data trampoline (wip)
    | ad [from] [to]   analyze data pointers to (from-to)
    | ae[?] [expr]     analyze opcode eval expression (see ao)
    | af[?]            analyze Functions
    | aF               same as above, but using anal.depth=1
    | ag[?] [options]  output Graphviz code
    | ah[?]            analysis hints (force opcode size, ...)
    | ai [addr]        address information (show perms, stack, heap, ...)
    | ao[?] [len]      analyze Opcodes (or emulate it)
    | aO               Analyze N instructions in M bytes
    | ar[?]            like 'dr' but for the esil vm. (registers)
    | ap               find prelude for current offset
    | ax[?]            manage refs/xrefs (see also afx?)
    | as[?] [num]      analyze syscall using dbg.reg
    | at[?] [.]        analyze execution traces
    | av[?] [.]        show vtables
    Examples:
    f ts @ `S*~text:0[3]`; f t @ section..text
    f ds @ `S*~data:0[3]`; f d @ section..data
    .ad t t+ts @ d:ds

`af` is used to analyse functions, to get help for this subcommand,
run `af?`

    [0x00000000]> af?
    |Usage: af
    | af ([name]) ([addr])                  analyze functions (start at addr or $$)
    | afr ([name]) ([addr])                 analyze functions recursively
    | af+ addr name [type] [diff]           hand craft a function (requires afb+)
    | af- [addr]                            clean all function analysis data (or function at addr)
    | afb+ fcnA bbA sz [j] [f] ([t]( [d]))  add bb to function @ fcnaddr
    | afb[?] [addr]                         List basic blocks of given function
    | afB 16                                set current function as thumb (change asm.bits)
    | afc[c] ([addr])@[addr]                calculate the Cycles (afc) or Cyclomatic Complexity (afcc)
    | afC[?] type @[addr]                   set calling convention for function
    | aft[?]                                type matching, type propagation
    | aff                                   re-adjust function boundaries to fit
    | afF[1|0|]                             fold/unfold/toggle
    | afi [addr|fcn.name]                   show function(s) information (verbose afl)
    | afl[?] [l*] [fcn name]                list functions (addr, size, bbs, name) (see afll)
    | afo [fcn.name]                        show address for the function named like this
    | afm name                              merge two functions
    | afM name                              print functions map
    | afn[?] name [addr]                    rename name for function at address (change flag too)
    | afna                                  suggest automatic name for current offset
    | afs [addr] [fcnsign]                  get/set function signature at current address
    | afS[stack_size]                       set stack frame size for function at current address
    | afu [addr]                            resize and analyze function from current address until addr
    | afv[bsra]?                            manipulate args, registers and variables in function
    | afx[cCd-] src dst                     add/remove code/Call/data/string reference


## Get information about opened file

Get the sections

```
iS
```

Get symbols

```
is
```

Get strings in the data section

```
iz
```

Get strings in the whole program

```
izz
```

Get all the import and export info

all import

```
ii
```

all export
```
iE
```

all import and export info
```
ia
```

## write

First of all, to write to the file, we
need to use `-w` option to open the file.

```
r2 -w KPRCA_00064
```

Seek to the place where we want to write

```
s <addr>
```

Then `wx` command can be used to write.
When we use `wx`, we need to use 2 hex
digits to represent one byte.

```
wx <hexpairs>
```


## find xrefs

ax shows all cross reference
Then we can use grep to narrow down
the results.

```
ax
```


How to find the reference of a string
in the program

First find the address of a string

```
iz
```

the search

```
/c address
```


## show something

`p` command

Show disassembly.

```
pd
```

Print in the format of C or python byte arrays:

C array

```
pc 16
#define _BUFFER_SIZE 16
const uint8_t buffer[16] = {
  0x53, 0x57, 0x56, 0x83, 0xec, 0x20, 0x8b, 0x35, 0x20, 0xcc,
  0x04, 0x08, 0x89, 0x34, 0x24, 0xc7
};

```

Python format
```
pcp 16

pcp 16
import struct
buf = struct.pack ("16B", *[
0x53,0x57,0x56,0x83,0xec,0x20,0x8b,0x35,0x20,0xcc,0x04,
0x08,0x89,0x34,0x24,0xc7])
```

JSON format

```
pcj  16
[83,87,86,131,236,32,139,53,32,204,4,8,137,52,36,199]
```

Assembly code

```
 pcA 16
sub_0x08048560:
 .byte 0x53  // push ebx
 .byte 0x57  // push edi
 .byte 0x56  // push esi
 .byte 0x83, 0xec, 0x20  // sub esp, 0x20
 .byte 0x8b, 0x35, 0x20, 0xcc, 0x04, 0x08  // mov esi, dword [0x804cc20]
 .byte 0x89, 0x34, 0x24  // mov dword [esp], esi
 .byte 0xc7  // invalid
.equ shellcode_len, 16

```

In halfwords, words, double words

```
// halfwords
> pch 16
#define _BUFFER_SIZE 8
const uint16_t buffer[8] = {
  0x5753, 0x8356, 0x20ec, 0x358b, 0xcc20, 0x0804, 0x3489, 0xc724
};


// words
> pcw 16
#define _BUFFER_SIZE 4
const uint32_t buffer[4] = {
  0x83565753U, 0x358b20ecU, 0x0804cc20U, 0xc7243489U
};

//double words
> pcd 16
#define _BUFFER_SIZE 2
const uint64_t buffer[2] = {
  0x358b20ec83565753ULL, 0xc72434890804cc20ULL
};

```

String
```
pcs 16
"\x53\x57\x56\x83\xec\x20\x8b\x35\x20\xcc\x04\x08\x89\x34\x24\xc7"
```

`ps` print string

## search

`/` command


## grep the result of a command

```
cmd ~<search string>
```

Get the first row of a search result

```
cmd ~<search string>:0
```

Get the first column of a search result

```
cmd ~<search string>[0]
```


## ESIL


This language is used to trace CPU states in R2.


## python interface

### r2pipe

[r2pipe](https://github.com/radare/radare2-r2pipe)

```
import r2pipe

r2 = r2pipe.open("/bin/ls")
r2.cmd('aa')
print(r2.cmd("afl"))
print(r2.cmdj("aflj"))  # evaluates JSONs and returns an object
r2.quit()
```

[Others](https://github.com/radare/radare2-bindings)

