# notes for using fuzzer and related projects

## shellphish-afl

1. fail to install via pip
2. download the repo and try to install it by the setup.py script
prerequisite

```
$ sudo apt-get install gcc-5-base gcc-5-plugin-dev gcc-5-multilib
$ sudo apt-get install debootstrap debian-archive-keyring
```

the [patch](./patch.diff)

## installing fuzzer

Install angr

```
pip install angr
```

Install tracer, which is the concolic execution tool:

```
sudo apt-get build-dep qemu-system
sudo apt-get install libacl1-dev
pip install git+https://github.com/angr/tracer.git
```

Install shellphish-qemu and shellphish-afl

```
sudo apt-get install build-essential gcc-multilib libtool automake autoconf bison debootstrap debian-archive-keyring
sudo apt-get build-dep qemu
pip install git+https://github.com/shellphish/shellphish-qemu.git
pip install git+https://github.com/shellphish/shellphish-afl
```

Install fuzzer

```
pip install git+https://github.com/shellphish/fuzzer

```


## running the fuzzer

```
cd /sys/devices/system/cpu; echo performance | sudo tee cpu*/cpufreq/scaling_governor; cd -
echo 1 | sudo tee /proc/sys/kernel/sched_child_runs_first

shellphuzz -c 4 -d 2 -i ./YAN01_00015
```
