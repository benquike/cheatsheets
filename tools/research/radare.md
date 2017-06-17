# radare2 usage

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