# convert linked list into array, then array to bst
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next

        def recursive(l, r):
            if l > r:
                return None
            m = l + (r - l) // 2
            node = TreeNode(arr[m])
            node.left = recursive(l, m - 1)
            node.right = recursive(m + 1, r)
            return node

        return recursive(0, len(arr) - 1)