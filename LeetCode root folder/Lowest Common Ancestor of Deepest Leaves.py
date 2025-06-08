# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        q = deque([root])
        depth = 0
        while q:
            l = len(q)
            while l:
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                l -= 1
            depth += 1
        ans = root
        minDepth = float('inf')

        def dfs(node, d):
            nonlocal minDepth, ans
            if node is None:
                return d == depth

            a = dfs(node.left, d + 1)
            b = dfs(node.right, d + 1)
            if a and b and d < minDepth:
                minDepth = d
                ans = node
            return a or b

        dfs(root, 0)
        return ans