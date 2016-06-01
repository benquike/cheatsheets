# Running perl

## from command line

```
$ perl -e 'perl code here'
```

E.g, the following code can be used to feed 100 As as arguments
to bof program.

```
./bof `perl -e 'print "A"x100'`
```
