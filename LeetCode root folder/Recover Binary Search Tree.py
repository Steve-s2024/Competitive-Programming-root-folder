# brute-force

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # brute-force
        arr = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        large, small = arr[0], arr[0]
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                large = arr[i]
                break
        for i in range(len(arr)-1, 0, -1):
            if arr[i-1] > arr[i]:
                small = arr[i]
                break
        # print(small, large)
        def swap(node):
            if node is None:
                return
            if node.val == large:
                node.val = small
            elif node.val == small:
                node.val = large
            swap(node.left)
            swap(node.right)
        swap(root)