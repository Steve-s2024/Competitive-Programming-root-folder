# can't believe it can be achieved by this algorithm (bellman ford)
# credit for (neetcode, bellman):31%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        arr = [float('inf')] * n
        tmp = [float('inf')] * n
        arr[src] = 0
        for i in range(k+1):
            for a, b, price in flights:
                tmp[b] = min(tmp[b], arr[a]+price)
            # print(tmp)
            arr = tmp[:]

        # print(arr[dst])
        return arr[dst] if arr[dst] != float('inf') else -1

# haha, it turns out I'm over complicating the whole situation
# you don't even need to be worried about try out all the
# possible path when doing dfs (cause the k is not bigger than
# 100, so all possible path is not too much)
# so, I just removed the visited hash set. also, because the
# visited is removed, I can comfortably use dp: 10%
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, destination, price in flights:
            graph[source].append((destination, price))


        source, destination = src, dst
        dp = {}
        def dfs(src, remain):
            state = (src, remain)
            if state in dp:
                return dp[state]
            nonlocal destination
            if src == destination:
                return 0
            if remain == 0:
                return float('inf')
            res = float('inf')
            for dst, price in graph[src]:
                res = min(dfs(dst, remain-1) + price, res)
            dp[state] = res
            return res
        res = dfs(source, k+1)
        if res == float('inf'):
            return -1
        return res


# really don't know if dp work in this case... and how would i
# complete the dp if it does work
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, destination, price in flights:
            graph[source].append((destination, price))


        source, destination = src, dst
        visited = set()
        dp = {}
        def dfs(src, remain):
            state = (src, remain)
            if state in dp:
                return dp[state]
            nonlocal destination
            if src == destination:
                return 0
            if remain == 0:
                return float('inf')
            res = float('inf')
            visited.add(src)
            for dst, price in graph[src]:
                if dst not in visited:
                    res = min(dfs(dst, remain-1) + price, res)
            visited.remove(src)
            dp[state] = res
            return res
        res = dfs(source, k+1)
        if res == float('inf'):
            return -1
        return res

# dfs finding the min cost path actually worked, now I wonder
# when will dfs not work for finding the min path
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, destination, price in flights:
            graph[source].append((destination, price))


        source, destination = src, dst
        visited = set()
        def dfs(src, remain):
            nonlocal destination
            if src == destination:
                return 0
            if remain == 0:
                return float('inf')
            res = float('inf')
            visited.add(src)
            for dst, price in graph[src]:
                if dst not in visited:
                    res = min(dfs(dst, remain-1) + price, res)
            visited.remove(src)
            return res
        res = dfs(source, k+1)
        if res == float('inf'):
            return -1
        return res

