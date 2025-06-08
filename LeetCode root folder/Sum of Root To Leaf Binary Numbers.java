//100%

class Solution {
    public int sumRootToLeaf(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int n) {
        if (node == null) return 0;
        n *= 2;
        n += node.val;
        int a = dfs(node.left, n);
        int b = dfs(node.right, n);
        if (node.left == null && node.right == null) return n;
        return a + b;
    }
}