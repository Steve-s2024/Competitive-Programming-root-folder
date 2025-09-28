# binary search and greedy solution: 20%

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        size = len(batteries)
        res = -1
        l, r = 1, sum(batteries) // n
        while l <= r:
            m = (l + r) // 2
            sm = 0
            for i in range(size):
                inc = min(batteries[i], m)
                sm += inc
            if sm // m >= n:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res



