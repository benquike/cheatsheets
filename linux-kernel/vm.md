# Linux virtual memory subsystem


## Linux configure and building

### console and serial port

During the boot process, console is the place that the kernel
dump the logging. And it is the place where users can login
the system.

To use the serial port as console, we need to do some configure
in the kconfig linux kernel.

To enable kernel to dump logs during to a console, we can set up a kernel
arguments named `console`, for example:

```
qemu-system-arm -M vexpress-a9 -cpu cortex-a9 -kernel uImage -drive file=oe-alip_vexpress.img,if=sd -append "root=/dev/mmcblk0p2 vga=normal rw console=ttyAMA0" -nographic
```

After the kernel boots, `getty` is used to run the `login` program to
allow user to login the system.

These are typically run by the `init` process.

## page cache and buffer cache

### controlling page cache

via /proc/sys/vm/drop_caches, we can force the system to
drop some of the memory used as cache[^1]

| value  |              description            |
|--------|-------------------------------------|
|   1    |  drop pagecache                     |
|   2    | drop inodes and dentires            |
|   3    | drop pagecache, dentries and inodes |

In case that `sudo echo 3 > /proc/sys/vm/drop_caches`
does not work, we can use this command:

	$ sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

[^1]: http://www.linuxinsight.com/proc_sys_vm_drop_caches.html
