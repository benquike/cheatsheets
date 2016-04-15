# netstat usage

## list ports

### list all ports (both listening and non-listening)[^1]

```
$ netstat -a
```

### list all tcp ports

```
$ netstat -at
```

### list all upd ports

```
$ netstat -au
```

### list all listening sockets

```
$ netstat -l
```

#### list all listening tcp sockets

```
$ netstat -lt
```

#### list all listening udp sockets

```
$ netstat -lu
```

#### list all listening unix sockets

```
$ netstat -lx
```

## show the statisitics of each protocol

```
$ netstat -s
```

To show the statisitics of TCP/UDP, combine -s with -t or others
e.g.

```
$ netstat -st  # show the statisitics of tcp protocol
$ netstat -su  # show the statisitics of udp protocol
```

## show which program is using which port

```
$ netstat -p
```

Combined with -t -u, we can show only the programs using tcp or udp
protocols.


Another approach is using `lsof -i`

```
$ lsof -i :8080
```

## show network interfaces

```
$ netstat -i
```


## show routing information

Using `-n`, we can suppress naming resolution.

```
$ netstat -r
```

## disable naming resolve

```
$ netstat -r -n
```
[^1]: http://www.thegeekstuff.com/2010/03/netstat-command-examples/
