// this pointer thing in c++ is really complicated...
// when to use and when not to use them...

class Solution {
public:
	TreeNode* increasingBST(TreeNode* root) {
		vector<int> vals;
		dfs(root, vals);
		TreeNode* head = new TreeNode();
		TreeNode* cur = head;
		for (int val : vals) {
			cur->right = new TreeNode(val);
			cur = cur->right;
		}
		return head->right;
	}
private:
	void dfs(TreeNode* node, vector<int>& vals) {
		if (node == nullptr) {
			return ;
		}

		dfs(node->left, vals);
        vals.push_back(node->val);
		dfs(node->right, vals);
	}
};
