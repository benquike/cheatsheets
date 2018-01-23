#include <iostream>
using namespace std;

/**
 * Definition for a binary tree node.
 */ 
class TreeNode {
public:
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int max(int x, int y) {
        if (x > y)
            return x;
        return y;
    }
    int __maxPathSum(TreeNode *r, int &res) {
        if (r == NULL)
            return 0;
        
        int left = __maxPathSum(r->left, res);
        int right = __maxPathSum(r->right, res);

	int singleMax = max(r->val, max(r->val + left, r->val + right));
	cout << "res0:" << res << endl;
        res = max(res, max(r->val + left + right, singleMax));
	cout << "res1:" << res << endl;
	cout << "singleMax:" << singleMax << endl;
        return singleMax;
    }
    
    int maxPathSum(TreeNode* root) {
        int res = -0xFFFFFFFF;
        __maxPathSum(root, res);
        
        return res;
    }
};

int main() {
  //  TreeNode n1(1), n2(2), n3(3);
  // n1.left = &n2;
  // n1.right = &n3;

  TreeNode n1(0);
  Solution s;
  cout << s.maxPathSum(&n1) << endl;
  return 0;
}
