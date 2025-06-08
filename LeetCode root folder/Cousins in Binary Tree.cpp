//100%
class Solution {
  public:
      bool isCousins(TreeNode* root, int x, int y) {
          deque<TreeNode*> q;
          q.push_back(root);
          int level = 0;
          int mark = -1;
          while (q.size() > 0) {
              int l = q.size();
              while (l-- > 0) {
                  TreeNode* cur = q[0];
                  if (cur->val == x || cur->val == y) {
                      if (mark == -1) mark = level;
                      else return mark == level;
                  }
                  q.pop_front();
                  if (cur->left != nullptr && cur->right != nullptr) {
                      int a = cur->left->val, b = cur->right->val;
                      if (a == x && b == y || a == y && b == x) return false;
                  }
                  if (cur->left != nullptr) q.push_back(cur->left);
                  if (cur->right != nullptr) q.push_back(cur->right);
              }
              level++;
          }
          return true;
      }
  };