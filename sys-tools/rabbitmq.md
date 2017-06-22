# rabbitmq setup

## clustering

selectint one node as master

1. copy the key on the master to all slave nodes.

```
cat sudo cat /var/lib/rabbitmq/.erlang.cookie
```

2. on each slave node run the following cmd

```bash
# hexfuzz-node01 is the master
sudo rabbitmqctl stop_app
sudo rabbitmqctl join_cluster --ram rabbit@hexfuzz-node01
sudo rabbitmqctl start_app
```


## referenece

1. http://linuxpitstop.com/rabbitmq-cluster-on-centos-7/
