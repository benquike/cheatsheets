#include <stdio.h>

int singleNumber(int* nums, int numsSize) {
    int c[32] = {0};
    int n = 0;
    for (int i = 0; i < 32; i++) {
        for (int j = 0; j < numsSize; j++) {
            if ((nums[j] >> i) & 0x1)
                c[i] ++;
        }
        if (c[i] % 3 != 0)
            n |= 0x1 << i;
    }
    
    return n;
}

int main() {
  int x[4] = {1,1,1,2};
  printf("%d\n", singleNumber(x, 4));
  return 0;
}
