

On Ubuntu Linux:

```
sudo apt-get install llvm
sudo apt-get install clang
sudo apt-get install libblocksruntime-dev
```

test.c:

```
#include <stdio.h>

int main() {
    void (^hello)(void) = ^(void) {
        printf("Hello, block!\n");
    };
    hello();
    return 0;
}
```

compile and run:

```
clang test.c -fblocks -lBlocksRuntime -o test
./test
```

Hello, block!


works fine.



https://stackoverflow.com/questions/5907071/clang-block-in-linux