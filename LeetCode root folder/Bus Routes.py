# what a genius am I, now I can design my own bus app
# for route selection 😂: 90%

from collections import defaultdict, deque
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        # graph[stop] --> all the buses that pass this stop
        graph = defaultdict(list)
        for i in range(n):
            for stop in routes[i]:
                graph[stop].append(i)        

        visitedBus = set()
        visited = set()
        q = deque([])
        for bus in graph[source]:
            visitedBus.add(bus)
            for stop in routes[bus]:
                if stop not in visited:
                    visited.add(stop)
                    q.append(stop)
        res = 1
        while q:
            l = len(q)
            while l:
                stop = q.popleft()
                if stop == target:
                    return res
                for bus in graph[stop]:
                    if bus in visitedBus:
                        continue
                    visitedBus.add(bus)
                    for nextStop in routes[bus]:
                        if nextStop not in visited:
                            visited.add(nextStop)
                            q.append(nextStop)
                l-=1
            res += 1

        return -1


#  bfs solution, I am overcomplicating the question, and even
# tried with a variation of Dijkstras, but this will work:TLE

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        # graph[stop] --> all the buses that pass this stop
        graph = defaultdict(list)
        for i in range(n):
            for stop in routes[i]:
                graph[stop].append(i)        

        visited = set()
        q = deque([])
        for bus in graph[source]:
            for stop in routes[bus]:
                if stop not in visited:
                    visited.add(stop)
                    q.append(stop)
        
        res = 1
        while q:
            l = len(q)
            while l:
                stop = q.popleft()
                if stop == target:
                    return res
                for bus in graph[stop]:
                    for nextStop in routes[bus]:
                        if nextStop not in visited:
                            visited.add(nextStop)
                            q.append(nextStop)
                l-=1
            res += 1

        return -1