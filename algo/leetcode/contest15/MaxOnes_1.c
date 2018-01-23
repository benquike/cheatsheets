#include <stdio.h>

int findMaxConsecutiveOnes(int* nums, int numsSize) {
  if (nums == NULL || numsSize == 0) {
    return 0;
  }

  int i = 0, j = 0;
  int ret = 0;
  while (i < numsSize) {
    while (i < numsSize && nums[i] == 0) i ++;
    if (i == numsSize)
      return 0;

    // nums[i] is 1
    j = i+1;
    while (j < numsSize && nums[j] == 1) j ++;

    if (ret < j - i)
      ret = j - i;
    i = j;
  }

  return ret;
}


int main() {
  int arr1[] = {1,1,0,1,1,1};
  printf("%d\n", findMaxConsecutiveOnes(arr1,6));

  printf("%d\n", findMaxConsecutiveOnes(NULL,6));

  printf("%d\n", findMaxConsecutiveOnes(arr1,0));
  printf("%d\n", findMaxConsecutiveOnes(arr1,1));
  printf("%d\n", findMaxConsecutiveOnes(arr1,2));
  printf("%d\n", findMaxConsecutiveOnes(arr1,3));
  printf("%d\n", findMaxConsecutiveOnes(arr1,4));
  printf("%d\n", findMaxConsecutiveOnes(arr1,5));

  int arr2[] = {0,0,0,0,0,0};

  printf("%d\n", findMaxConsecutiveOnes(arr2,0));
  printf("%d\n", findMaxConsecutiveOnes(arr2,1));
  printf("%d\n", findMaxConsecutiveOnes(arr2,2));
  printf("%d\n", findMaxConsecutiveOnes(arr2,3));
  printf("%d\n", findMaxConsecutiveOnes(arr2,4));
  printf("%d\n", findMaxConsecutiveOnes(arr2,5));
  printf("%d\n", findMaxConsecutiveOnes(arr2,6));
  
  return 0;
}
