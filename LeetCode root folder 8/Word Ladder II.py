# MLE, man this is hard!
class Solution:
    def findLadders(self, b: str, e: str, w: List[str]) -> List[List[str]]:
        g = defaultdict(list)
        if b not in w:
            for v in w:
                x = 0
                for i in range(len(b)):
                    if b[i] != v[i]: x += 1
                if x == 1: g[b].append(v)
        for v1 in w:
            for v2 in w:
                x = 0
                for i in range(len(v1)):
                    if v1[i] != v2[i]: x += 1
                if x == 1: g[v1].append(v2)

        # print(g)
        vis = {}
        vis[b] = 0
        q = deque([(0, b, [b, None])])
        lim = inf
        ans = []
        while q:
            # print(q)
            ct, u, li = q.popleft()
            # print(u)
            if ct > lim: break
            if u == e:
                ans.append(li)
                lim = ct
            # print(u)

            for v in g[u]:
                # print(v, vis)
                if v in vis and vis[v] < ct + 1: continue
                vis[v] = ct + 1
                q.append((ct + 1, v, [v, li]))

        # print(ans)
        res = []
        for v in ans:
            cur = v
            tmp = []
            while cur:
                tmp.append(cur[0])
                cur = cur[1]
            res.append(tmp[::-1])
        return res



