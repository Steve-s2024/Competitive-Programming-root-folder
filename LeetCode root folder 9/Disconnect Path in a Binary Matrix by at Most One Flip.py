# a failed attempt using tarjan, though it is not about bridge checking instead of critical node checking
def tarjan(n, edges):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    vis = [0] * n
    arr = [0] * n
    low = [0] * n
    cnt = 0

    def dfs(u, p):
        nonlocal cnt
        vis[u] = 1
        arr[u] = cnt
        low[u] = arr[u]
        cnt += 1
        for v in g[u]:
            if v == p: continue
            if vis[v]:
                low[u] = min(low[u], arr[v])
                continue

            a = dfs(v, u)
            low[u] = min(low[u], a)
        return low[u]

    dfs(0, -1)

    ans = []
    for u, v in edges:
        if low[u] > arr[v] or low[v] > arr[u]: ans.append((u, v))
    return ans  # all the bridge connections will be returned


class Solution:
    def isPossibleToCutPath(self, mat: List[List[int]]) -> bool:
        for r in mat: print(r)
        n, m = len(mat), len(mat[0])
        g = [[] for _ in range(n * m)]
        edges = []
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0: continue
                for r, c in ((i + 1, j), (i, j + 1)):
                    if r in range(n) and c in range(m) and mat[r][c]:
                        u, v = i * m + j, r * m + c
                        # print(u, v, n, m)
                        g[u].append(v)
                        g[v].append(u)
                        edges.append((u, v))
        bridges = tarjan(n * m, edges)
        # print(g)
        # print(bridges)
        st = set(bridges)
        for u, v in bridges:
            if u in [0, n * m - 1] or v in [0, n * m - 1]: st.remove((u, v))
        q = deque([0])
        vs = [0] * (n * m)
        vs[0] = 1
        while q:
            u = q.popleft()
            if u == n * m - 1: return False
            for v in g[u]:
                if vs[v] or (u, v) in st or (v, u) in st: continue
                vs[v] = 1
                q.append(v)

        return True

