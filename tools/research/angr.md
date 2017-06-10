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


#### Execution Engine

Execution engines are used to `execute`(interpret, simulate)
the code(vex code) that is accociated with the current state(
the `ip` of the current state can be retrieved from the `ip` field
of SimState object, more information can be get from the `Scratch`
state plugin object).

The API that does the execution is `process` defined in SimEngine.
It takes a SimState object(s1) as argument, returns the possible states
after executing the basic block asscociated with s1. The possible states
are wrapped in `SimSuccessors` class.


![SimEngine](SimEngine.png)

Current implementations are:

- SimEngineVEX: this engine interprets the VEX code one by one.
- SimEngineUnicorn: this engine execute the code with Unicorn.
- ...


Some implementationd details:
1. Some common code is written in the parent class `SimEngine.process`, the different
implementations are in `_process` method, which takes a new state and a SimSuccessors
as argument.
2. In SimEngineVEX, `_process` first lift the binary code basic block to VEX IR
Super block, and invoke `_handle_irsb` to handle the superblock. After doing some
setup for the successors object, it iterates through all the statements in the
superblock and invoke `_handle_statement` to handle each VEX statement.
`_handle_statement` will further call `translate_stmt` which will call the
`process` method of each class representing the simulated IR statement.

![Sequence diagram of SimEngine.process](./SimEngine_process.png)


#### SimVexIR

This part is used to execute code represented in VEX IR and track
the constraints in symbolically execution.

![Class Diagram of SimIRStmt](./SimIRStmt.png)

![Class Diagram of SimIRExpr](./SimIRExpr.png)

Some implementation details:

1. SimIRStmt defines some common functions for its subclasses to reuse them:
   - \_translate\_expr
   - \_translate\_exprs
   - \_record\_expr
   - \_record\_exprs
   - \_add\_constraints
   - \_write_tmp

It exports `process` method to handle a VEX IR statement. The following is its
sequence diagram. `process` calls the `_execute` function of its subclasses which
takes an valina VEX IR expression and SimState as argument and construct a
corresponding SimIRExpr object(it is fully processed before being returned).


![Sequence diagram of SimIRStment.process](./SimIRStmt_process.png)

#### Plugins

Plugins are used to access information from a program state.
The system maintains all plugin implmentations in a `default_plugins`(defined
in plugins/plugin.py). All plugin implementation classes have a static method
that will register itself in `default_plugins`.

All plugins are subclasses of `SimStatePlugin`.

![SimStatePlugin](./SimStatePlugin.png)

Each plugin provides unique APIs to get information
associated with the plugin.

A SimState object has a field for for handling different aspects
of a program.

| FieldName  | Plugin Class           | Desc                   |
|------------|------------------------|------------------------|
| memory     |SimSymbolicMemory       | Symbolic memory        |
| mem        |SimMemView              | |
| register   |SimSymbolicMemory       | |
| regs       |SimRegNameView          | |
| libc       |SimStateLibc            | |
| posix      |SimStateSystem          | |
| solver\_engine(se) | SimSolver       | |
| cgc        | SimStateCGC            | |
| scratch    | SimStateScratch        | |
| log        | SimStateLog            | |
| procedure\_data| SimProcedureData    | |
| gdb        | GDB                    | |
| inspector  | SimInspector           | |
| unicorn    | Unicorn                | |
|uc\_manager  | SimUCManager           | |

##### SimSymbolicMemory and related

Important API:
- store: used to save a **value** to an **address** of some **size**;
- load: used to load a **value** from an **address** of some **size**;

Some of the internal API implementations:
1. `SimMemory.set\_state`: asssociate the SimState object with it by
   calling `SimStatePlugin.set\_state` and initialize `_stack_region_map` and
   and `_generic_region_map` passed from the constructor.
2. `SimMemory.\_resolve\_location_name`: get the location of registers, not complete?
3. `SimMemory.\_convert\_to\_ast`: convert `data_e` to an claripy ast expression, if it
   is a string or integer, create a bitvector for it, if it is a SimIRExpr, call its `to_bv`
   member function.
4. `SimMemory.set\_stack\_address\_mapping`:
5. `SimMemory.unset\_stack\_address\_mapping`:
6. `SimMemory.stack\_id`: Return a memory region ID for a function. If the
   default region ID exists in the region mapping, an integer will be appended
   to the region name, this is to handle recursive function calls.
7. `SimMemory.\_constrain_underconstrained\_index`: If the possible address
   (represented by passed in argument) range is beyond the predefined limit,
   add some constraints to the state.
   ([here](https://hexdump.cs.purdue.edu/source/xref/simuvex/simuvex/storage/memory.py#799)).
8. `SimMemory.store`: store a **value** to an **address** of some **size** and a **condition**,
   **value**, **address**, and **size** can be symbolic:
   - convert value, address, size and condition to symbolic expressions
   - call inpect
   - check the condition, if it does not hold under the state constraintsm, simply return
   - call `\_constrain_underconstrained\_index` to restrict the address
   - create a `MemoryStoreREquest` object and call `_store` method implementation in subclasses.
   - call inspect
   - handle actions

9. `SimMemory.store\_cases`: save value to a memory location with condition. it accept
   an address and a list of contents and a list of corresponding values to save to
   that address. In case the condition does not hold, we can provide a fallback value
   to write to that address, by default, the fallback value is the original value.
   - convert address, contents, codnitions and fallback to claripy ast
   - load the original value to be fallback if no fallback value is provided
   - call `\_store\_cases` to do the job
   - ....

10. `SimMemory.\_store\_cases`:
   - extend the size of each content to the max size
   - merge the conditions of the same contents and make a new constraint for the
     conditions by connecting all of them using `or` operator.
   - If there is only one content, same as `store` dose, create MemoryStoreRequest
     object and call `\_store`; if there are multiple contents, first simplify them;
     create a ite operation, create a MemoryStoreRequest for it and call `\_store`.

11. `SimMemory.load`: load contents from an address of size.
    - convert address, size, condition and fallback to a claripy ast.
    - call inspect
    - call `\_constrain_underconstrained\_index` to restrict the address
    - call `_load` and post handling
    - call inspect

12. `SimMemory.find`: returns the addresses of bytes equal to some value.
13. `SimMemory.copy\_contents`:


![Class Diagram of SimMemory](./SimMemory.png)

##### SimSolver

It is a wrapper for the functions provided by claripy.

It includes a constraints solver whose implementation
might vary depending on the configuration.

It exports functions to:
1. create variables(symbolic variables)
   - BVS
   - Unconstrained
2. add constraints
   - add
3. check satisfiability
4. extract solutions
5. constraints simplification
   - simplify

![Class Diagram of SimSolver](./SimSolver.png)


## claripy

This is a library for:
1. create symbolic variables
2. build AST and constraints from symbolic variables
3. solve the constraints and get solutions for expressions
