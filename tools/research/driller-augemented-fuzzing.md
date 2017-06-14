# Driller augmented fuzzing


## Fuzzer Module

![Class Diagram of Fuzzer](./Fuzzer_class.png)

### AFL related run env management

| property name | description |
| --------------|-------------|
| binary\_path  | the target program to fuzz |
| work\_dir     | the working directory of the fuzzer |
| in\_dir       | input directory |
| out\_dir      | output directory |
| job\_dir      | job directory    |
| dictionary    | dictionary for fuzzing |
| resume        | whether in resuming mode |
|fuzz\_id       | the id|
| time\_limit   | run time limit |
| target\_opts  | the options for the target program |
| memory        | memory limit for the target program |
| crash\_mode   | if the fuzzer runs in crash mode |
| library\_path | the library paths |
| qemu          | use qemu for instrumentation |
| is\_multicb   | wether run in multi cb mode |
| stats         | get the state file content |

important methods:
- `_perform_env_checks`: check for cpu core pattern and cpu scaling setting
- `start`: start running afl
  - `_start_afl`
  - start timer
  - set `_on` to be true
- `kill`: stop fuzzing afl
- `add_fuzzer`: add one more fuzzing process
- `found_crash`: indicates whether there was some crash found
- `add_extension`:  start a mutation extension process(?)
- `queue`: get all the queue files
- `pollenate`: add all the testcases passed in the argument to the"pollen/queue"
   directory, in this way, the fuzzers are able to read in the testcases and
   influence the fuzzing process.
- `bitmap`: used to extract the bitmap of a fuzzer
- `crashes`: get all the crash inputs


Implementation details:

1. Fuzzer class uses a callback called `stuck_callback`, which is passed in from
the constructor. Internally, it uses a timer to call the callback
periodically[here](https://hexdump.cs.purdue.edu/source/xref/fuzzer/fuzzer/fuzzer.py#650).
In the callback, it get the queue files from the outputn directory of the fuzzer,
nremove the already drilled files from the queue, take one undrilled input and create a
driller worker thead and start it. In the driller thread, it calls `_run_drill` function,

In this function, it will create a new process using the following command:

```
timeout -k xxx+10 xxx python local_callback.py _binary_path, _fuzzer_out_dir, _bitmap_path, _path_to_input_to_drill
```
That is to say, the main function of [local_callback](https://hexdump.cs.purdue.edu/source/xref/driller/driller/local_callback.py)
will be called and in it the Driller algorithm is used to generate the new fuzzing inputs.

In this main function, it creates a `Driller` object and then use the `drill_generator`
to generate all the new inputs and then write them to `afl_output/driller/queue` directory.
