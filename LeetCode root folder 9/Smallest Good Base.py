# so far the one problem with the most mathematics involvement (solved by help of hint)
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        ans = n-1
        for m in range(1, 60):
            l, r = 2, n-1
            res = -1
            while l <= r:
                k = (l+r)//2
                nu = k**m - 1
                de = k - 1
                if nu > n*de: r = k-1
                elif nu < n*de: l = k+1
                else:
                    res = k
                    break
            # print(res)
            if res != -1: ans = min(ans, res)
        return str(ans)