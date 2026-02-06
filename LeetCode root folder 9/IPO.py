# max heap solution
class Solution:
    def findMaximizedCapital(self, k: int, w: int, prof: List[int], capi: List[int]) -> int:
        ar = list(zip(capi, prof))
        ar.sort()
        n = len(ar)
        hp = []
        i = 0
        x = w
        while i < n and x >= ar[i][0]:
            heappush(hp, -ar[i][1])
            i += 1

        ct = 0
        while hp:
            x += -heappop(hp)
            ct += 1
            if ct >= k: return x
            while i < n and x >= ar[i][0]:
                heappush(hp, -ar[i][1])
                i += 1

        return x
