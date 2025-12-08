# an algorithm to find the diameter of a given tree, note that the diameter of a tree is the maximum path among all the
# shortest path of 2 nodes in the tree
# complexity: O(V+E)
from collections import deque

# take in g (lists of child node of each node) and n (number of nodes), return the diameter of the tree
def bfs(g, n):
    deg = [len(r) for r in g]
    vis = [0] * n
    q = deque()
    for u in range(n):
        if deg[u] == 1:
            vis[u] = 1
            q.append(u)

    res = 0
    while q:
        l = len(q)
        for _ in range(l):
            u = q.popleft()
            for v in g[u]:
                if vis[v]: continue
                deg[v] -= 1
                if deg[v] == 1:
                    vis[v] = 1
                    q.append(v)
        if l == 1 and not q: return 2 * res
        if l == 2 and not q: return 2 * res + 1
        res += 1
    return 0