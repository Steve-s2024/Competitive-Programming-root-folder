class Solution:
    def deleteNode(self, node):
        # swap the value of node and node.next
        tmp = node.val
        node.val = node.next.val
        node.next.val = node.val
        # remove node.next from the linked list
        node.next = node.next.next
