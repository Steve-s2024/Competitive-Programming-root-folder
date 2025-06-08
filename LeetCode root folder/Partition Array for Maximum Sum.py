# turns out using segment tree is completely unnecessary... : 38%

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = {}
        dp[n] = 0
        def recursive(i):
            nonlocal n
            if i in dp:
                return dp[i]
            
            res = 0
            max_ = 0
            for j in range(i, min(i+k, n)):
                max_ = max(max_, arr[j])
                res = max(res, recursive(j+1) + (j-i+1)*max_)
            dp[i] = res
            return res
        return recursive(0)
    
    

# segTree solution with maximum segTree & dp, how can this not be the optimal man...: 5%
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaxTree:
    def build(self, l, r, arr):
        if l == r:
            return Node(arr[l])
        if l > r:
            return None
        m = (l + r) // 2
        left = self.build(l, m, arr)
        right = self.build(m+1, r, arr)
        return Node(
            max(left.val, right.val),
            left, 
            right
        )

    def query(self, l, r, L, R, node):
        if l >= L and r <= R:
            return node.val
        if l > R or r < L:
            return 0

        m = (l+r) // 2
        return max(
            self.query(l, m, L, R, node.left),
            self.query(m+1, r, L, R, node.right)
        )


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        maxTree = MaxTree()
        tree = maxTree.build(0, n-1, arr)

        dp = {}
        dp[n] = 0
        def recursive(i):
            if i in dp:
                return dp[i]
            
            res = 0
            for j in range(i, min(i+k, n)):
                max_ = maxTree.query(0, n-1, i, j, tree)
                res = max(res, recursive(j+1) + (j-i+1)*max_)
            dp[i] = res
            return res

        res = 0
        for i in range(k):
            max_ = maxTree.query(0, n-1, 0, i, tree)
            res = max(res, recursive(i+1) + (i+1)*max_)
        return res
