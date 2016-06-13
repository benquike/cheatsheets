# Linux virtual memory subsystem

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
