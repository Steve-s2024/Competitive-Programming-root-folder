// 40%
class Solution {
  unordered_map<int, vector<int>> graph;
  unordered_set<int> visited;
  vector<int> ans;
public:
  vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
      graph.clear();
      visited.clear();
      ans.clear();
      dfs(root, -1);
      visited.insert(target->val);
      bfs(target->val, k);
      return ans;
  }

  void dfs(TreeNode* node, int parent) {
      if (parent != -1) graph[node->val].push_back(parent);
      int cur = node->val;
      if (node->left != nullptr) {
          graph[cur].push_back(node->left->val);
          dfs(node->left, cur);
      }
      if (node->right != nullptr) {
          graph[cur].push_back(node->right->val);
          dfs(node->right, cur);
      }
  }

  void bfs(int cur, int dst) {
      if (dst == 0) {
          ans.push_back(cur);
          return;
      }
      int res = 0;
      for (int neighbor : graph[cur]) {
          if (visited.find(neighbor) == visited.end()) {
              visited.insert(neighbor);
              bfs(neighbor, dst-1);
          }
      }
  }
};
