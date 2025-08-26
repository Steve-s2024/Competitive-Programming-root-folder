# one line optimization speed the backtracking solution up like crazy, wtf???
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        arr = [0]*k
        res = inf
        def recursive(i):
            nonlocal res
            if i >= n:
                res = min(res, max(arr))
                return
            for j in range(k):
                if arr[j] + cookies[i] >= res: continue
                arr[j] += cookies[i]
                recursive(i+1)
                arr[j] -= cookies[i]
        recursive(0)
        return res


# DP solution tle
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        dp = {}
        def recursive(i, arr):
            nonlocal n, k
            state = tuple([i]+arr)
            if state in dp: return dp[state]
            if i >= n: return max(arr)
            res = inf
            for j in range(k):
                arr[j] += cookies[i]
                res = min(res, recursive(i+1, arr))
                arr[j] -= cookies[i]
            dp[state] = res
            return res
        return recursive(0, [0]*k)
