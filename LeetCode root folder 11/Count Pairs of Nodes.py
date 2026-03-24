# aced it! woooo~, why is it so easy???

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        mp = defaultdict(int)
        for u, v in edges:
            u, v = u - 1, v - 1
            mp[(u, v)] = mp[(v, u)] = mp[(u, v)] + 1
            g[u].append(v)
            g[v].append(u)

        ans = []
        ar = sorted([len(e) for e in g])
        for k in queries:
            res = 0
            for u in range(n):
                x = len(g[u])
                st = set()
                for v in g[u]:
                    if v in st: continue
                    st.add(v)
                    t = x + len(g[v]) - mp[(u, v)]
                    if t > k: res += 1
                    if len(g[v]) > k - x: res -= 1
                    # print(u, v)
                    # print(x, t)
                res += n - bisect_right(ar, k - x)
                if 2 * x > k: res -= 1
                # print(u, res, n - bisect_right(ar, k - x))
            # print('res', res)
            ans.append(res // 2)

        return ans