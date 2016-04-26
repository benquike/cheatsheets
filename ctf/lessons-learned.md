# Lessons

## Get information about a process

### ptrace
`ptrace` or `gdb` can be used to get information about a running process.
But this can be restricted by the administrator[^1].

This is configured in `/etc/sysctl.d/10-ptrace.conf `
by the following option(introduced in Ubuntu 10.10).

```
kernel.yama.ptrace_scope = 0
```

## injecting special chars to victim program

the shell separate input using `;`, but it can be escaped.
So we can inject strings containing any chars to program argument.

`scanf` seperate input using `\x0a`, so we can not input strings
containing `\0x0a` to scanf(is there any workaround?TBC).

If you want to inject some address containing `0x0a` to scanf to
and the address is located in the stack, we can change that addresses
by injecting some arguments or environmental variables to the program
and thus avoiding injecting addresses containing `0x0a`(learned from Greg).

## Get the runtime address of some buffer
Some time we need to know the runtime address of some buffer, there are a couple
of ways.

If we can inject the format string, the method mentioned in this paper[^2] can be
used.

Assuming we have the following source code, we need to get the address
of name,

```
#include <stdio.h>

int main( void )
{
	char name[ 1337 ];

	printf("Hello stranger...\nName: ");
	scanf( "%s", name );

	printf( "I'm sorry, " );
	printf( name );

	printf(". I can't let you in...\n");
}
```

we can pass in the format string to `printf` like this:

```
$ python -c 'printf AAAABBBBCCCC%n$s\xYY\xZZ\xWW\xUU...'
```

where `\xYY\xZZ\xWW\xUU...` is the address you guess.


Another way is to use `ltrace`, but it limit is also very obvious,
you can get only the addresses passed to standard library functions.

```
$ ltrace ./fsa
__libc_start_main(0x400656, 1, 0x7fffffffe518, 0x4006e0 <unfinished ...>
printf("Hello stranger...\nName: "Hello stranger...
)                                                                                                = 24
__isoc99_scanf(0x40077d, ====0x7fffffffdee0 =====, 0x7ffff7dd5970, 0x7ffff7ff5000Name: sdfasd
)                                                           = 1
printf("I'm sorry, ")                                                                                                              = 11
printf("sdfasd")                                                                                                                   = 6
puts(". I can't let you in..."I'm sorry, sdfasd. I can't let you in...
)                                                                                                    = 24
+++ exited (status 0) +++

```

[^1]: http://askubuntu.com/questions/41629/after-upgrade-gdb-wont-attach-to-process

[^2]: https://crypto.stanford.edu/cs155/papers/formatstring-1.2.pdf
