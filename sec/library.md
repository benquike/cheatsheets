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

### How to create dynamic library
  "How to create dynamic libraries" can be found here[^3].

#### SONAME and related stuff
When creating a shared library using GNU ld[^4], you can use `-h=<SO_NAME>`
or `-soname=<SO_NAME>` to specify the the value of SONAME field(or property)
of the shared library.

When a linker is trying to readin the shared library to solve some symbol, if
this field is set, the linker will stop reading the current file, instead, it
will readin the shared library specified by that field. And in dynamic section
of the executable, it will also fill in the name specified in the `<SO_NAME>` field.

For more details, read here[^5].

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
[^3]: http://www.cprogramming.com/tutorial/shared-libraries-linux-gcc.html
[^4]: https://ftp.gnu.org/old-gnu/Manuals/ld-2.9.1/html_node/ld_3.html
[^5]: http://stackoverflow.com/questions/12637841/what-is-the-soname-option-for-building-shared-libraries-for

### How to specify rpath
In case of gnu ld, we can use option `-rpath=dir` to add a runtime library search path when building an `executable`.

What is the difference between rpath and rpath-link?

### security implication of rpath
    it can be used as a defense against environmental overide attack
