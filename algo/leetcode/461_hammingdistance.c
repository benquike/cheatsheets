#include <stdio.h>

int hammingDistance(int x, int y) {
    int xor = x ^ y;
    int n = 0;
    while (xor ^ (xor - 1)) {
        xor = xor ^ (xor - 1);
        n++;
    }

    return n;
}

int main() {
  int x = 1;
  int y = 4;

  printf("%d", hammingDistance(x, y));

  return 0;
}
