# dp solution: 55%
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        def recursive(length):
            if length in dp:
                return dp[length]
            if length > high:
                return 0
            if length >= low:
                res = 1
            else:
                res = 0
            res += recursive(length+zero)
            res += recursive(length+one)
            res %= 1000000007
            dp[length] = res 
            return res
        return recursive(0) 
