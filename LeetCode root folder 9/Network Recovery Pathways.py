# with a bit modification it is working properly with score = "min edges-cost"
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        if not edges: return -1
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            if online[u] and online[v]: g[u].append((v, w))
        ans = -1
        vs = [e[2] for e in edges]
        l, r = min(vs), max(vs)
        while l <= r:
            m = (l + r) // 2
            hp = [(0, 0)]
            vs = [0] * n
            res = inf
            while hp:
                sc, u = heappop(hp)
                if u == n - 1:
                    res = sc
                    break
                if vs[u]: continue
                vs[u] = 1
                for v, w in g[u]:
                    if w < m: continue
                    heappush(hp, (sc + w, v))

            if res <= k:
                ans = m
                l = m+1
            else: r = m-1

        return ans



# holy this is hard as shit. complete solution, just not for the problem (yeah I misread the definition of score as "max edges-cost" instead of "min")
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            if online[u] and online[v]: g[u].append((v, w))

        ans = -1
        vs = [e[2] for e in edges]
        l, r = min(vs), max(vs)
        while l <= r:
            m = (l + r) // 2
            hp = [(0, 0)]
            vs = [0] * n
            res = inf
            while hp:
                sc, u = heappop(hp)
                if u == n - 1:
                    res = sc
                    break
                vs[u] = 1
                for v, w in g[u]:
                    if vs[v] or w > m: continue
                    heappush(hp, (sc + w, v))

            if res <= k:
                ans = m
                r = m-1
            else:
                l = m+1

        return ans