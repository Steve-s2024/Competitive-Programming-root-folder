# the solution, after several iteration, comes done to testing the ability to avoid visiting the same node multiple
# times, and the technique which I implement is a good way to reduce BFS traversal, or any graph traversal, from n^2
# to linea by using appropriate condition with the visited map: 39%
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        vis = [inf] * n
        vis[0] = 0
        minheap = [(0, 0)]
        res = inf
        while minheap:
            t, node = heapq.heappop(minheap)
            # print(t, node)
            if node == n - 1:
                if res < t:
                    return t
                else:
                    res = t

            mul = (t // change)
            if mul % 2 == 1:
                for nxt in graph[node]:
                    if vis[nxt] == inf:
                        vis[nxt] = (mul + 1) * change + time
                    elif vis[nxt] != -1 and vis[nxt] < (mul + 1) * change + time:
                        vis[nxt] = -1
                    else:
                        continue
                    heapq.heappush(minheap, ((mul + 1) * change + time, nxt))
            else:
                for nxt in graph[node]:
                    if vis[nxt] == inf:
                        vis[nxt] = t + time
                    elif vis[nxt] != -1 and vis[nxt] < t + time:
                        vis[nxt] = -1
                    else:
                        continue
                    heapq.heappush(minheap, (t + time, nxt))

