#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    void findAllPerm(vector<int> &nums, vector<int> &perm, vector< vector<int> > &all) {
        if (nums.size() == 0) {
            all.push_back(perm);
            return;
        }
        
        for (int  i = 0; i < nums.size(); i ++) {
	    int x = nums[i];
            perm.push_back(x);
            nums.erase(nums.begin() + i);
            findAllPerm(nums, perm, all);
            nums.insert(nums.begin() + i, x);
            perm.pop_back();
        }
    }
    vector< vector<int> > permute(vector<int>& nums) {
        vector< vector<int> > ret;
        vector<int> p;
        findAllPerm(nums, p, ret);

        return ret;
    }
};

int main() {
  int x[] = {1,2,3,4,5};
  vector<int> v(x, x + sizeof(x)/sizeof(x[0]));

  Solution s;
  vector< vector<int> > r = s.permute(v);

  for (int i = 0; i < r.size(); i ++) {
    for (int  j = 0; j < r[i].size(); j ++) {
      cout << r[i][j] << ' ';
    }
    cout << endl;
  }

  return 0;
}
