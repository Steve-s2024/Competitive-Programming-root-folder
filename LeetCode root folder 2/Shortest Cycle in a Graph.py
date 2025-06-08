# bfs finding solution, finding the shortest
# cycle is the same as finding the shortest path,
# only that the path connects to itself: 24%
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        minCycle = float('inf')
        for start in range(n):
            q = deque([start])
            visited = {}
            visited[start] = 0
            pl = 0
            while q:
                l = len(q)
                flag = False
                while l:
                    node = q.popleft()
                    for nextNode in graph[node]:
                        if nextNode in visited and visited[nextNode] in [pl+1, pl]:
                            # cycle merged
                            cycleLen = pl+1 + visited[nextNode]
                            # print(start, node, nextNode, cycleLen)
                            minCycle = min(minCycle, cycleLen)
                            flag = True
                        if nextNode not in visited:
                            visited[nextNode] = pl+1
                            q.append(nextNode)
                    l -= 1
                if flag:
                    break
                pl += 1
        return minCycle if minCycle != float('inf') else -1