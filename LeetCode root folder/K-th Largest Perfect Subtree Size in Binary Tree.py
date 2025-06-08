# recursive solution, post order traversal:60
# ms
# Beats
# 17.70%
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def checkPBT(node):
            if node is None:
                return 0

            if (
                    (node.left and node.right) or
                    (node.left is None and node.right is None)
            ):
                l = checkPBT(node.left)
                r = checkPBT(node.right)
                if l == r and l != -float('inf'):
                    # two subtree are both perfect, return their depth
                    arr.append(2 * l + 1)
                    return 2 * l + 1
                else:
                    # not perfect
                    return -float('inf')
            else:
                # not perfect, but one of the subarray may be perfect
                checkPBT(node.left)
                checkPBT(node.right)
                return -float('inf')

        checkPBT(root)
        if k <= len(arr):
            return sorted(arr)[-k]
        else:
            return -1