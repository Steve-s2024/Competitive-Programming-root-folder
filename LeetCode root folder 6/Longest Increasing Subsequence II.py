# before this I didn't know segment tree can be used to find LIS, but this question is forcing the coder to use
# segment tree to find the longest increasing subsequence:5%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaxTree:
    def __init__(self, n):
        self.n = n
        self.root = self.build(0, self.n-1)

    def build(self, l, r):
        if l == r: return TreeNode()
        m = (l+r)//2
        return TreeNode(
            0,
            self.build(l, m),
            self.build(m+1, r)
        )

    def update(self, node, l, r, i, val):
        if l == r:
            node.val = val
            return val
        m = (l+r)//2
        if i in range(l, m+1):
            self.update(node.left, l, m, i, val)
        else:
            self.update(node.right, m+1, r, i, val)
        node.val = max(node.left.val, node.right.val)
        return node.val

    def query(self, node, l, r, L, R):
        if l >= L and r <= R: return node.val
        m = (l+r)//2
        res = -inf
        if m >= L: res = max(res, self.query(node.left, l, m, L, R))
        if m+1 <= R: res = max(res, self.query(node.right, m+1, r, L, R))
        return res


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        mt = MaxTree(mx)
        nums = [e-1 for e in nums]
        n = len(nums)
        res = 0
        # print(nums)
        for i in range(n):
            # node, l, r, L, R
            if nums[i] != 0:
                cur = mt.query(mt.root, 0, mt.n-1, max(nums[i]-k, 0), nums[i]-1)
            else: cur = 0
            # print(nums[i], cur)
            # node, l, r, i, val
            mt.update(mt.root, 0, mt.n-1, nums[i], cur+1)
            res = max(cur+1, res)
        return res