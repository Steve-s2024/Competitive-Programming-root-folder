# LCA, force me to write a new version of it
# with leetgoat's trick to finish it up
class LCA:
    def __init__(self, g):
        n = len(g)
        self.up = self.build(g)
        dep = [0] * n

        def fn(u, p, d):
            dep[u] = d
            for v in g[u]:
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
            for v in g[u]:
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


class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append(v)
            g[v].append(u)
        lca = LCA(g)

        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append([v, w])
            g[v].append([u, w])

        pre = [0] * n

        def dfs(u, p, sm):
            pre[u] = sm
            for v, w in g[u]:
                if v == p: continue
                dfs(v, u, sm + w)

        dfs(0, -1, 0)

        ans = []
        for u, v, w in queries:
            x = 0
            for a, b in ((u ,w), (v, w), (u, v)):
                c = lca.search(a, b)
                x += pre[a]-pre[c] + pre[b]-pre[c]
            ans.append(x//2)
        return ans