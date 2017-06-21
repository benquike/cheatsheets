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


## how to run gcov on the challenges

The cgc platform does not have support for files
thus gcov support is not complete.

But the compiler has the function for instrumenting
the programs for collecting the coverage.

We have done some patch for collecting gcov information
on the challenges.

1. install gcc of lower version because the instrumentation
   in the compiler of the cgc os only supports old version of
   gcov info.

Add apt source with gcc-4.4
```
# add the following 2 lines to /etc/apt/sources.list
deb http://dk.archive.ubuntu.com/ubuntu/ trusty main universe
```

Install gcc-4.4
```
sudo apt-get update
sudo apt-get install gcc-4.4
```

Make `gcov-4.4` the default `gcov`
```
cd /usr/bin/
sudo rm gcov
sudo ln -s gcov-4.4 gcov
```

2. build and install a new version of libcgc
   Get and install the patched libgcg

    Run the building on the VM.

```
git clone https://github.com/benquike/libcgc.git
cd libcgc

# run those command on the vm
make
sudo make install
```

3. build the challenge with gcov support
   To build it with GCOV support, first we need an updated
   [cgc-cb.mk](./cgc-cb.mk) and replace the old one `/usr/share/cb-testing/cgc-cb.mk`

    when building the challenge, the the following command:

    ```
    make build GCOV=1
    ```


4. run the challenge and collect coverage information

    As there is no file system API support in cgc, we need to use
    gdb to collect the coverage data.
    there is a [script](./cmd_example.py) for doing this.

```
gdb <bin/challege_name>

# in GDB
source cmd_example.py
run < input
quit
```

After these, all the coverage data is written to the gcda files.

5. visualize the coverage

    Change directory (`cd`) to the root of the challange
    run the following cmd:

```
lcov --capture --directory . --output-file coverage.info
genhtml coverage.info --output-directory <html>
```

<html> is the place to put the gernated html file


6. Run [cmd_example.py](./cmd_example.py) automatically

Put `cmd_example.py` somewhere in the file system.

Put the following line in `~/.gdbinit`

```
source <PATH_TO_cmd_example.py>
```

And to run cmd_example.py automatically via gdb to collect
the coverage information, SET the following environmental
variables:

```
export GDB_AUTO_EXEC="1"
export GDB_BIN_FILE="bin/KPRCA_00064"
export GDB_INPUT_FILE="/vagrant/KPRCA_00064_queue/id:000079,src:000015,op:havoc,rep:8,+cov"
```

## how to detect the checksum problems

Which challenges have checksum issue?
