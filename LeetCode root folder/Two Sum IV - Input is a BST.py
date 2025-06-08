class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashSet = set()
        def dfs(node):
            if node is None:
                return False
            if k - node.val in hashSet:
                return True
            hashSet.add(node.val)
            return (
                dfs(node.left) or
                dfs(node.right)
            )
        return dfs(root)