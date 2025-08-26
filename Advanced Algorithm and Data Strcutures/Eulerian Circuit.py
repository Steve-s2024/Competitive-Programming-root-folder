# to traverse an Eulerian circuit, the in and out edge count on each node must be exactly the same
# here the approach is using Hierholzer's algorithm to traverse EC, which is simply a post-order DFS traversal
# a reminder, EC is a circuit which visited every edge of a graph exactly once, it starts and end at the same node
# I haven't yet fully understand why post-order-dfs is enough for finding the Eulerian path
from collections import defaultdict


data = edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],  # closes first cycle

    [1, 4],
    [4, 5],
    [5, 1],  # cycle through 1-4-5-1

    [2, 6],
    [6, 7],
    [7, 2],  # cycle through 2-6-7-2

    [0, 8],
    [8, 9],
    [9, 0],  # cycle through 0-8-9-0
]

graph = defaultdict(list)
for u, v in data:
    graph[u].append(v)
    graph[v].append(u)

vis = set()
def dfs(node):
    for nxt in graph[node]:
        if (node, nxt) not in vis:
            vis.add((node, nxt))
            vis.add((nxt, node))
            dfs(nxt)
            print(node, '->', nxt)

# dfs(beginNode) when called, the path (in reverse order) will be printed
dfs(0)
