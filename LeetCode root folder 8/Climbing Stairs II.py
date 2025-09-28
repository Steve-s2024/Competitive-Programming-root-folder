# nice, not Fibonacci this time, it's a normal 3 pick knap-sack (Q2 in the contest of 2025/09/27)
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @cache
        def recursive(i):
            if i >= n-1: return 0
            res = recursive(i+1) + costs[i+1]+1
            if i < n-2:
                a = recursive(i+2) + costs[i+2] + 4
                res = min(a, res)
            if i < n-3:
                a = recursive(i+3) + costs[i+3] +  9
                res = min(a, res)
            return res
        return recursive(-1)
