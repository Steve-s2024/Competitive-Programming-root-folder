# too slow?? its nlongn. isn't it?
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SumTree:
    @staticmethod
    def build(l, r):
        if l >= r:
            return Node()
        node = Node()
        m = (l + r) // 2
        node.left = SumTree.build(l, m)
        node.right = SumTree.build(m + 1, r)
        return node

    @staticmethod
    def update(l, r, num, node):
        if l == r == num:
            node.val += 1
            return
        m = (l + r) // 2
        if m >= num:
            SumTree.update(l, m, num, node.left)
        else:
            SumTree.update(m + 1, r, num, node.right)
        node.val += 1

    @staticmethod
    def getSum(l, r, L, R, node):
        if r < L or R < l:
            return 0
        if L <= l and r <= R:
            return node.val
        m = (l + r) // 2
        return (
                SumTree.getSum(l, m, L, R, node.left) +
                SumTree.getSum(m + 1, r, L, R, node.right)
        )

    @staticmethod
    def undo(l, r, num, node):
        if l == r == num:
            node.val -= 1
            return
        m = (l + r) // 2
        if m >= num:
            SumTree.update(l, m, num, node.left)
        else:
            SumTree.update(m + 1, r, num, node.right)
        node.val -= 1


class Solution:
    def __init__(self):
        self.MAX = 100005
        self.tree = SumTree.build(1, self.MAX)

    def createSortedArray(self, instructions: List[int]) -> int:
        MAX = self.MAX
        tree = self.tree

        res = 0
        for num in instructions:
            a = SumTree.getSum(1, MAX, 1, num - 1, tree)
            b = SumTree.getSum(1, MAX, num + 1, MAX, tree)
            SumTree.update(1, MAX, num, tree)
            res += min(a, b)
            res %= 10 ** 9 + 7

        # clean the tree by undo the update process, linear time, no issue
        for num in instructions:
            SumTree.undo(1, MAX, num, tree)
        return res

