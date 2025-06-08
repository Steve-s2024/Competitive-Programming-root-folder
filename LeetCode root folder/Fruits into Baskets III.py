# brute force: tle

'''class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        hashSet = set()
        res = 0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if j not in hashSet and fruits[i] <= baskets[j]:
                    hashSet.add(j)
                    break
            else:
                res += 1
        return res'''


# segment tree solution no.2, the correct solution with n*log(n):2223
# ms
# Beats
# -%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxTree:
    @staticmethod
    def build(arr, l, r):
        if l >= r:
            return TreeNode(arr[l])
        m = (l + r) // 2
        a = MaxTree.build(arr, l, m)
        b = MaxTree.build(arr, m + 1, r)
        return TreeNode(
            max(a.val, b.val),
            a,
            b
        )


class Solution:
    def numOfUnplacedFruits(self, fruits, baskets):
        ans = len(fruits)
        def searchTree(node, val):
            nonlocal ans
            if node is None:
                return
            if node.left is None:
                if node.val >= val:
                    node.val = -float('inf')
                    ans -= 1
                return node.val
            if node.left.val >= val:
                searchTree(node.left, val)
            else:
                searchTree(node.right, val)
            node.val = max(node.left.val, node.right.val)


        maxTree = MaxTree.build(baskets, 0, len(baskets) - 1)
        for fruit in fruits:
            searchTree(maxTree, fruit)
        return ans



# segment tree solution no.1, n*log(n)^2: tle
# however, this is indeed faster than the mere brute force. one testcase 733, this spent 1800ms while the above
# brute force get a tle.
'''class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaxTree:
    @staticmethod
    def build(arr, l, r):
        if l >= r:
            return TreeNode(arr[l])
        m = (l + r) // 2
        a = MaxTree.build(arr, l, m)
        b = MaxTree.build(arr, m + 1, r)
        return TreeNode(
            max(a.val, b.val),
            a,
            b
        )
    @staticmethod
    def query(node, L, R, l, r):
        if r < L or l > R:
            return -float('inf')
        if l >= L and r <= R:
            return node.val
        m = (l + r) // 2
        return max(
            MaxTree.query(node.left, L, R, l, m),
            MaxTree.query(node.right, L, R, m + 1, r)
        )
    @staticmethod
    def update(i, val, node, l, r):
        if l == r == i:
            node.val = val
            return node.val
        m = (l + r) // 2
        if i in range(l, m + 1):
            MaxTree.update(i, val, node.left, l, m)
        else:
            MaxTree.update(i, val, node.right, m + 1, r)
        node.val = max(node.left.val, node.right.val)
        return node.val


class Solution:
    def findPlace(self, num, arr):

        def binarySearch(l, r):
            nonlocal num
            if l >= r:
                tar = MaxTree.query(self.maxTree, l, l, 0, len(arr)-1)
                if tar >= num:
                    # print(num, (l, r), MaxTree.query(self.maxTree, l, l, 0, len(arr)-1))
                    # the position found!
                    MaxTree.update(l, -float('inf'), self.maxTree, 0, len(arr)-1)
                    self.ans -= 1
                return
            m = (l + r) // 2
            max_ = MaxTree.query(self.maxTree, l, m, 0, len(arr) - 1)
            if max_ >= num:
                binarySearch(l, m)
            else:
                binarySearch(m + 1, r)
        binarySearch(0, len(arr)-1)

    def numOfUnplacedFruits(self, fruits, baskets):
        self.ans = len(fruits)
        self.maxTree = MaxTree.build(baskets, 0, len(baskets) - 1)
        for fruit in fruits:
            self.findPlace(fruit, baskets)
        return self.ans'''