# this is soooo ugly, I have to keep putting little things on
# top of the solution and end up making it a piece of gibberish
# : 38%

class Solution:
    @staticmethod
    def getPath(node, arr, vis):
        l, r = node.left, node.right
        if l and l.val in vis and vis[l.val]:
            arr.append('L')
            Solution.getPath(l, arr, vis)
        elif r and r.val in vis and vis[r.val]:
            arr.append('R')
            Solution.getPath(r, arr, vis)

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        vis = {}
        def dfs(node):
            if node == None:
                return False
            if node.val == destValue:
                vis[node.val] = True
                return True

            vis[node.val] = (
                    dfs(node.left) or
                    dfs(node.right)
            )
            return vis[node.val]

        dfs(root)
        flag = True
        res = []
        vis2 = {}
        def dfs2(node):
            nonlocal flag
            if node is None:
                return False
            if node.val == startValue:
                vis2[node.val] = True
            else:
                vis2[node.val] = (
                    dfs2(node.left) or
                    dfs2(node.right)
                )
            if node.val in vis and vis[node.val] and vis2[node.val]:
                if flag:
                    flag = not flag
                    Solution.getPath(node, res, vis)
            elif vis2[node.val]:
                res.append('U')
            return vis2[node.val]
        dfs2(root)

        return ''.join(res)

