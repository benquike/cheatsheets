#include <iostream>
using namespace std;

class TreeNode {
public:
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int countNodes(TreeNode* root) {
        TreeNode *t = root;
        int rl =0, ll = 0;
        
        if (root == NULL)
            return 0;
        
        while (t != NULL) {
            ll ++;
            t = t -> left;
        }
        t = root;
        while (t != NULL) {
            rl ++;
            t = t->right;
        }

        cout << "ll:" << ll << ", rl:" << rl << endl;
        if (ll == rl) {
            return (1 << ll) - 1;
        } else {
            return countNodes(root->left) + countNodes(root->right)  + 1;
        }
    }
};

int main() {
  TreeNode n1(1);
  TreeNode n2(2);
  n1.left = &n2;
  Solution s;
  cout << s.countNodes(&n1) << endl;

  return 0;
}
