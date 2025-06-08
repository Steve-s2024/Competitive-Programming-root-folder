# brute force:5%
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        cur = head

        n = 1
        while cur:
            arr.append([])
            for i in range(n):
                arr[n-1].append(cur.val)
                cur = cur.next
                if cur is None:
                    break
            n+=1
        
        # print(arr)
        for i in range(len(arr)):
            n = i+1
            if len(arr[i]) % 2 == 0:
                arr[i] = arr[i][::-1]
        
        # print(arr)
        newHead = ListNode('tmp')
        cur = newHead
        for row in arr:
            for val in row:
                cur.next = ListNode(val)
                cur = cur.next

        return newHead.next