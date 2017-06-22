# corpus analysis


## KPRCA_00064

In handling compress, it asks for a KEY of length 95 from the user.
There is strict check on the key(see [here](https://github.com/benquike/cgc-challenge-corpus/blob/master/KPRCA_00064/src/main.c#L51]):
1. all of them must fall between 32 and 126
2. there must be no duplicates

This makes the fuzzing approach highly unlikely to get the vulnerable code.

>> These constraints should be easy to solved by the symbolic execution engine?
>> Why Driller does not help in solving the issue?
