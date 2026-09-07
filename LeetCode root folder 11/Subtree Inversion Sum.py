# okay... standard dp on tree variation


class Solution:
    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        dp = [[[-1]*k for _ in range(2)] for _ in range(n)]
        stk = [[0, -1, 0, 0]]
        while stk:
            u, p, f, x = stk[-1]

            if dp[u][f][x] == -1:
                dp[u][f][x] = 0

                for v in g[u]:
                    if v == p: continue
                    stk.append([v, u, f, max(x-1, 0)])
                    if x == 0: stk.append([v, u, f^1, k-1])
            else:

                res, a = 0, 0
                for v in g[u]:
                    if v == p: continue
                    res += dp[v][f][max(x-1, 0)]
                    if x == 0: a += dp[v][f^1][k-1]

                t = (-1 if f else 1) * nums[u]
                dp[u][f][x] = max(res + t, a - t) if x == 0 else (res + t)
                stk.pop()

        return dp[0][0][0]
