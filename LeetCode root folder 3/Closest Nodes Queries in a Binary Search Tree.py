# boring question, does not do with BST at all, don't know why they make
# bring BST in: 60%
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        q = deque([root])
        while q:
            node = q.popleft()
            arr.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        arr.sort()
        n = len(arr)
        ans = []
        for i, q in enumerate(queries):
            l, r = 0, n - 1
            left = right = -1
            while l <= r:
                m = (l + r) // 2
                if arr[m] == q:
                    left = right = m
                    break
                elif arr[m] < q:
                    left = m
                    l = m + 1
                else:
                    right = m
                    r = m - 1
            ans.append([arr[left] if left != -1 else -1, arr[right] if right != -1 else -1])
        return ans


# thought the input will be balanced tree, guess not: TLE
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        n = len(queries)
        ans = [[-1, -1]] * n
        for i, q in enumerate(queries):
            mi, mx = -1, -1
            node1, node2 = root, root
            while node1:
                if node1.val <= q:
                    mi = node1.val
                    node1 = node1.right
                else:
                    node1 = node1.left
            while node2:
                if node2.val >= q:
                    mx = node2.val
                    node2 = node2.left
                else:
                    node2 = node2.right

            ans[i] = [mi, mx]
        return ans