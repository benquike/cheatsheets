# Makefile usage

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
