# gcc usage


## complile code alone

`-nostdlib -fno-builtin -nostdinc` 


## how to handle name conflict with standard library

define your own function with any name (that may conflict with standard library)
and do not include the headers of the standard library, use `extern` declarations
when you need to use some from the library.


## gcc plugins

http://thinkingeek.com/2015/08/16/a-simple-plugin-for-gcc-part-1/