# need to realize that apart from pairing the min and max from the two heap, you also have a third choice
# that is to use the absolute minimum in both array as a bridge to do two exchange with the cost of absmi*2
# for a swap.

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        absmi = min(basket1 + basket2)
        n = len(basket1)
        mp = defaultdict(int)
        for i in range(n):
            mp[basket1[i]] += 1
            mp[basket2[i]] -= 1

        minheap, maxheap = [], []
        for key, val in mp.items():
            if val % 2 != 0: return -1
            while val < 0:
                heapq.heappush(minheap, key)
                val += 1
            while val > 0:
                heapq.heappush(maxheap, -key)
                val -= 1

        res = 0
        while minheap:
            mi, mx = heapq.heappop(minheap), heapq.heappop(maxheap)
            mx = -mx
            if mp[mi] and mp[mx]:
                res += min(mi, mx, absmi * 2)
                mp[mi] += 2
                mp[mx] -= 2
        return res
