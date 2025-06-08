# elligent recursive solution: 32%
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        n = len(cost)
        for i in range(n, 0, -1):
            l, r = i*2, i*2+1

            a, b = 0, 0
            if l-1 < n:
                a = cost[l-1]
            if r-1 < n:
                b = cost[r-1]   
            res += abs(a-b)
            cost[i-1] += max(a, b)
        return res


# correct approach, just that I don't feel like 
# constructing a binary tree.
'''class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            a = dfs(node.left)
            b = dfs(node.right)
            diff = abs(a - b)
            res += diff
            return max(a, b) + cost(node.val)
        dfs(tree)
        return res'''