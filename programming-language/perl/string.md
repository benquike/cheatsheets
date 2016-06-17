# Perl String

## write hexpairs in strings

Precede the hex pair with `\x`, which is the same as `C`

```
$str = "aaaa\x50"
```

## repetition

`x` operator can be used to generate a string by repeting a character or string
multiple times

E.g

```
$a = "A"x1000
print $a # AAAAAA....(1000 times)
```


## concatenate

`.` operator is used to concatenate strings

```
$a = "A"."B"
$c = ('A'x10)."B"
```

## string constants

We can use single quote, double quote and HERE doc to
define string.

You can interpolate variables in strings quoted by double
quote.

## pitfalls

the print function of perl can not output characters above 0x80
