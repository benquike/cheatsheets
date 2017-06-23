# systemd

## what is init

1. The first process in *nix systems which is responsible for starting all other processes.
2. the parent process of other processes
3. Manages services

Other similar tools: System V init, Upstart, launchd. See also http://elinux.org/Android_Booting
for android system.


## Usage

```
# systemctl {start|stop|restart|reload} servicename
```

### list all services

```
# systemctl --type service --state active
```

### enabling and disabling services



## adding a service

Create a service file and put it in /etc/systemd/system

example:[celery.service](./celery.service) and [celery.cfg](./celery.cfg)
...

After a new service is added, run the following cmd:

```
 sudo systemctl daemon-reload
```


## enable a service


```
sudo systemctl enable celery.service
```


## references

1. http://blu.org/meetings/2016/03/BLU-20160315-systemd.pdf
2. https://en.wikipedia.org/wiki/Systemd
3. https://linoxide.com/linux-how-to/systemd-boot-process/
4. https://www.suse.com/docrep/documents/huz0a6bf9a/systemd_in_suse_linux_enterprise_12_white_paper.pdf
5. [How To Use Systemctl to Manage Systemd Services and Units](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)
