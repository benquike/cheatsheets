# perl modules

## definition

A Perl module is a self-contained piece of Perl code that can be used by a Perl
program or by other Perl modules. It is conceptually similar to a C link library,
or a C++ class[^1].


## defining module

### defining module written by script

Just write the module in a .pm file, put it in a directory
which is included in `@INC` list then it is enough.

### defining module using C library

Some Perl modules link to dynamically loaded shared C libraries,
via a special interface language called XS[^1].

## using modules

To use a module, `use` and `require` are the available options[^2]

### use keyword

`use` can only be used in perl version 5+.

`use` is evaluated before execution time. You can think of it as
a preprocessor directive in C/C++.

Using `use`, the `BEGIN`, `CHECK` and `INIT` routines will be called automatically.

Using `use` we can import symbols.

### require keyword

`require` is evaluated at runtime, you can think of it as a function.

[^1]: A Perl module is a self-contained piece of Perl code that can be used by a Perl program or by other Perl modules. It is conceptually similar to a C link library, or a C++ class.
[^2]: http://tech.bayashi.net/pdmemo/use-require.html
