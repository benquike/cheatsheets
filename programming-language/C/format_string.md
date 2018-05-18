# C Format String specifier

## Definition

The  format  string  is  a character string, beginning and ending in its initial shift state, if any.  The format string is composed of zero or more directives: ordinary characters (not %),
which are copied unchanged to the output stream; and conversion specifications, each of which results in **fetching zero or more subsequent arguments**(this means lift the stack counter).
Each conversion specification is introduced by the  character `%`, and ends with a conversion specifier. In between there may be (in this order) zero or more _flags_,
an optional minimum _field width_, an optional _precision_ and an optional _length_ modifier.

The  arguments must correspond properly (after _type promotion_) with the conversion specifier.  By default, the arguments are used in the order given, where each `*`
and each conversion specifier(`%`) asks for the next argument(and increase the stack counter) (and it is an error if insufficiently many arguments are given).  One
can also specify explicitly which argument is taken, at each place where an argument is required, by  writing "%m$" instead of '%' and "*m$" instead of `*` in which
case the stack counter won't be increased(??), where the _decimal_ integer m denotes the position in the argument list of the desired argument, _indexed starting from 1_.  Thus,

the `*` here is used to fetch the width specifier from the stack(ref [here](https://stackoverflow.com/questions/1000556/what-does-the-s-format-specifier-mean)).

    printf("%*d", width, num);

and

    printf("%2$*1$d", width, num);

are  equivalent.   The  second  style  allows repeated references to the same argument.  The C99 standard does not include the style using '$', which comes from the Single UNIX Specification.  If the
style using '$' is used, it must be used throughout for all conversions taking an argument and all width and precision arguments, but it may be mixed with "%%" formats which do not consume  an  argu‐
ment.  There may be no gaps in the numbers of arguments specified using '$'; for example, if arguments 1 and 3 are specified, argument 2 must also be specified somewhere in the format string.

For  some  numeric conversions a radix character ("decimal point") or thousands' grouping character is used.  The actual character used depends on the LC_NUMERIC part of the locale.  The POSIX locale
uses '.' as radix character, and does not have a grouping character.  Thus,

    printf("%'.2f", 1234567.89);

results in "1234567.89" in the POSIX locale, in "1234567,89" in the nl_NL locale, and in "1.234.567,89" in the da_DK locale.


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
|`-`    | left align                                                             |
|`+`    | Prepend a plus/minus sign for signed numbers                           |
|` `    | Pad using space                                                        |
|`0`    | When the 'width' option is specified, prepends zeros for numeric types.|
|`#`    | Alternate form: For 'g' and 'G' types, trailing zeros are not removed.
                          For 'f', 'F', 'e', 'E', 'g', 'G' types, the output always contains a decimal point.
                          For 'o', 'x', 'X' types, the text '0', '0x', '0X', respectively, is prepended to non-zero numbers. |

## length modifier

Length modifier can be used to specify how many bytes
to read or write[^2]

| Modifier |   Desc   |      Usage    |
|----------|--------- |---------------|
|    hh    |  1 byte  |      char     |
|    h     |  2 bytes |   short int   |
|    l     |  4 bytes |  long int     |
|    l    |  8 bytes | long long int  |

Example:

```
%hd
```

## Types
### %c
Interpret the argument as an char and display using the corresponding ASCII character.

### %d
Interpret the argument as an integer and display it using the decimal format

### %x
Interpret the argument as an integer and display it using the hexdecimal format

### %n
Write the number of bytes written out by printf to a variable in the argument list.
```
int n;
printf("I will write a value to n, %n", &n);  // after this statement, n == 27
```

[^1]:https://en.wikipedia.org/wiki/Printf_format_string

[^2]:http://security.cs.rpi.edu/courses/binexp-spring2015/lectures/9/06_lecture.pdf
