# KMP searching string on the reverse of itself solution, pretty hard to observe.

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == '': return ''
        s1, s2 = s[::-1], s
        n, m = len(s1), len(s2)
        lps = [0] * m
        l = 0
        for i in range(1, m):
            while s2[i] != s2[l] and l: l = lps[l - 1]
            if s2[i] == s2[l]:
                l += 1
                lps[i] = l
        l = 0
        for i in range(n):
            while s1[i] != s2[l] and l: l = lps[l - 1]
            if s1[i] == s2[l]:
                l += 1
                if i == n - 1:
                    idx = i - l + 1
                    mid = s1[idx:][::-1]
                    sde = s1[:idx][::-1]
                    return sde[::-1] + mid + sde
                if l == m: l = lps[l - 1]
