# dp solution: TLE
'''class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = {}
        def recursive(i, count):
            if (i, count) in dp:
                return dp[(i, count)]
            if count == 3:
                return 1
            if i >= len(s):
                return 0
            total = 0
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    total += recursive(j, count+1)
            dp[(i, count)] = total
            return total
        res = 0
        for i in range(len(s)):
            res += recursive(i, 1)
        return res'''

# greedy (or it can be considered as dp):266
# ms
# Beats
# 66.60%
class Solution:
    def numberOfWays(self, s: str) -> int:
        zero, one = 0, 0
        n1, n2 = 0, 0
        # n1 --> the number of different pairs start with 0
        # n2 --> the number of different pairs start with 1
        m1, m2 = 0, 0
        # m1 --> the number of different triplets start with 0
        # m2 --> the number of different triplets start with 1

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                zero += 1
                n1 += one
                m1 += n2
            else:
                one += 1
                n2 += zero
                m2 += n1
        return m1 + m2

