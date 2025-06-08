# dp solution:258
# ms
# Beats
# 17.80%
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        count = 0
        dp = []
        for c in s:
            if c == '1':
                count += 1
            dp.append(count)

        def recursive(i):
            if i < 0:
                return 0
            if s[i] == '0':
                min_ = min(dp[i], recursive(i-1)+1)
            elif s[i] == '1':
                min_ = min(dp[i], recursive(i-1))
            return min_
        return recursive(len(s)-1)