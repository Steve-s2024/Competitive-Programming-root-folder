# so boring, just implementing bfs

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = deque([root])
        while q:
            res.append([])
            l = len(q)
            while l:
                node = q.popleft()
                res[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                l -= 1
        return res[::-1]