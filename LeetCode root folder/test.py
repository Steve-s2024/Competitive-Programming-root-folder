
from collections import defaultdict, deque
import heapq, math
from typing import List


from collections import defaultdict, deque
import heapq, math
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        curBus = -1
        n = len(routes)
        # graph[stop] --> all the buses that pass this stop
        graph = defaultdict(list)
        for i in range(n):
            for stop in routes[i]:
                graph[stop].append(i)        

        visited = {}
        q = deque([])
        for bus in graph[source]:
            for stop in routes[bus]:
                if stop not in visited:
                    visited.add(stop)
                    q.append(stop)
        
        res = 1
        while q:
            stop = q.popleft()
            if stop == target:
                return res
            for bus in graph[stop]:
                for nextStop in routes[bus]:
                    if nextStop not in visited:
                        visited.add(nextStop)
                        q.append(nextStop)
            res += 1

        return -1