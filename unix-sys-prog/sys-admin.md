# Linux System administration

## zombie process
A zombie process is a dead process, but because
its parent is still live and not call wait on it.

It is actually a bug in the program. If a daemon
program pawns a lot processes and does not wait
on the child processes, those PCBs can not be reused.

To release the PCBs of zombie processes, we need to
kill their parent process and make init process their
parent, and init process will wait on them and release
the PCBs used by them.

This is the command to do this:

```
$ kill $(ps -A -ostat,ppid | awk '/[zZ]/{print $2}')
```

The difference between orphan process and zombie process(https://www.cs.princeton.edu/courses/archive/fall11/cos217/precepthandouts/22shell/orphanzombie.pdf)

## iptables
iptables is a powerful firewall tool on linux[^1][^3][^4].

### port forwarding

#### forward multiple ports to one port
This is very important in doing CTF challenges related to
port knocking.

This is the command[^2]:

```
$ iptables -t nat -A PREROUTING -p tcp --dport 1:65535 -j REDIRECT --to-ports 10000
```

[^1]: http://www.howtogeek.com/177621/the-beginners-guide-to-iptables-the-linux-firewall/
[^2]: http://superuser.com/questions/440324/iptables-how-to-forward-all-external-ports-to-one-local-port
[^3]: https://help.sakura.ad.jp/app/answers/detail/a_id/2423/~/iptables%E3%81%AE%E8%A8%AD%E5%AE%9A%E6%96%B9%E6%B3%95
[^4]: http://www.atmarkit.co.jp/flinux/index/indexfiles/iptablesindex.html
