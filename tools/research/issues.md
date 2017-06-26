# Issues with fuzzer, driller ...

## fuzzer is not able to tell the crashes correctly

It seems that it moves the crashes to another directory when
afl resumes. But in case that AFL starts from scratch, even
if there is some crashes found, it still reports an empty
list in from `crashes` method.
