# brute-force: time-limit exceeded
'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(target, idx):
            # print(target)
            if target == 0:
                return 1
            if idx >= len(coins):
                return 0

            count = 0
            total = 0
            while count * coins[idx] <= target:
                total += dfs(target - coins[idx] * count, idx + 1)
                count += 1
            return total

        return dfs(amount, 0)
'''

# dp solution no.1 / decision tree & memoization solution, need to be optimized:7350
# ms
# Beats
# 5.02%

'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(target, idx):
            if (target, idx) in dp:
                return dp[(target, idx)]
            # print(target)
            if target == 0:
                return 1
            if idx >= len(coins):
                return 0
            
            count = 0
            total = 0
            while count * coins[idx] <= target:
                total += dfs(target - coins[idx]*count, idx+1)
                count += 1
            dp[(target, idx)] = total
            return total
            
        return dfs(amount, 0)
'''

# the 2d table dp solution, the time and space complexity is the same as the above one but this is majestically much
# faster...
# 603
# ms
# Beats
# 24.98%
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dp = [[0]*len(coins) for i in range(amount)]
        for r in range(len(dp)-1, -1, -1):
            for c in range(len(dp[0])-1, -1, -1):
                if coins[c] + r == amount:
                    a = 1
                elif coins[c] + r > amount:
                    a = 0
                else:
                    a = dp[coins[c]+r][c]

                if c >= len(coins)-1:
                    b = 0
                else:
                    b = dp[r][c+1]

                dp[r][c] = a + b
        return dp[0][0]