# a new way of approach, the recursive function return the length, not the actual string, but the DP can use this
# length information to construct a path which builds the actual sequence/string: 34%
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[0]*m for _ in range(n)]
        @cache
        def recursive(i, j):
            nonlocal n, m
            if i >= n and j >= m: return 0
            if i >= n: return m-j
            if j >= m: return n-i
            if str1[i] == str2[j]:
                dp[i][j] = 2
                res = recursive(i+1, j+1)
            else:
                a, b = recursive(i+1, j), recursive(i, j+1)
                if a <= b:
                    dp[i][j] = 0
                    res = a
                else:
                    dp[i][j] = 1
                    res = b
            return res+1

        recursive(0, 0)

        strarr = []
        i, j = 0, 0
        while i < n and j < m:
            val = dp[i][j]
            if val == 0:
                strarr.append(str1[i])
                i += 1
            elif val == 1:
                strarr.append(str2[j])
                j += 1
            else:
                strarr.append(str1[i])
                i += 1
                j += 1
        strarr.extend(list(str1[i:]) + list(str2[j:]))
        return ''.join(strarr)



# trying the bottom up solution now, which is the intended solution
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[None]*m for _ in range(n)]
        dp[n-1][m-1] = []
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                a, b = dp[i+1][j] if i < n-1 else 0, dp[i][j+1] if j < m-1 else 0
                return dp[i]


# the technique which I used to allow returning reference value while caching it and modifying based on it later all
# at the same time in a recursive dp call is something I invented, by the virtue of python's typeless list, in the
# atCoder contest Q4. it only works in python though and is not very efficient: 5%
# it's basically a nested list performing as if like linked list.
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        @cache
        def recursive(i, j):
            nonlocal n, m
            if i >= n and j >= m: return [0]
            if i < n and j < m:
                a = recursive(i+1, j+1)
                if str1[i] == str2[j]: res = [a[0]+1, a, str1[i]]
                else:
                    a = recursive(i+1, j)
                    b = recursive(i, j+1)
                    if a[0] <= b[0]: res = [a[0]+1, a, str1[i]]
                    else: res = [b[0]+1, b, str2[j]]

            elif i < n:
                a = recursive(i+1, j)
                res = [a[0]+1, a, str1[i]]
            elif j < m:
                a = recursive(i, j+1)
                res = [a[0]+1, a, str2[j]]
            return res
        res = recursive(0, 0)
        # print(res)
        strarr = []
        cur = res
        while len(cur) > 1:
            strarr.append(cur[2])
            cur = cur[1]
        return ''.join(strarr)


# got the wrong thing, it returns the length not the actual supersequence
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        def recursive(i, j):
            nonlocal n, m
            if i >= n and j >= m: return 0
            if i < n and j < m:
                if str1[i] == str2[j]: res = recursive(i+1, j+1)
                else: res = min(recursive(i+1, j), recursive(i, j+1))
            elif i < n: res = recursive(i+1, j)
            elif j < m: res = recursive(i, j+1)
            return res+1
        return recursive(0, 0)