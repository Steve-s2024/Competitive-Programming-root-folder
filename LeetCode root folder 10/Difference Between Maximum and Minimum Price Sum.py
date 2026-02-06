# re-root dp, observe that to calculate the maximum path sum of an arbitrary root, given the maximum path sums of all its
# subtree max path sum, can be easy and the transition can be done in constant time operation. Though, we also need the max path sum
# of the parent node, and it must not be the subtree max path sum, it must be the parent node subtree max path sum excluding the current branch. (need a bit trick
# to handle this)

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        mp = {}

        def fn(u, p):
            mx = 0
            if len(g[u]) == 1 and g[u][0] == p: mx = 0
            for v in g[u]:
                if v == p: continue
                a = fn(v, u)
                mx = max(mx, a)
            mx += price[u]
            mp[u] = mx
            return mx

        fn(0, -1)

        # print(mp)

        res = 0

        def dfs(u, p, MX):
            nonlocal res
            mx = MX
            ar = []
            for v in g[u]:
                if v == p: continue
                mx = max(mx, mp[v])
                ar.append(mx)
            res = max(res, mx)
            # if u == 3: print(ar, MX)
            mx = MX
            j = len(ar)-1
            for i in range(len(g[u]) - 1, -1, -1):
                v = g[u][i]
                if v == p: continue
                dfs(v, u, max(mx, ar[j-1] if j else 0)+price[u])
                mx = max(mx, mp[v])
                j -= 1
        dfs(0, -1, 0)

        return res