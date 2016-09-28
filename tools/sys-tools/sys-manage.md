# System management

## auto start a service

1. sudo update-rc.d <SERVICE_NAME> defaults
2. sudo update-rc.d <SERVICE_NAME> enable


## LDAP

LDAP is a standardized service to manage hierarchical information.

### Concepts

DN and RDN:


## managing block device

### get the block uuid

```
sudo blkid
```

### get more detailed info of blocks

```
sudo lsblk -f
```

## sudo

remove the password of sudo[^1].

## Ref
*[Install OpenLDAP In Ubuntu 15.10 And Debian 8](https://www.unixmen.com/install-openldap-in-ubuntu-15-10-and-debian-8/)
*[OpenLDAP Server](https://help.ubuntu.com/lts/serverguide/openldap-server.html)
*[How To Install and Configure OpenLDAP and phpLDAPadmin on an Ubuntu 14.04 Server](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-openldap-and-phpldapadmin-on-an-ubuntu-14-04-server)

[^1]: http://askubuntu.com/questions/235084/how-do-i-remove-ubuntus-password-requirement
