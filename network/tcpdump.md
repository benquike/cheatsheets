# tcpdump usage

tcpdump is a command line packet capturing tool[^1].

Here are some typical usage.

## capture the packets with some host

### both incoming and outgoing packets

```
$ tcpdump host 192.168.1.1
```

### only packets from some host

```
$ tcpdump src 192.168.1.1
```

### packets going to some host

```
$ tcpdump dst 192.168.1.1
```

### packet from/to a net

```
$ tcpdump net 1.2.3.0/24
```

### other filters

#### port filter

Using port, you can specify packets whose src and/or dst port is some value

```
$ tcpdump port 1234   # either src or dst port is 1234
$ tcpdump src port 1234 # src port only
$ tcpdump dst port 1234 # dst port only
$ tcpdump portrange 21-25  # port range
```


[^1]: https://danielmiessler.com/study/tcpdump/
