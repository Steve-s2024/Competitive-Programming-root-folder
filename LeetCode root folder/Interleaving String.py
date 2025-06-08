# brute-force O((n+m)^2) where n, m is the length of s1, s2: time-limit exceeded
'''class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(s1, s2, s3):
            if len(s1) == 0 and len(s2) == 0:
                return True
            res = False
            if len(s1) and s1[0] == s3[0]:
                res = res or dfs(s1[1:], s2, s3[1:])
            if len(s2) and s2[0] == s3[0]:
                res = res or dfs(s1, s2[1:], s3[1:])
            return res
        return dfs(s1, s2, s3)'''


# dp solution O(m*n):47
# ms
# Beats
# 43.69%
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = set()
        def dfs(s1, s2, s3):
            if (len(s1), len(s2)) in dp:
                return False
            if len(s1) == 0 and len(s2) == 0:
                return True
            res = False
            if len(s1) and s1[0] == s3[0]:
                res = res or dfs(s1[1:], s2, s3[1:])
            if len(s2) and s2[0] == s3[0]:
                res = res or dfs(s1, s2[1:], s3[1:])
            dp.add((len(s1), len(s2)))
            return res
        return dfs(s1, s2, s3)

# interesting how I don't remember that I had solved it only after a week...
# so that I solved it again: brute-force
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        # brute-force
        def dfs(i1, i2, i3):
            if i3 >= len(s3):
                return True
            res = False
            if i1 < len(s1) and s3[i3] == s1[i1]:
                res = res or dfs(i1+1, i2, i3+1)
            if i2 < len(s2) and s3[i3] == s2[i2]:
                res = res or dfs(i1, i2+1, i3+1)
            return res
        return dfs(0, 0, 0)
'''
