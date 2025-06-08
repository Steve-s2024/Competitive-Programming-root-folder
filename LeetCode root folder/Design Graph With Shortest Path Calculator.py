# use Dijkstra, and thats all...: 58% 
from collections import deque, defaultdict
from typing import List
import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for a, b, cost in edges:
            self.graph[a].append((cost, b)) 

    def addEdge(self, edge: List[int]) -> None:
        [a, b, cost] = edge
        self.graph[a].append((cost, b))

    def shortestPath(self, node1: int, node2: int) -> int:
        visited = set()
        minHeap = [(0, node1)]
        heapq.heapify(minHeap)
        while minHeap:
            [curCost, node] = heapq.heappop(minHeap)
            if node == node2:
                return curCost
            if node in visited:
                continue
            visited.add(node)
            for cost, nextNode in self.graph[node]:
                if nextNode not in visited:
                    heapq.heappush(minHeap, (curCost+cost, nextNode))
        return -1