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
    int lca(TreeNode *r, TreeNode *p, TreeNode *q, TreeNode **res) {
        if (r == NULL) {
            return 0;
        }
        
        if (p == q) {
            *res = p;
            return 2;
        }
        
        int left = lca(r->left, p, q, res);
        int right = lca(r->right, p, q, res);
        
        if (left == 0 && right == 0) {
            if (r == p || r == q) {
                return 1;
            }
            return 0;
        }
        
        if (left != 0 && right == 0) {
            if (left == 1) {
                if (r == p || r == q) {
                    *res = r;
                    return 2;
                } else {
                    return 1;
                }
            }
            return 2;
        }
        
        if (left == 0 && right != 0) {
            if (right == 1) {
                if (r == p || r == q) {
                    *res = r;
                    return 2;
                } else {
                    return 1;
                }
            }
            return 2;
        }
        
        *res = r;
        return 2;
            
    }

    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode *res = NULL;
        
        lca(root, p, q, &res);
        
        return res;
    }
};


int main() {
  TreeNode n1(1), n2(2);
  n1.left = &n2;

  Solution s;
  TreeNode * x = s.lowestCommonAncestor(&n1, &n1, &n2);
  cout << x->val << endl;
  return 0;
}
