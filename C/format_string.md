# C Format String specifier

## General syntax
Ref[^1]

`%[parameter][flags][width][.precision][length]type`


## Parameter field
  Optional. n$ can be used to specifiy the index of the parameter that will use this format specifier.
E.g.

```
printf("%2$d %2$#x; %1$d %1$#x",16,17)   ->   "17 0x11; 16 0x10"
```

## Flag
| Flag  | Description                                                            |
|-------|------------------------------------------------------------------------|
|`-`    | left aligh                                                             |
|`+`    | Prepend a plus/minus sign for signed numbers                           |
|` `    | Pad using space                                                        |
|`0`    | When the 'width' option is specified, prepends zeros for numeric types.|
|`#`    | Alternate form: For 'g' and 'G' types, trailing zeros are not removed.
                          For 'f', 'F', 'e', 'E', 'g', 'G' types, the output always contains a decimal point.
                          For 'o', 'x', 'X' types, the text '0', '0x', '0X', respectively, is prepended to non-zero numbers. |


## Types
### %c
Interpret the argument as an char and display using the corresponding ASCII character.

### %d
Interpret the argument as an integer and display it using the decimal format

### %n
Write the number of bytes written out by printf to a variable in the argument list.
```
int n;
printf("I will write a value to n, %n", &n);  // after this statement, n == 27
```

[^1]:https://en.wikipedia.org/wiki/Printf_format_string
