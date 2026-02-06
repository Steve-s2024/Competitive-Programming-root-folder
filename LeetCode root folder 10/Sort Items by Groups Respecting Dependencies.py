# intensive topo sort problem

class Solution:
    def sortItems(self, n: int, m: int, g: List[int], bi: List[List[int]]) -> List[int]:
        st = set()
        for i in range(n): st.add(g[i])
        x = 0
        for i in range(n):
            if g[i] == -1:
                while x in st: x += 1
                g[i] = x
                st.add(x)

        vermp = defaultdict(set)
        for u in range(n): vermp[g[u]].add(u)
        ver = set(g)
        mp = {gid: defaultdict(list) for gid in ver}
        G = defaultdict(list)
        for u in range(n):
            for v in bi[u]:
                g1, g2 = g[u], g[v]
                if g1 == g2:
                    mp[g1][v].append(u)
                else:
                    G[g2].append(g1)

        def topo(g, ver):
            d = defaultdict(int)
            for u in ver:
                if u not in d: d[u] = 0
                for v in g[u]: d[v] += 1

            q = deque()
            for u, frq in d.items():
                if frq == 0: q.append(u)

            res = []
            vs = set()
            while q:
                u = q.popleft()
                if u in vs: continue
                vs.add(u)
                res.append(u)
                for v in g[u]:
                    d[v] -= 1
                    if d[v] == 0: q.append(v)
            return res

        res = topo(G, ver)
        if len(res) != len(ver): return []
        ans = []
        for gid in res:
            ar = topo(mp[gid], vermp[gid])
            if len(ar) != len(vermp[gid]): return []
            for v in ar: ans.append(v)
        # print(G, ver)
        # print(res)
        # print(vermp)
        # print(mp)
        return ans