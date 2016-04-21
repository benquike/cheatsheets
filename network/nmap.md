# nmap usage

## basic format

```
$ nmap [ScanType] [Options] {targets}
```

where **target** can be any of the following
- IP v4 address
- IP v6 address
- host name
- ip address range
- CIDR block
- a file containing a list of IP addresses

and **options** for target ports can be
    `-F`: scan 100 most popluar ports
    `-p<port1>-<port2>`: port range
    `-p<port1>, ..., <portn>`, port list
    `-pU:53, U:110, T20-445`: mix tcp and udp
    `-r` : scan linearly
  
References[^1][^2]

[^1]: https://8ack.de/dontpanic/NmapCheatSheetv1.0.pdf
[^2]: https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/
