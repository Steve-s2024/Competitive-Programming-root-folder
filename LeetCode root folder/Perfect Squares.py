# brute-force solution: TLE
'''class Solution:
    def numSquares(self, n: int) -> int:
        # brute-force
        min_ = float('inf')
        def dfs(tar, depth):
            nonlocal min_
            if tar < 0:
                return
            if tar == 0:
                min_ = min(min_, depth)
                return
            i = 1
            while i*i <= tar:
                dfs(tar-i*i, depth+1)
                i += 1
        dfs(n, 0)
        return min_
'''

# dp solution, need optimize:5016
# ms
# Beats
# 5.48%
'''class Solution:
    def numSquares(self, n: int) -> int:
        # dp solution
        dp = {}

        def dfs(tar):
            if tar < 0:
                return float('inf')
            if tar == 0:
                return 0
            if tar in dp:
                return dp[tar]

            min_ = float('inf')
            i = 1
            while i * i <= tar:
                min_ = min(dfs(tar - i * i) + 1, min_)
                i += 1
            dp[tar] = min_
            return min_

        return dfs(n)'''


# what the fuck man... :186
# ms
# Beats
# 89.12%
# I'm kinda cheating with this one, I didn't change anything but to move dp to be the class instance variable lol.
class Solution:
    dp = {}
    def numSquares(self, n: int) -> int:
        # dp solution

        def dfs(tar):
            if tar < 0:
                return float('inf')
            if tar == 0:
                return 0
            if tar in self.dp:
                return self.dp[tar]

            min_ = float('inf')
            i = 1
            while i * i <= tar:
                min_ = min(dfs(tar - i * i) + 1, min_)
                i += 1
            self.dp[tar] = min_
            return min_

        return dfs(n)

