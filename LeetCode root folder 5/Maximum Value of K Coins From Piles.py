# array DP solution: 5%
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        arr = []
        mp = {}
        for p in piles:
            size = len(arr)
            for i, c in enumerate(p):
                mp[size + i] = size + len(p)
                arr.append(c)

        n = len(arr)
        dp = [[-1] * k for _ in range(n)]

        def recursive(i, k):
            nonlocal n
            if i >= n or k == 0: return 0
            if dp[i][k - 1] != -1: return dp[i][k - 1]
            a = recursive(i + 1, k - 1) + arr[i]
            b = recursive(mp[i], k)
            dp[i][k - 1] = max(a, b)
            return dp[i][k - 1]

        return recursive(0, k)



# MLE
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        arr = []
        mp = {}
        for p in piles:
            size = len(arr)
            for i, c in enumerate(p):
                mp[size + i] = size + len(p)
                arr.append(c)
        # print(mp)

        n = len(arr)

        @cache
        def recursive(i, k):
            nonlocal n
            if i >= n or k == 0: return 0
            a = recursive(i + 1, k - 1) + arr[i]
            b = recursive(mp[i], k)
            return max(a, b)

        return recursive(0, k)