# dfs and mono-stack solution, very fast: 99%
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        i = 0
        arr = traversal.split('-')
        tmp = []
        prev = 0
        for i, e in enumerate(arr):
            if e != '':
                dif = i - prev
                tmp.append((dif, int(e)))
                prev = i

        stk = []
        for d, v in tmp:
            while stk and stk[-1][0] >= d: stk.pop()
            node = TreeNode(v)
            if stk:
                prt = stk[-1][1]
                if not prt.left: prt.left = node
                else: prt.right = node
            stk.append((d, node))

        return stk[0][1]

