# gcov and related

## Merge multiple executions

use `lcov` to generate .info files and use lcov
we can merge multiple .info files.

First run a gcov instrumented program
and we run lcov to collect to coverage
info and save it in a.info

```
lcov -c --directory . -o a.info
```

Then we run another execution and
collect another coverage info in b.info.

```
lcov -c --directory . -o b.info
```

Then we add them together.

```
lcov -a a.info -a b.info -o all.info
```

Then we can use `genhtml` to visualize the results.

```
genhtml all.info --output-directory <html>
```

## reference
1. https://stackoverflow.com/questions/30833081/is-it-possible-to-merge-coverage-data-from-two-executables-with-gcov-gcovr
