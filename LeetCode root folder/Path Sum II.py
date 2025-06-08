class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, seq, sum_):
            nonlocal targetSum
            if node is None:
                return
            sum_ += node.val
            seq.append(node.val)
            if node.left is None and node.right is None:
                if sum_ == targetSum:
                    res.append(seq)
                return
            dfs(node.left, seq[:], sum_)
            dfs(node.right, seq[:], sum_)
        dfs(root, [], 0)
        return res