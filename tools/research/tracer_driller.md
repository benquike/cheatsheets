# Driller and Tracer

![Driller and Tracer](./Driller_And_Tracer.png)

## Tracer

Tracer is the tool to trace the program concretely.

Important Fields:

| field name  | description |
|-------------|-------------|
|binary       |the path to the program to analys|
|input        |the input to feed in the program |
|argv         | |
|....         | ...|
| os          | the name of the os |
| base        | the base directory of shellphish qemu |
| tracer_qemu | the file name of the qemu |
| tracer_qemu_path | the directory of the qemu |
| crash\_mode | |
| crash\_addr | |
| crash\_state| |
| trace       | the list of addresses of code blocks that were executed |

Important methods:

- `dynamic_trace`: setup the shared memory and  run a binary instrumented with
  AFL compiler with the input. Check if the input triggers crashes or not, if
  it does, collect the addresses where crash happened.

- `next_branch`: move the current path to the next node along the path.

- `run`: trace the program symbolically along the trace of the input until
  it finds a deadend.


Coding sample:

To start a tracer,
```python
import tracer
input = file('/dev/shm/work/KPRCA_00064/sync/fuzzer-master/queue/id:000007,src:000000,op:ext_UI,pos:0,+cov').read()
t = tracer.Tracer('KPRCA_00064/bin/KPRCA_00064', input=input)
```

In this setting, the tracer will run the program `KPRCA_00064/bin/KPRCA_00064` and
the program will read `stdin` from the input, it is like running the following cmd:

```
$ KPRCA_00064/bin/KPRCA_00064 < /dev/shm/work/KPRCA_00064/sync/fuzzer-master/queue/id:000007,src:000000,op:ext_UI,pos:0,+cov
```

If we want to add more options to the program, we can use
the `add_options` named argument in the constructor.

In the constructor, it will run `dynamic_trace` and colllect the list of basic blocks
exercised during the execution of the target program with the input the addresses
of the basic blocks are saved in the `traces` field. And if the input caused a
crash, it will also save the crash address.

```
print t.trace

[134530765,
 134531030,
 134531078,
 134531096,
 ....
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 134531096,
 ...]
```

```python
import tracer
samplefile  =  "/dev/shm/work/CADET_00003/sync/fuzzer-master/crashes/id:000000,sig:11,src:000000,op:havoc,rep:64"
f = file(samplefile)
input = f.read()
t = tracer.Tracer('CADET_00003/bin/CADET_00003', input=input)

print t.crash_addr
>>> 134513508

print t.trace
    [134514172,
    134514437,
    134514485,
    134514503,
    134514503,
    134514503,
    134514503,
    ....
    134514503,
    134514503,
    134514503,
    134514503,
    134514503,
    134514503,
    ...]
```

In the constructor it will also prepare the `path_group` variable,
which contains a state at address at the first address in the trace.
Preparing the first `path_group` varible is done in `_prepare_paths`
method, which will call others different methods depending on the OS.
There are a lot of detailed setup in those methods, among which the most
important few of them are:
1. create a project
2. setup the project
3. create a path group using `full_init_state`
4. proceed the execution of the state to go to the entry address of the target program

```
import tracer
samplefile  =  "/dev/shm/work/CADET_00003/sync/fuzzer-master/crashes/id:000000,sig:11,src:000000,op:havoc,rep:64"
f = file(samplefile)
input = f.read()
t = tracer.Tracer('CADET_00003/bin/CADET_00003', input=input)

first = t.path_group.active[0]
assert first.addr == self._p.entry
```


## Driller

Driller is the tool that augment fuzzing of AFL by symbolic
execution.

Driller iteratively calls `next_branch` method of tracer, along the path,
find the constraints of the missed nodes and solve those constraints to
generate inputs that will trigger execution along the missed paths.
