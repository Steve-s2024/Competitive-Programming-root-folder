# turns out to build a MST, you don't care the minPath to each node,
# instead because you collect the weight of edges to the sum of the
# MST, in order to minimize the sum you just always pick the new edge
# to new node which has the least weight, it's a variation of Dijkstra
#: 5%

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                [x1, y1], [x2, y2] = points[i], points[j]
                dst = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, dst))
                graph[j].append((i, dst))

        # print(graph)

        def getMSTSum(root):
            minHeap = [(0, root)]
            heapq.heapify(minHeap)
            visited = set()
            sm = 0
            while minHeap:
                (curDst, node) = heapq.heappop(minHeap)
                if node not in visited:
                    visited.add(node)
                    sm += curDst
                    for nextNode, dst in graph[node]:
                        heapq.heappush(minHeap, (dst, nextNode))
            return sm

        return getMSTSum(0)


# pretty interesting question, attempt to build a MST with Dijkstra
# guess Dijkstra is not how you build MST...
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                [x1, y1], [x2, y2] = points[i], points[j]
                dst = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, dst))
                graph[j].append((i, dst))

        # print(graph)

        def getMSTSum(root):
            minHeap = [(0, root, 0)]
            heapq.heapify(minHeap)
            visited = set()
            sm = 0
            while minHeap:
                (weight, node, dst) = heapq.heappop(minHeap)
                if node not in visited:
                    cur = weight
                    sm += dst
                    visited.add(node)
                    for nextNode, dst in graph[node]:
                        heapq.heappush(minHeap, (cur + dst, nextNode, dst))
            return sm

        return getMSTSum(0)