# linked list hard is not that hard...:0
# ms
# Beats
# 100.00%

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next

        for i in range(k-1, len(arr), k):
            j = i
            while j > i-k+1:
                arr[j].next = arr[j-1]
                j -= 1
            arr[j].next = arr[i+k] if i+k < len(arr) else (arr[i+1] if i+1 < len(arr) else None)

        return arr[k-1]