# Angr source study

## simvex

This is the package that is able to "execute" or simulate
program in the VEX format.

### concept

#### Mode

It is able to simulate program in symbolically and concretely.
This is called execution mode.

#### Program State

Program state is tracked using `SimState` class, including:
- register values
- memory values
- file system

Other important/interesting features of the program state is provided
via `Plugins`, including:

- regs: accessing registers
- mem: accessing memory
- se: constraint solver engine
- log:
- inspect: breakpoint mananger
- posix: some features defined in posix
- scratch: information about the current state
- libc: information of the c library
- cgc: information about the cgc environment
- unicorn: control of the unicorn engine
- uc_manager:

The class diagram is as follows:

![Class Diagram](./SimState.png)

#### Plugins

Plugins are used to access information from a program state.
The system maintains all plugin implmentations in a `default_plugins`(defined
in plugins/plugin.py). All plugin implementation classes have a static method
that will register itself in `default_plugins`.

All plugins are subclasses of `SimStatePlugin`.

![SimStatePlugin](./SimStatePlugin.png)

