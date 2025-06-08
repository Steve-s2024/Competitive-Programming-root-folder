# brute-force: tle
'''class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # brute-force
        sums = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                sums.append(sum(arr[i:j+1]))
        res = 0
        for sum_ in sums:
            res += sum_ % 2
        return res'''

# dp solution:314
# ms
# Beats
# 5.03%

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        dp = [None] * len(arr)
        dp.append([0, 0])
        total = 0
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] % 2 == 1:
                dp[i] = [1 + dp[i + 1][1], dp[i + 1][0]]
            else:
                dp[i] = [dp[i + 1][0], 1 + dp[i + 1][1]]
            total += dp[i][0]
            total %= (pow(10, 9) + 7)
        return total
