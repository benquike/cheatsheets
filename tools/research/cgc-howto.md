# CGC howtos

## using cgc-linux-dev vms

There are some VM image file and packages hosted
[here](https://repo.cybergrandchallenge.com/release-final/).
simply downowloading the Vagrantfile and vagrant up does
not work because the following error happens.

    cb: Downloading: http://s3.amazonaws.com/cgcdist/boxes/vm.json
    An error occurred while downloading the remote file. The error
    message, if any, is reproduced below. Please fix this error and try
    again.

    The requested URL returned error: 403 Forbidden


To solve this, first dowmload the vagrant box file to the local machine.
and add the box from the local file system.

```
$ wget https://cgcdist.s3.amazonaws.com/release-cfe/boxes/cgc-linux-dev.box
$ vagrant box add cgc-linux-dev cgc-linux-dev.box
```

Then goto where the Vagrantfile is and run `vagrant up`.
