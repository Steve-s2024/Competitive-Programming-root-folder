# optimized solution with preprocess: 26%
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def cntCost(s, l, r):
            cost = 0
            while l < r:
                if s[l] != s[r]:
                    cost += 1
                l += 1
                r -= 1
            return cost

        n = len(s)
        records = {}
        for i in range(n):
            for j in range(i, n):
                records[(i, j)] = cntCost(s, i, j)
        dp = {}
        def recursive(i, remain):
            if (i, remain) in dp:
                return dp[(i, remain)]
            if i >= n:
                if remain == 0:
                    return 0
                return float('inf')

            minCost = float('inf')
            for j in range(i, n):
                tmp = recursive(j + 1, remain - 1) + records[(i, j)]
                minCost = min(minCost, tmp)
            dp[(i, remain)] = minCost
            return minCost

        return recursive(0, k)


# probably the least time spent on hard problem (less then 10 min): 5%
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def cntCost(s, l, r):
            cost = 0
            while l < r:
                if s[l] != s[r]:
                    cost += 1
                l += 1
                r -= 1
            return cost

        n = len(s)
        dp = {}

        def recursive(i, remain):
            if (i, remain) in dp:
                return dp[(i, remain)]
            if i >= n:
                if remain == 0:
                    return 0
                return float('inf')

            minCost = float('inf')
            for j in range(i, n):
                tmp = recursive(j + 1, remain - 1) + cntCost(s, i, j)
                minCost = min(minCost, tmp)
            dp[(i, remain)] = minCost
            return minCost

        return recursive(0, k)