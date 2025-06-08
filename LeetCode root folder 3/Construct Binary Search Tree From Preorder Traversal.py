# mono-stack solution, kinda hard to come up with:100%
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        stack = [TreeNode(float('inf'))]
        n = len(preorder)
        mp = {}
        for i in range(n):
            node = TreeNode(preorder[i])
            mp[preorder[i]] = node
            val = None
            while stack and stack[-1].val < preorder[i]:
                val = stack.pop()
            if val:
                val.right = node
            else:
                stack[-1].left = node
            stack.append(node)
        return mp[preorder[0]]



# kinda hard with recursion, cause I don't know the mono-stack
# approach: 15%
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        i = 0
        n = len(preorder)
        def build(l, r):
            nonlocal i, n
            if i >= n-1:
                return TreeNode(preorder[i])
            a, b = preorder[i], preorder[i + 1]
            node = TreeNode(a)
            if b in range(l+1, r):
                if b < a:
                    i += 1
                    node.left = build(l, a)

            if i >= n-1:
                return node
            a, b = preorder[i], preorder[i + 1]
            if b in range(l+1, r):
                if b > a:
                    i += 1
                    node.right = build(a, r)
            return node

        return build(-10**10, 10**10)




