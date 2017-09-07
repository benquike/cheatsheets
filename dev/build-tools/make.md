# Makefile usage

## variables

we can define a variable from the command.

If we run the following cmd, `VAR` will be defined
in the Makefile.
```
make VAR=a
```

## text functions

### verbose substitute

```
$(subst from,to,text to subst)

$(subst ee,EE,feet on the street)  ==> fEEt on the strEEt
```

### pattern substitute

```
(patsubst from,to,text to substitute)
$(patsubst %.c,%.o,x.c.c bar.c)  ==> x.c.o bar.o
```

It is the same as $(var:pattern=replacement)

### strip function

remove the starting and tailing space.

## generating depenedency graph

https://github.com/lindenb/makefile2graph
