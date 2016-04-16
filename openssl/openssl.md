# Openssl usage

## generate random number

`openssl rand` can be used to generate random numbers.

The following command can be used to generate a 6-byte random number.

```
$ openssl rand -hex 6
```

This can be used to randomly set the MAC address of the computer

```
$ openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//' | xargs sudo ifconfig eth0 ether
```

## Reference
1. Command Line Utilities[^1]

[^1]: https://wiki.openssl.org/index.php/Command_Line_Utilities
