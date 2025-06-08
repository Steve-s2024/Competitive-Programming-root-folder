# don't know how so many people speed run this question, it took me a while...
class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        def checkPalin(string, i):
            l, r = i, len(string) - 1
            while l <= r:
                n1, n2 = l, r
                while n1 < len(string) and n2 >= 0 and string[n1] == string[n2]:
                    n1 += 1
                    n2 -= 1
                if n1 >= n2:
                    return r - l + 1
                else:
                    r -= 1
            return 0

        def getLen(i, j):
            a, b = i, j
            cnt = 0
            while i < len(s) and j >= 0:
                if s[i] == t[j]:
                    i += 1
                    j -= 1
                    cnt += 2
                else:
                    break
            return cnt + max(checkPalin(s, i), checkPalin(t[::-1], len(t) - j - 1))

        res = 0
        for i in range(len(s)):
            for j in range(len(t)):
                res = max(res, getLen(i, j))
        return res
