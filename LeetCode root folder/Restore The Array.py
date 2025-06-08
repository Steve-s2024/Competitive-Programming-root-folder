# DP solution with array: MLE
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        def recursive(i):
            nonlocal s, k, n
            if dp[i] != 0:
                return dp[i]
            if s[i] == '0':
                return 0

            res = 0
            string = ''
            for nextI in range(i, n):
                string += s[nextI]
                if int(string) <= k:
                    res += recursive(nextI+1)
                else:
                    break
            dp[i] = res
            return res % 1000000007
        return recursive(0)

# DP solution: MLE
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = {}
        dp[n] = 1
        def recursive(i):
            nonlocal s, k, n
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0

            res = 0
            string = ''
            for nextI in range(i, n):
                string += s[nextI]
                if int(string) <= k:
                    res += recursive(nextI+1)
                else:
                    break
            dp[i] = res
            return res
        return recursive(0) % 1000000007