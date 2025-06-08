# brute-force

'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # brute-force
        def backtrack(i1, i2):
            if i1 >= len(s) and i2 < len(t):
                return 0
            if i2 >= len(t):
                return 1

            if s[i1] == t[i2]:
                sum_ = (
                    backtrack(i1+1, i2) +
                    backtrack(i1+1, i2+1)
                )
            else:
                sum_ = backtrack(i1+1, i2)

            return sum_
        return backtrack(0, 0)
'''


# dp solution:950
# ms
# Beats
# 18.95%
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp solution
        dp = {}

        def backtrack(i1, i2):
            if i1 >= len(s) and i2 < len(t):
                return 0
            if i2 >= len(t):
                return 1
            if (i1, i2) in dp:
                return dp[(i1, i2)]

            if s[i1] == t[i2]:
                sum_ = (
                        backtrack(i1 + 1, i2) +
                        backtrack(i1 + 1, i2 + 1)
                )
            else:
                sum_ = backtrack(i1 + 1, i2)
            dp[(i1, i2)] = sum_
            return sum_

        return backtrack(0, 0)
