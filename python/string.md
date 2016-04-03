# String class

## string functions
### join
    used to make a list(the elements of the list must be string objects) into a string. e.g.,
```
"-".join(['a', 'b', 'c']) will return 'a-b-c'.
```

### format
1. Old formatting :
```
"%x %x"%(10, 44)
"%s, %s"%('one', 'two')
```
2. New formatting
```
"{} {}".format('one', 'two') => "one two"
"{1} {0}".format('one', 'two') => "two one"
```
3. TODO
   Value conversion, padding, truncating, ...

Ref:Pyformat[^1]

### encode and decode
str.encode(encoding="", errors="")
str.decode.
For all the supported encoding and decoding method, see, Standard encoding list[^2]
```
"This is a test string".encode('base64','strict')
```

[^1]: <https://pyformat.info/>
[^2]: <https://docs.python.org/2/library/codecs.html#standard-encodings>
