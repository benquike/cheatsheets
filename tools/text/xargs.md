# xargs usage

xargs takes the output of a command, split it and feed them to another command[^1].
Athough the backquote feature of bash[^3] offers similar functions, xargs is more
flexible, in that it is able to split very long list of arguments run the second command
multiple times.


## controlling max number of arguments

By default, xargs runs echo if no command is specified.

    echo 1 2 3 4 5 6 | xargs
    1 2 3 4 5 6

    echo 1 2 3 4 5 6 | xargs -n 2
    1 2
    3 4
    5 6

## argument list marker

By defaut xargs uses `{}` as the marker of argument, which is the same as
`find -exec`. We can use -I to define our own marker

    find . -type file | xargs mv {} to_dir

or

    find . -type file | xargs -I file mv file to_dir

## customizing seperator

see ref[^1].

[^1]: http://www.cyberciti.biz/faq/linux-unix-bsd-xargs-construct-argument-lists-utility/

[^2]: http://unix.stackexchange.com/questions/27428/what-does-backquote-backtick-mean-in-commands
