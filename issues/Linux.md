# Issues found in Linux

## strcpy

If there is a byte `0xb0`, all the bytes after it won't be copied.

The following code output `aaaaaaaaaaaaaaaaaaa`

```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	char *stra = "aaaaaaaaaaaaaaaaaaa\xb0bbbbbbbbbbbbbbbbbbbbb";
	char strb[100];
	memset(strb, 0, 100);

	strcpy(strb, stra);
	printf("%s\n", strb);

	return 0;
}

```
