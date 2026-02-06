# didn't notice it is a BST, so did a general algorithm work for all binary tree (inorder traversal encode and greedy stack decode)
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        ar = []

        def dfs(u):
            if not u:
                ar.append(' ')
                return
            ar.append(str(u.val))
            dfs(u.left)
            dfs(u.right)

        dfs(root)
        return ':'.join(ar)

    def deserialize(self, s: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not s: return None
        # print(s)
        ar = s.split(':')
        n = len(ar)
        stk = []
        for i in range(n - 1, -1, -1):
            if ar[i] == ' ':
                stk.append(None)
            elif len(stk) < 2:
                stk.append(TreeNode(int(ar[i])))
            else:
                a, b = stk.pop(), stk.pop()
                x = TreeNode(int(ar[i]))
                x.left = a
                x.right = b
                stk.append(x)
        return stk[0]