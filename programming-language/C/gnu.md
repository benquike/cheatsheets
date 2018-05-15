# _GNU_SOURCE

```
Defining _GNU_SOURCE has nothing to do with license and everything to do with writing (non-)portable code. If you define _GNU_SOURCE, you will get:

access to lots of nonstandard GNU/Linux extension functions
access to traditional functions which were omitted from the POSIX standard (often for good reason, such as being replaced with better alternatives, or being tied to particular legacy implementations)
access to low-level functions that cannot be portable, but that you sometimes need for implementing system utilities like mount, ifconfig, etc.
broken behavior for lots of POSIX-specified functions, where the GNU folks disagreed with the standards committee on how the functions should behave and decided to do their own thing.
As long as you're aware of these things, it should not be a problem to define _GNU_SOURCE, but you should avoid defining it and instead define _POSIX_C_SOURCE=200809L or _XOPEN_SOURCE=700 when possible to ensure that your programs are portable.

In particular, the things from _GNU_SOURCE that you should never use are #2 and #4 above.
```

https://stackoverflow.com/questions/5582211/what-does-define-gnu-source-imply



# ctype related

## __ctype_b_loc related

https://stackoverflow.com/questions/37702434/ctype-b-loc-what-is-its-purpose