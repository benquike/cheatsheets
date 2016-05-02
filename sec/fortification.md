# FORTITY_SOURCE

`FORTRIFY_SOURCE` is a lightweight defending mechanism against buffer overflow in the following functions[^1][^2].

    memcpy, mempcpy, memmove, memset, strcpy, stpcpy, strncpy, strcat, 
    strncat, sprintf, vsprintf, snprintf, vsnprintf, gets.

It protects both C and C++, and works by  counting the number of bytes to copy, if the attacker tries to copy more bytes,
the execution of the program is stopped.

## Usage
`FORTIFY_SOURCE` can be set by defining a macro called `_FORTIFY_SOURCE` when compiling the program.
Possible values of this macro are `0`, `1`, or `2`. If 0 is defined, `FORTIFY_SOURCE` is disabled; if
`1` is set(and the optimization should be set to O1 or above), checks that should not change the behavior
of the comforming program is performed; with `_FORTIFY_SOURCE` setting to 2, more checking will be added,
some at compile time, some at run time. For more details, read the ref[^1][^2].

[^1] https://access.redhat.com/blogs/766093/posts/1976213
[^2] https://wiki.debian.org/Hardening#DEB_BUILD_HARDENING_FORTIFY_.28gcc.2Fg.2B-.2B-_-D_FORTIFY_SOURCE.3D2.29
