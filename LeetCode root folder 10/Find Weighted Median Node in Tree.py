# absolutely necessary practice to improve and build a strong implementation skill.
# it is the type that you really need to force a super-clean though process. a tiny redundant thought can overcomplicate
# the thing a lot. I am forced to rethink again and gain and taking on different angles viewing the same issue. each one
# is an upgrade of the previous one with reduced redundancy.

# LCA & using binary lifting to binary search on tree solution.
class LCA:
    def __init__(self, g):
        n = len(g)
        self.up = self.build(g)
        dep = [0] * n

        def fn(u, p, d):
            dep[u] = d
            for v, _ in g[u]:
                if v == p: continue
                fn(v, u, d + 1)

        fn(0, -1, 0)
        self.dep = dep

    def build(self, g):
        n = len(g)
        lim = n.bit_length()
        up = [[-1] * lim for _ in range(n)]
        stk = []

        def dfs(u, p):
            i = 0
            while 1 << i <= len(stk): up[u][i], i = stk[-(1 << i)], i + 1
            for v, _ in g[u]:
                if v == p: continue
                stk.append(u)
                dfs(v, u)
                stk.pop()

        dfs(0, -1)
        return up

    def search(self, u, v):
        dep = self.dep
        up = self.up
        if dep[u] > dep[v]: u, v = v, u

        dif = dep[v] - dep[u]
        i = 0
        while dif:
            if dif & 1: v = up[v][i]
            dif >>= 1
            i += 1

        if u == v: return v
        i = len(up[0]) - 1
        while i >= 0:
            if up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
            i -= 1
        return up[u][0]

    def solveDown(self, sm, t, p, u, pre):
        x = (sm+1)//2-t
        dep, up = self.dep, self.up
        res, i = u, 0
        j = 0
        # print(sm, t, p, u)
        while 1:
            # print(u, i, res)
            v = up[u][i]
            if v != -1 and pre[v] - pre[p] >= x: res, i = v, i+1
            else:
                if u == res: break
                u, i = res, 0
        return u

    def solveUp(self, sm, t, u, pre):
        U = u
        x = (sm+1)//2
        dep, up = self.dep, self.up
        res, i = u, 0
        j = 0
        while 1:
            # print(u, i, res)
            v = up[u][i]
            if v != -1 and pre[U] - pre[v] < x: res, i = v, i+1
            else:
                if res == u: break
                u, i = res, 0
        return up[u][0]



class Solution:
    def findMedian(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        pre = [0] * n

        def dfs(u, p, W):
            pre[u] = W
            for v, w in g[u]:
                if v != p: dfs(v, u, W + w)

        dfs(0, -1, 0)
        ans = []
        lca = LCA(g)
        for u, v in queries:
            if u == v:
                ans.append(u)
                continue
            x = lca.search(u, v)
            # u->x, then x->v
            a, b = pre[u] - pre[x], pre[v] - pre[x]
            if a < b: res = lca.solveDown(a + b, a, x, v, pre)
            else: res = lca.solveUp(a + b, 0, u, pre)
            ans.append(res)

        return ans


