# my ctf tools

## HTTP tools

### hackbar
1. hide and show hackbar using F9

### tamper-data

### live http headers

## GDB plugin
### voidwalker
    https://github.com/dholm/voidwalker


## suply special input to programs

### Print characters using ascii code

```
$ echo -e '\x41\x42\x43\x44'   # print ABCD using echo command built in shell
$ printf '\x41\x42\x43\x44'
$ python -c 'print "\x41\x42\x43\x44"'
$ perl -e 'print "\x41\x42\x43\x44"'
```

### Print long inputs

```
$ echo/printf (hold down alt; type 100) A
$ python -c 'print "A"*100'
$ perl -e 'print "A" x 100;'
```

### supply the output of a command to a program

#### in shell
```
$ ./vulnerable `your_command_here`   # 1
$ ./vulnerable $(your_command_here)  # 2
$ your_command_here | ./vulnerable   # 3
$ your_command_here > filename       # 4
$ ./vulnerable < filename
```

#### in gdb

```
~~ $ run $(your_command_here)      # 1 ~~
$ run < <(your_command_here)    # 2
$ your_command_here > filename  # 3
$ run < filename
```

For reference[^1][^2]

[^1]: http://security.cs.rpi.edu/courses/binexp-spring2015/lectures/5/04_lecture.pdf
[^2]: http://stackoverflow.com/questions/6121094/how-do-i-run-a-program-with-commandline-args-using-gdb-within-a-bash-script


## ROP

### ROPgadget
[ROGgadget](http://shell-storm.org/project/ROPgadget/)

### Ropper
[Ropper](http://scoding.de/ropper/)

### rp
[rp++](https://github.com/0vercl0k/rp)



## Good sites

1. https://ghostbin.com/paste/6kho7
