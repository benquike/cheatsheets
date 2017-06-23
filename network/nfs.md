# nfs setup

## install nfs server

```
apt-get install nfs-kernel-server
```

## bind directories

Add the following lines to /etc/fstab
```
/home/users    /export/users   none    bind  0  0
```

remount all entries in /etc/fstab

```
mount -a
```


## export directories on the server side

In `/etc/exports` add the following lines

```
/export       192.168.1.0/24(rw,fsid=0,insecure,no_subtree_check,async)
/export/users 192.168.1.0/24(rw,nohide,insecure,no_subtree_check,async)
```

Restart nfs server

```
service nfs-kernel-server restart
```


## client side

Install nfs support

```
apt-get install nfs-common
```

add the following line to /etc/fstab

```
<nfs-server-IP>:/   /mnt   nfs    auto  0  0
```

## reference

1. https://help.ubuntu.com/community/SettingUpNFSHowTo
