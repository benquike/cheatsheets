# netcat usage

## use netcat as a tcp/udp client

by default,nc uses tcp, using `-u`, we can ask nc to us udp.
Using -p, we can specify the source port to use  and using `-s`
we can specify the local IP address to use
```
$ nc [-u] <ip> port using -p <source port> -s <source ip>
```

## use netcat as a tcp/udp server

```
$ nc [-u] -l <ip> port
```

## use netcat to do port scan

```
$ nc -z <ip> 20-30
```

will scan the ports from 2- to 30 on machine specified by `ip`, `-z`
means that nc should scan for listening daemon without sending any
data to the server.


## Data transfer

receiving data

```
$ nc -l port > filename.in
```

sending data

```
$ nc ip port < filename.in
```

```
$nc localhost 25 << EOF
HELO host.example.com
MAIL FROM: <user@host.example.com>
RCPT TO: <user2@host.example.com>
DATA
Body of email.
.
QUIT
EOF
```
