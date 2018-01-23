#include <iostream>
#include <vector>
#include <priority_queue>

using namespace std;

class Solution {
public:
  vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    vector<double> ret;

    if (k == 1) {
      // todo it later
    }

    if (nums.size() < k) {
      return ret;
    }

    int half  = nums.size()/2;
    int l1 = half, l2 = half;
    bool even = true;

    if (half * 2 < nums.size()) {
      l1 = half + 1;
      even = false;
    }

    priority_queue<int> heap1;
    priority_queue<int, greater<int> > heap2;

    for (int i = 0; i < k; i ++) {
      heap1.push(nums[i]);
      if (heap1.size() > l1) {
        int x = heap1.top();
        heap1.pop();
        heap2.push(x);
      }
    }

    if (even) {
      ret.push_back(((double)(heap1.top() + heap2.top()))/2);
    } else{
      ret.push_back((double) heap1.top());
    }

    for (int i = k; i < nums.size(); i++) {
      heap1.push(nums[i]);
      int x = heap1.top();
      heap1.pop();

      
    }
  }
};
