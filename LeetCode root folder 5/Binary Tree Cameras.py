# funny solution, bottom up (begin from leaf) greedily installing camera solution: 100%
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right: return 1
        cnt = 0
        def dfs(node):
            nonlocal cnt
            if not node.left and not node.right: return 'leaf'
            a, b = None, None
            if node.left: a = dfs(node.left)
            if node.right: b = dfs(node.right)
            if a == 'leaf' or b == 'leaf':
                cnt += 1
                return 'camera'
            if a == 'camera' or b == 'camera': return 'gap'
            if a == 'gap' or b == 'gap': return 'leaf'
        if dfs(root) == 'leaf': cnt += 1
        return cnt
