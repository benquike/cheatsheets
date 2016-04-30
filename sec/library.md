# Library related

## static library

## dynamic library

### dynamic library loading
  The libraries are search using the following mechanisms, in the
  following order[^1][^2].

1. the DT_RPATH dynamic section attribute of the library causing the lookup 
2. the DT_RPATH dynamic section attribute of the executable 
3. the LD_LIBRARY_PATH environment variable, unless the executable is setuid/setgid.
4. the DT_RUNPATH dynamic section attribute of the executable
5. /etc/ld.so.cache
6. base library directories (/lib and /usr/lib)


Note:
1). Regarding steps 1 and 2: The DT_RPATH attribute is ignored if the
    DT_RUNPATH attribute is found. Then, LD_LIBRARY_PATH is searched first!
2). Regarding step 3: LD_LIBRARY_PATH can be overridden by calling the
    dynamic linker with the option --library-path (e.g. /lib/ld-linux.so.2
    --library-path $HOME/mylibs myprogram
3). Regarding steps 5 and 6: If the executable was linked with -z nodeflib linker
    option, /lib and /usr/lib are skipped at step 5 and 6. 

4). Regarding all steps: If the dynamic linker is called using --inhibit-rpath LIST,
    the objects in LIST are ignored.

5). Before library searching takes place, the libraries in LD_PRELOAD are loaded

[^1]: https://wiki.debian.org/RpathIssue
[^2]: http://blog.tremily.us/posts/rpath/

### security implication of rpath
    it can be used as a defense against environmental overide attack
