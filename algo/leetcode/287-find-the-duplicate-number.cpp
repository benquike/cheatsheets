#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int countLess(vector<int> &nums, int x) {
        int ret = 0;
        for (int n:nums){
            if (n <= x)
                ret ++;
        }
        return ret;
    }

    int findDuplicate(vector<int>& nums) {
        int s= nums.size();
        int start = 1, end = s - 1;
        int m = (start + end)/2;

        while (start < end) {
            if (countLess(nums, m) > m) {
                end = m;
            } else {
                start = m + 1;
            }

            m = (start + end)/2;
        }

	return start;
    }
};

int main() {
  Solution s;
  static const int arr[] = {1, 2, 2, 3};
  vector<int> v(arr,  arr + sizeof(arr)/sizeof(arr[0]));
  cout << s.findDuplicate(v) << endl;
}
