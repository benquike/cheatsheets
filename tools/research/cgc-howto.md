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

What's available on the VMs are summarized hereL:

https://github.com/CyberGrandChallenge/cgc-release-documentation/blob/master/walk-throughs/running-the-vm.md

Checking the ABI and GCC executable format:

    man cgcabia
    man cgc_executable_format


## details of writing challenges

https://github.com/CyberGrandChallenge/cgc-release-documentation/blob/master/walk-throughs/building-a-cb.md

Important parts:

`PATCHED_` macros: are used to facilitate the building of vulnerable and corresponding
secure binaries.

`Partial`: a binary that is only partially patched. If a binary has multiple vulerabilities and
it is only patched to fix some (not all) of the vulerabilities, it is called partially patched.

`Poll`: what are polls?

`PoV`: what are proof of verification/vulerability?

## cgc toolchain

`file`: detect the magic of files, able to detect cgc executable format.

    file CROMU_00001/bin/CROMU_00001
    CROMU_00001/bin/CROMU_00001: CGC 32-bit LSB executable, (CGC/Linux)


`readcgcef`: read information from the cgc executable file, much like `readelf`.

`cgc2elf`: convert a cgc executable to an elf file.


Know-hows:

Preventing the default building system from stripping the binaries
of the CGC.

In `/usr/share/cb-testing/cgc-cb.mk`, remove the `-s` option

    $(RELEASE_PATH): $(RELEASE_OBJS)
        $(LD) $(LDFLAGS) -s -o $(RELEASE_PATH) -I$(BUILD_DIR)/$(RELEASE_DIR)/lib $^ $(LIBS)

==>

    $(RELEASE_PATH): $(RELEASE_OBJS)
        $(LD) $(LDFLAGS) -o $(RELEASE_PATH) -I$(BUILD_DIR)/$(RELEASE_DIR)/lib $^ $(LIBS)


## how to build the samples

[corpus sources](https://github.com/lungetech/cgc-challenge-corpus)

Download the corpus repo to the vm and run make under each directory
of the challenge.

During the building, it will connect to the server and because they are not setup
it won't succeed. but it is ok.

[cgc-cb.mk](./cgc-cb.mk)

by default it will run the `build` and `test` targets.

The `build` target runs the following dependent targets:

- build
  - prep
  - release
  - patched
  - pov
  - build-partial

or

- build
    - prep
    - build-binaries
    - pov


`test` target runs build and `check` targets.

- generate:
  - generate-polls
  then run the polls using `cb-test` program.




## classifying the samples



## how to detect the checksum problems

Which challenges have checksum issue?
