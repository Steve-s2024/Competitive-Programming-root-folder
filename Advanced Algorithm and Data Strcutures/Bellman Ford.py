# a shortest path algorithm that locates the shortest path from one node to all the other node in a graph, similar to
# Dijkstra, but it handles negative weighted edge as an advantage. runtime is O(V*E)

# remember these graph algo will not handle negative cyclic graph as the shortest path weight in that case is -inf.

from math import inf
def bellmanFord(n, edges, src):
    arr = [inf] * n
    tmp = [inf] * n
    arr[src] = 0
    for i in range(n):
        for u, v, p in edges:
            tmp[v] = min(tmp[v], arr[u] + p)
            tmp[u] = min(tmp[u], arr[v] + p)
        arr = tmp[:]
    return arr

print(bellmanFord(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0))
print(bellmanFord(3, [[0,1,100],[1,2,100],[0,2,500]], 0))
print(bellmanFord(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], 0))

