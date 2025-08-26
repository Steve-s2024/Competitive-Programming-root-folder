# shocking solution...: 80%
# what in the world is this... it is not possible to analyze the time complexity accurately, otherwise I would
# get to this solution very soon
class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dfs(n):
            if n == 0: return 0
            return 1 + min(dfs(n//2)+n%2, dfs(n//3)+n%3)
        return dfs(n)-1



# NeetCode hint, better but tle
class Solution:
    def minDays(self, n: int) -> int:
        minheap = [(n, 0)]
        mi = inf
        while minheap:
            re, cnt = heapq.heappop(minheap)
            if cnt >= mi: continue
            if re == 0: mi = min(mi, cnt)
            heapq.heappush(minheap, (re // 2, cnt + 1 + re % 2))
            heapq.heappush(minheap, (re // 3, cnt + 1 + re % 3))

        return mi - 1



# Dijkstra, better but still tle
class Solution:
    def minDays(self, n: int) -> int:
        minheap = [(n, 0)]
        mi = inf
        while minheap:
            re, cnt = heapq.heappop(minheap)
            if re == 0: mi = min(mi, cnt)
            if cnt + 1 >= mi: continue

            if re%2 == 0: heapq.heappush(minheap, (re//2, cnt+1))
            if re%3 == 0: heapq.heappush(minheap, (re//3, cnt+1))
            heapq.heappush(minheap, (re-1, cnt+1))

        return mi


# DP tle
class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def recursive(n):
            if n == 0: return 0
            res = inf
            if n%2 == 0:
                res = recursive(n//2)
            if n%3 == 0:
                res = min(res, recursive(n//3))
            res = min(res, recursive(n-1))
            return res+1
        return recursive(n)