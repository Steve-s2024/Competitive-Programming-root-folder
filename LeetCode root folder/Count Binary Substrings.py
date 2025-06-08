class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        dp = [0] * len(s)
        cur = 1
        for i in range(len(s)-1, -1, -1):
            if i < len(s)-1 and s[i] == s[i+1]:
                cur += 1
            else:
                cur = 1
            dp[i] = cur
        # print(dp)
        res = 0
        for i in range(len(s)):
            prev = s[i]
            for j in range(i+dp[i], len(s), dp[i]):
                if s[j] == prev:
                    break
                elif dp[j] < dp[i]:
                    break
                elif dp[j] > dp[i]:
                    res += 1
                    break
                else:
                    res += 1
        return res
