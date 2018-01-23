#include <iostream>
#include <stack>
#include <vector>

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
    vector<int> postorderTraversal(TreeNode* root) {
        stack<TreeNode*> stk;
        vector<int> ret;
        TreeNode *t = root;

        while (!stk.empty() || t != NULL) {
            while (t != NULL) {
	      if (t->right != NULL)
		stk.push(t->right);
	      stk.push(t);
	      t = t->left;
            }
            
            if (stk.empty())
                break;
            t = stk.top();
            stk.pop();
            
	    if (!stk.empty() && t->right == stk.top()) {
	      stk.pop();
	      stk.push(t);
	      t  = t->right;
	    } else {
	      ret.push_back(t->val);
	      t = NULL;
	    }
        }
        
        return ret;
    }
};

int main() {

  TreeNode n1(1), n2(2), n3(3), n4(4), n5(5), n6(6);
  n1.left = &n2;
  n1.right = &n3;
  n2.left = &n4;
  n2.right = &n5;
  n3.left = &n6;

  Solution s;
  vector<int> ret = s.postorderTraversal(&n1);

  for (int i = 0; i < ret.size(); i++){
    cout << ret[i] << endl;
  }

  return 0;
}
