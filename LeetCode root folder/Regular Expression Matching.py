# the solution for linux global matching, not for regular expression...
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # brute force
        def recursive(i1, i2):
            if i1 >= len(s) and i2 >= len(p):
                return True
            elif i1 >= len(s) or i2 >= len(p):
                return False


            if p[i2] == '.':
                return recursive(i1+1, i2+1)
            elif p[i2] == '*':
                for i in range(i1, len(s)+1):
                    if recursive(i, i2+1):
                        return True
                return False
            elif p[i2] == s[i1]:
                return recursive(i1+1, i2+1)
            else:
                return False
        return recursive(0, 0)
'''


# brute force. Handling the edge cases are driving me mad. My bad for not being smart enough to come up with optimal solution...
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # brute force
        def recursive(i1, i2):
            if i1 >= len(s) and i2 >= len(p):
                return True
            elif i1 >= len(s):
                if (len(p)-i2) % 2 == 1:
                    return False
                for i in range(i2+1, len(p), 2):
                    if p[i] != '*':
                        return False
                return True 
            elif i2 >= len(p):
                return False
            
            if i2 < len(p)-1 and p[i2+1] == '*':
                if p[i2] == '.':
                    for i in range(i1, len(s)+1):
                        if recursive(i, i2+2):
                            return True
                else:
                    for i in range(i1, len(s)+1):
                        if recursive(i, i2+2):
                            return True
                        if i == len(s) or s[i] != p[i2]:
                            break
                return False
            elif p[i2] == '.':
                return recursive(i1+1, i2+1)
            elif s[i1] == p[i2]:
                return recursive(i1+1, i2+1)
            else:
                return False
        return recursive(0, 0)
'''


# dp solution:7
# ms
# Beats
# 69.50%

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp solution
        dp = {}

        def recursive(i1, i2):
            if (i1, i2) in dp:
                return dp[(i1, i2)]
            if i1 >= len(s) and i2 >= len(p):
                return True
            elif i1 >= len(s):
                if (len(p) - i2) % 2 == 1:
                    return False
                for i in range(i2 + 1, len(p), 2):
                    if p[i] != '*':
                        return False
                return True
            elif i2 >= len(p):
                return False

            res = False
            if i2 < len(p) - 1 and p[i2 + 1] == '*':
                if p[i2] == '.':
                    for i in range(i1, len(s) + 1):
                        if recursive(i, i2 + 2):
                            res = True
                            break
                else:
                    for i in range(i1, len(s) + 1):
                        if recursive(i, i2 + 2):
                            res = True
                            break
                        if i == len(s) or s[i] != p[i2]:
                            break
            elif p[i2] == '.':
                res = recursive(i1 + 1, i2 + 1)
            elif s[i1] == p[i2]:
                res = recursive(i1 + 1, i2 + 1)
            dp[(i1, i2)] = res
            return res

        return recursive(0, 0)

