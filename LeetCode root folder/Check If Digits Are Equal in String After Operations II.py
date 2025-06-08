# brute-force: tle
'''
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) == 2:
            return s[0] == s[1]
        res = ''
        for i in range(len(s)-1):
            sum_ = int(s[i]) + int(s[i+1])
            sum_ %= 10
            res += str(sum_)
        return self.hasSameDigits(res)
'''



# pascal triangle solution, man i am only clever enough to get to this solution: mle
class Solution:
    dp = [[1, 1]]

    def constructDp(self, n):
        dp = self.dp
        l = len(dp)
        for i in range(l, n):
            dp.append([1])
            for j in range(len(dp[-2]) - 1):
                dp[i].append(dp[-2][j] + dp[-2][j + 1])
            dp[-1].append(1)

    def hasSameDigits(self, s: str) -> bool:
        layer = len(s) - 2
        dp = self.dp
        if len(dp) < len(s) - 1:
            self.constructDp(len(s) - 1)
            # print(dp)
        total = 0
        l, r = 0, 0
        for i, c in enumerate(s):
            if i < len(s) - 1:
                l += dp[layer - 1][i] * int(c)
            if i > 0:
                r += dp[layer - 1][i - 1] * int(c)

        # print(l, r)
        return l % 10 == r % 10

# combination formula solution: no idea why it doesn't work sometime
# it should work and run with optimal time-complexity
'''
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        l, r = 0, 0
        n1, n2 = 1, 1
        n = len(s)-2
        for i in range(1, len(s)):
            l += (n1/n2) * int(s[i-1])
            r += (n1/n2) * int(s[i])
            l %= 10
            r %= 10
            # print(n1/n2)
            n1 *= (n)
            n2 *= (i)
            n -= 1
        # print(l, r)
        return l % 10 == r % 10
'''