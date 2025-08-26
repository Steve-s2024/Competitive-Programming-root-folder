# hard to realize that you can reduce the time complexity by only maintaining the 3 maximums and 2 minimums, I have the
# idea but keeps thinking in the direction that I have to maintain every child nodes' costs in sorted order so to access
# the 3 maximums and 2 minimums: 42%
class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:

        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        n = len(cost)
        ans = [1]*n
        vis = set()
        def dfs(node):
            maxheap, minheap = [], []
            for nxt in tree[node]:
                if nxt in vis: continue
                vis.add(nxt)
                mxheap, miheap = dfs(nxt)
                while mxheap: heapq.heappush(maxheap, heapq.heappop(mxheap))
                while miheap: heapq.heappush(minheap, heapq.heappop(miheap))
            heapq.heappush(maxheap, -cost[node])
            heapq.heappush(minheap, cost[node])
            while len(maxheap) > 2: heapq.heappop(maxheap)
            while len(minheap) > 3: heapq.heappop(minheap)
            if len(minheap) == 3:
                arr1 = heapq.nlargest(2, maxheap)
                arr2 = heapq.nsmallest(3, minheap)
                a = -arr1[0]*-arr1[1]*arr2[2]
                b = arr2[0]*arr2[1]*arr2[2]
                # print('2 mins', arr1, '3 maxs', arr2)
                # print(node, a, b)
                ans[node] = max(0, a, b)
            return maxheap, minheap
        vis.add(0)
        dfs(0)

        return ans