# 更复杂的返回贪心问题, 维护油量和距离： 78%
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        arr = []
        for p, f in stations:
            if p > target: continue
            arr.append((p, f))
        stations = arr
        stations.sort(key=lambda i: i[0])
        f = startFuel
        d = 0
        maxheap = []
        res = 0

        for i in range(n):
            nd = stations[i][0]
            inc = nd - d
            f -= inc
            while f < 0 and maxheap:
                f -= heappop(maxheap)
                res += 1
            # print(i, maxheap, f)
            if f < 0: return -1
            heappush(maxheap, -stations[i][1])
            d = nd

        inc = target - d
        f -= inc
        while f < 0 and maxheap:
            f -= heappop(maxheap)
            res += 1
        # print(maxheap, f)
        if f < 0: return -1
        return res
