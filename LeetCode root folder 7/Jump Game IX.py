# why did it TLE? the time complexity is solid good
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. build
def build(arr, l, r):
    if l >= r:
        return TreeNode(arr[l])
    m = (l + r) // 2
    a = build(arr, l, m)
    b = build(arr, m + 1, r)
    return TreeNode(
        max(a.val, b.val),
        a,
        b
    )


# 2. update
def update(node, i, val, l, r):
    if l == r == i:
        node.val = val
        return val
    m = (l + r) // 2
    if i in range(l, m + 1):
        res = update(node.left, i, val, l, m)
    else:
        res = update(node.right, i, val, m + 1, r)
    node.val = max(node.val, res)
    return node.val


# 3. query
def query(node, L, R, l, r):
    if r < L or l > R:
        return -float('inf')
    if l >= L and r <= R:
        return node.val

    m = (l + r) // 2
    return max(
        query(node.left, L, R, l, m),
        query(node.right, L, R, m + 1, r),
    )


def queryForMiIndex(node, tar, L, l, r):
    if L > r: return -1
    if l == r: return l
    m = (l + r) // 2
    res = -1
    if node.right and node.right.val > tar:
        a = queryForMiIndex(node.right, tar, L, m + 1, r)
        res = max(res, a)
    elif node.left and node.left.val > tar:
        a = queryForMiIndex(node.left, tar, L, l, m)
        res = max(res, a)
    return res


class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        mx = nums[0]
        for i in range(n):
            mx = max(nums[i], mx)
            pre[i] = mx

        mitree = build([-e for e in nums], 0, n - 1)
        suf = [0] * n
        for i in range(n):
            suf[i] = queryForMiIndex(mitree, -pre[i], i, 0, n - 1)
        dp = nums[:]
        mxtree = build(dp, 0, n - 1)
        for i in range(n - 1, -1, -1):
            dp[i] = max(pre[i], query(mxtree, i, suf[i], 0, n - 1))
            update(mxtree, i, dp[i], 0, n - 1)
        return dp

