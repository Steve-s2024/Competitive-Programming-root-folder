# an algorithm for detecting the bridge in graph, connections that are critical for connecting the graph
# bridges are edges that, upon removal, the graph will be separate into two pieces.
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
    return ans # all the bridge connections will be returned


print(tarjan(4, [[0,1],[1,2],[2,0],[1,3]]))
print(tarjan(2, [[0,1]]))