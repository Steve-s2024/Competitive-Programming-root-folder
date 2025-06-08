# segment tree question, so segment tree solution:959
# ms
# Beats
# 37.50%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NumArray:
    def __init__(self, nums: List[int]):
        self.arr = nums
        self.length = len(nums)
        self.sumTree = self.build(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.updateTree(0, self.length - 1, index, val, self.sumTree)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(0, self.length - 1, left, right, self.sumTree)

    def build(self, l, r):
        if l >= r:
            return TreeNode(self.arr[l])
        m = (l + r) // 2
        a = self.build(l, m)
        b = self.build(m + 1, r)
        return TreeNode(a.val + b.val, a, b)

    def updateTree(self, l, r, i, val, node):
        if l == r == i:
            node.val = val
            return
        m = (l + r) // 2
        if i <= m:
            self.updateTree(l, m, i, val, node.left)
        else:
            self.updateTree(m + 1, r, i, val, node.right)
        node.val = node.left.val + node.right.val

    def query(self, l, r, L, R, node):
        if l > R or r < L:
            return 0
        if l >= L and r <= R:
            return node.val
        m = (l + r) // 2
        a = self.query(l, m, L, R, node.left)
        b = self.query(m + 1, r, L, R, node.right)
        return a + b

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)