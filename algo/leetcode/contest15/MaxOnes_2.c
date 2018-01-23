#include <stdio.h>

int findMaxConsecutiveOnes(int* nums, int numsSize) {
  if (nums == NULL || numsSize == 0) {
    return 0;
  }

  int i = 0, j = 0 ,j1;
  int ret = 0, ret1;

  while (i < numsSize && nums[i] == 0) i ++;
  if (i == numsSize)
    return 1;

  // nums[i] is 1
  j = i+1;
  while (j < numsSize && nums[j] == 1) j ++;

  if (j == numsSize) {
    if (i == 0)
      return numsSize;
    else {
      // we can flip one
      return numsSize-i + 1;
    }
  } else if (j == numsSize - 1) {
    // there must be a 0
    return j-i + 1;

  } else {

    if (nums[j+1] == 0) {
      // one direction
      ret1 = findMaxConsecutiveOnes(&nums[j+1], numsSize - j - 1);
      return ret1 > j - i + 1 ? ret1:j - i + 1;
    } else {
      // the other
      j1 = j + 1;
      while (j1 <numsSize && nums[j1] == 1) j1++;

      if (j1 == numsSize) {
        return j1 - i;
      } else {
        ret = j1 - i;
        ret1 = findMaxConsecutiveOnes(&nums[j+1], numsSize - j - 1);
        return ret > ret1 ? ret : ret1;
      }
    }
  }
}


int main() {
  /* int arr1[] = {1,1,0,1,1,1}; */
  /* printf("%d\n", findMaxConsecutiveOnes(arr1,6)); */

  /* printf("%d\n", findMaxConsecutiveOnes(NULL,6)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr1,0)); */

  /* printf("%d\n", findMaxConsecutiveOnes(arr1,1)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr1,2)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr1,3)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr1,4)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr1,5)); */

  /* int arr2[] = {0,0,0,0,0,0}; */

  /* printf("%d\n", findMaxConsecutiveOnes(arr2,0)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr2,1)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr2,2)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr2,3)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr2,4)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr2,5)); */
  /* printf("%d\n", findMaxConsecutiveOnes(arr2,6)); */


  int arr3[] = {0,1,0,1,1,0, 1, 1, 1};

  printf("%d\n", findMaxConsecutiveOnes(arr3,0));
  printf("%d\n", findMaxConsecutiveOnes(arr3,1));
  printf("%d\n", findMaxConsecutiveOnes(arr3,2));
  printf("%d\n", findMaxConsecutiveOnes(arr3,3));
  printf("%d\n", findMaxConsecutiveOnes(arr3,4));
  printf("%d\n", findMaxConsecutiveOnes(arr3,5));
  printf("%d\n", findMaxConsecutiveOnes(arr3,6));
  printf("%d\n", findMaxConsecutiveOnes(arr3,7));
  printf("%d\n", findMaxConsecutiveOnes(arr3,8));
  printf("%d\n", findMaxConsecutiveOnes(arr3,9));

  return 0;
}
