# brute force solution:18
# ms
# Beats
# 51.98%

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(treeNode, listNode):
            if listNode == None:
                return True
            if treeNode == None:
                return False

            if treeNode.val != listNode.val:
                return False

            return (
                    dfs(treeNode.left, listNode.next) or
                    dfs(treeNode.right, listNode.next)
            )

        def traverse(node):
            nonlocal head
            if node is None:
                return False
            if dfs(node, head):
                return True

            return (
                    traverse(node.left) or
                    traverse(node.right)
            )

        return traverse(root)