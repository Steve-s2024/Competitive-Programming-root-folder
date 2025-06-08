# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(-float('inf'), head)
        nodes = [newHead]
        cur = head
        while cur:

            idx = len(nodes) - 1
            while nodes[idx].val > cur.val:
                idx -= 1
            if idx != len(nodes) - 1:  # if move the node
                nodes[-1].next = cur.next  # assign cur.prev.next = cur.next
                nodes[idx].next = cur
                cur.next = nodes[idx + 1]
                nodes.insert(idx + 1, cur)
            else:  # if don't move the node
                nodes[-1].next = cur
                nodes.append(cur)
            cur = nodes[-1].next  # reassign the cur for next operation

        return nodes[0].next