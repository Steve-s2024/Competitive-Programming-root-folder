# dfs dp, tle
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = defaultdict(list)
        for u, v, cost in edges:
            if online[u] and online[v]: graph[u].append((v, cost))

        @cache
        def dfs(node, totCost):
            if node == n - 1: return [True, inf]
            res = [False, -inf]
            for nxt, cost in graph[node]:
                if totCost + cost <= k:
                    a = dfs(nxt, totCost + cost)
                    if a[0]:
                        res[0] = True
                        mi = min(a[1], cost)
                        res[1] = max(res[1], mi)

            return res

        res = dfs(0, 0)
        return res[1]



# double Dijkstra, still fking TLE...
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = defaultdict(list)
        for u, v, cost in edges:
            if online[u] and online[v]: graph[u].append((v, cost))

        vis = set()
        minheap = [[0, 0]]
        while minheap:
            totCost, node = heapq.heappop(minheap)
            if node == n - 1: break
            if node in vis: continue
            vis.add(node)
            for nxt, cost in graph[node]:
                if totCost + cost <= k:
                    heapq.heappush(minheap, (totCost + cost, nxt))
        else:
            return -1

        # maxheap[i] = [minCost, node, totCost]
        maxheap = [[-inf, 0, 0]]
        while maxheap:
            minCost, node, totCost = heapq.heappop(maxheap)
            minCost = -minCost
            if node == n - 1:
                return minCost
            for nxt, cost in graph[node]:
                if totCost + cost <= k:
                    heapq.heappush(maxheap, (-min(minCost, cost), nxt, totCost + cost))





# Dijkstra, TLE on last two cases...
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = defaultdict(list)
        for u, v, cost in edges:
            if online[u] and online[v]: graph[u].append((v, cost))

        # minheap[i] = [minCost, node, totCost]
        maxheap = [[-inf, 0, 0]]
        while maxheap:
            minCost, node, totCost = heapq.heappop(maxheap)
            minCost = -minCost
            if node == n - 1:
                return minCost
            for nxt, cost in graph[node]:
                if totCost + cost <= k:
                    heapq.heappush(maxheap, (-min(minCost, cost), nxt, totCost + cost))

        return -1



# i don't know why this is not fast enough, and it is hitting MLE??
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = defaultdict(list)
        for u, v, cost in edges:
            if online[v]: graph[u].append((v, cost))


        res = -1
        q = deque([[0, inf, 0]])
        while q:
            for _ in range(len(q)):
                node, minCost, totCost = q.popleft()
                if node == n-1:
                    # print(node, minCost, totCost)
                    res = max(res, minCost)
                for nxt, cost in graph[node]:
                    if totCost + cost <= k and online[nxt]:
                        q.append((nxt, min(minCost, cost), totCost + cost))

        return res