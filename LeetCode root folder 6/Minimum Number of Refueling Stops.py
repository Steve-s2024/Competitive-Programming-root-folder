# I blame it on the deceptive constraint stations.length <= 500, I makes me think that the solution must be at least
# O(n*2) and not n*log(n): 27%
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        maxheap = []
        stations.append([0, 0])
        stations.sort(key=lambda i: i[0])

        n = len(stations)
        tank = startFuel
        tot = 0
        cnt = 0
        i = 1
        while i < n:
            while i < n and tot + tank >= stations[i][0]:
                heapq.heappush(maxheap, -stations[i][1])
                dst = stations[i][0] - stations[i - 1][0]
                tot += dst
                tank -= dst
                i += 1
            if tot + tank >= target:
                return cnt
            elif not maxheap:
                return -1

            mx = -heapq.heappop(maxheap)
            tank += mx
            cnt += 1

        while maxheap and tot + tank < target:
            tank += -heapq.heappop(maxheap)
            cnt += 1
        if tot + tank < target: return -1
        return cnt




# DP knap-sack solution: TLE
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([0, 0])
        stations.sort(key = lambda i:i[0])
        n = len(stations)

        @cache
        def recursive(startFuel, i):
            if target-stations[i-1][0] <= startFuel: return 0
            if i >= n:
                if startFuel >= target-stations[-1][0]: return 0
                else: return inf

            dst = stations[i][0] - stations[i-1][0]
            if startFuel-dst < 0: return inf

            _, fuel = stations[i]
            res = min(
                recursive(startFuel - dst, i+1),
                recursive(startFuel - dst + fuel, i+1) + 1
            )
            return res
        res = recursive(startFuel, 1)
        if res == inf: return -1
        return res