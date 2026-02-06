class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = []

        def recursive(hd):
            cr = hd
            while cr:
                ans.append(cr.val)
                recursive(cr.child)
                cr = cr.next

        recursive(head)
        res = Node()
        cr = res
        prv = None
        for v in ans:
            cr.next = Node(v, prv)
            prv = cr.next
            cr = cr.next

        # cr = res.next
        # while cr:
        #     print(cr.val)
        #     print(cr.next.val if cr.next else -1, cr.prev.val if cr.prev else -1)
        #     cr = cr.next
        return res.next