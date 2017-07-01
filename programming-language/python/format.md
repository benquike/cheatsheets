# formatting string

## method 1: %

Similar with C.
```
"%c %d %x ..." % (args)
```


## format method

```
"{0:#0{1}x}".format(42,6)  # == 0x002a
```

Explanation:

```
{   # Format identifier
0:  # first parameter
#   # use "0x" prefix
0   # fill with zeroes
{1} # to a length of n characters (including 0x), defined by the second parameter
x   # hexadecimal number, using lowercase letters for a-f
}   # End of format identifier
```


## Ref

1. https://pyformat.info/
