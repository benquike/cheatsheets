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

## Driller

Driller is the tool that augment fuzzing of AFL by symbolic
execution.

Driller iteratively calls `next_branch` method of tracer, along the path,
find the constraints of the missed nodes and solve those constraints to
generate inputs that will trigger execution along the missed paths.
