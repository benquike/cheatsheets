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


Important methods:

- `dynamic_trace`: setup the shared memory and  run a binary instrumented with
  AFL compiler with the input. Check if the input triggers crashes or not, if
  it does, collect the addresses where crash happened.



## Driller

Driller is the tool that augment fuzzing of AFL by symbolic
execution.
