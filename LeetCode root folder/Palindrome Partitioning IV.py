# predefine palindrome checking, still TLE
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def validPalin(i, j, s):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        n = len(s)
        ref = [[False]*n for i in range(n)]
        for i in range(n):
            for j in range(i, n):
                ref[i][j] = validPalin(i, j, s)

        for i in range(1, n-1):
            for j in range(i, n-1):
                if ref[0][i-1] and ref[i][j] and ref[j+1][n-1]:
                    return True
        return False

# dp solution, need a better way to check palindrome: TLE
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def validPalin(i, j, s):
            while i < j:
                if s[i] != s[j]:
                    return False
                i+=1
                j-=1
            return True
        dp = set()
        n = len(s)
        def recursive(i, remain):
            nonlocal n
            if remain == 0 and i == n:
                return True
            if remain == 0 or i >= n:
                return False
            if (i, remain) in dp:
                return False
            dp.add((i, remain))
            
            for j in range(i, n):
                if validPalin(i, j, s):
                    if recursive(j+1, remain-1):
                        return True
            return False
        return recursive(0, 3)
    

