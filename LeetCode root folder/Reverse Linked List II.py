class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = ListNode(0, head)
        res = prev
        count = 0
        while count + 1 < left:
            prev = prev.next
            count += 1

        newHead = prev
        cur = prev.next
        count += 1
        while count <= right:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            count += 1
        newHead.next.next = cur
        newHead.next = prev
        return res.next
