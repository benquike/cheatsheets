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

Writing assembly code

```
wa <assembly code>
```
For example:
```
s 0x0804866c
wa jmp 0x8048600
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

> Note: There is some difference between ps and pc.

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

## ASCII CFG

```
$ VV

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


## radare2 and capstone

http://radare.today/posts/Radare2-capstone/


## r2pm

```
# installing plugins
$ r2pm -i unicorn-lib
$ r2pm -i unicorn
```

## rasm2

List all supported architectures

```
$ rasm2 -L
_dAe  8 16       6502        LGPL3   6502/NES/C64/Tamagotchi/T-1000 CPU
_dA_  8          8051        PD      8051 Intel CPU
_dA_  16 32      arc         GPL3    Argonaut RISC Core
a___  16 32 64   arm.as      LGPL3   as ARM Assembler (use ARM_AS environment)
adAe  16 32 64   arm         BSD     Capstone ARM disassembler
_dA_  16 32 64   arm.gnu     GPL3    Acorn RISC Machine CPU
_d__  16 32      arm.winedbg LGPL2   WineDBG's ARM disassembler
adAe  8 16       avr         GPL     AVR Atmel
adAe  16 32 64   bf          LGPL3   Brainfuck (by pancake, nibble) v4.0.0
_dA_  16         cr16        LGPL3   cr16 disassembly plugin
_dA_  32         cris        GPL3    Axis Communications 32-bit embedded processor
adA_  32 64      dalvik      LGPL3   AndroidVM Dalvik
ad__  16         dcpu16      PD      Mojang's DCPU-16
_dA_  32 64      ebc         LGPL3   EFI Bytecode
adAe  16         gb          LGPL3   GameBoy(TM) (z80-like)
_dAe  16         h8300       LGPL3   H8/300 disassembly plugin
_d__  32         hexagon     GPL3    Qualcomm DSPv5
_d__  32         hppa        GPL3    HP PA-RISC
_dAe             i4004       LGPL3   Intel 4004 microprocessor
_dA_  8          i8080       BSD     Intel 8080 CPU
adA_  32         java        Apache  Java bytecode
_d__  32         lanai       GPL3    LANAI
_d__  8          lh5801      LGPL3   SHARP LH5801 disassembler
_d__  32         lm32        BSD     disassembly plugin for Lattice Micro 32 ISA
_d__  16 32      m68k        BSD     Capstone M68K disassembler
_dA_  32         malbolge    LGPL3   Malbolge Ternary VM
_d__  16         mcs96       LGPL3   condrets car
adAe  16 32 64   mips        BSD     Capstone MIPS disassembler
adAe  32 64      mips.gnu    GPL3    MIPS CPU
_dA_  16         msp430      LGPL3   msp430 disassembly plugin
_dA_  32         nios2       GPL3    NIOS II Embedded Processor
_dAe  8          pic18c      LGPL3   pic18c disassembler
_dAe  32 64      ppc         BSD     Capstone PowerPC disassembler
_dA_  32 64      ppc.gnu     GPL3    PowerPC
_dA_  32 64      riscv       GPL     RISC-V
_dAe  32         rsp         LGPL3   Reality Signal Processor
_dA_  32         sh          GPL3    SuperH-4 CPU
_dA_  8 16       snes        LGPL3   SuperNES CPU
_dAe  32 64      sparc       BSD     Capstone SPARC disassembler
_dA_  32 64      sparc.gnu   GPL3    Scalable Processor Architecture
_d__  16         spc700      LGPL3   spc700, snes' sound-chip
_d__  32         sysz        BSD     SystemZ CPU disassembler
_dA_  32         tms320      LGPLv3  TMS320 DSP family (c54x,c55x,c55x+,c64x)
_d__  32         tricore     GPL3    Siemens TriCore CPU
_dAe  32         v810        LGPL3   v810 disassembly plugin
_d__  32         v850        LGPL3   v850 disassembly plugin
_dAe  8 32       vax         GPL     VAX
_d__  32         wasm        MIT     WebAssembly (by pancake) v0.1.0
_dA_  32         ws          LGPL3   Whitespace esotheric VM
a___  16 32 64   x86.as      LGPL3   Intel X86 GNU Assembler
_dAe  16 32 64   x86         BSD     Capstone X86 disassembler
a___  16 32 64   x86.nasm    LGPL3   X86 nasm assembler
a___  16 32 64   x86.nz      LGPL3   x86 handmade assembler
_dAe  16 32 64   x86.udis    BSD     udis86 x86-16,32,64
_dA_  16         xap         PD      XAP4 RISC (CSR)
_dA_  32         xcore       BSD     Capstone XCore disassembler
_dAe  32         xtensa      GPL3    XTensa CPU
adA_  8          z80         GPL     Zilog Z80
_d__  32         propeller   LGPL3   propeller disassembly plugin
```
