# bfs solution, "a good question is simple to understand but hard to solve":4
# ms
# Beats
# 26.53%
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)  # the number of nodes
        visited = {}  # map the node --> the group it belongs to
        for i in range(
                n):  # repetitively do bfs to all separate block of the graph, each block must be bipartite in order to make the input graph be bipartite.
            if i in visited:
                continue
            visited[i] = 0  # let the entry point be of group zero
            q = deque([i])
            curGroup = 1
            while q:
                l = len(q)
                while l:
                    cur = q.popleft()
                    for next_ in graph[cur]:
                        if next_ not in visited:
                            q.append(next_)
                            visited[next_] = curGroup
                        elif next_ in visited and visited[next_] != curGroup:
                            return False
                    l -= 1
                curGroup = 1 if curGroup == 0 else 0  # alternate the cur group each time the bfs spread

        return True
