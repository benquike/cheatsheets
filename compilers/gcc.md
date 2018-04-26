
# dump the predefined macros

```
$ gcc -dM -E - < /dev/null
```

https://stackoverflow.com/questions/2224334/gcc-dump-preprocessor-defines

# internals
## GENERIC
   https://www.slideshare.net/chimerawang/gcc-generic


# implementing a frontend

http://thinkingeek.com/gcc-tiny/



# dumping the tree related structure

```
gcc -fdump-tree-all test4.c
```

# disable jump table

```
gcc -O0 -fno-jump-tables test.c -o test
```
http://lazarenko.me/switch/
http://www.jauu.net/2010/06/15/gcc-generated-switch-jump-tables/


# disable function inlining

```
$ gcc/clang -fno-inline ..... 
```


# no stack protector

```
$ gcc -fno-stack-protector ...
```