# don't know why it didn't work...

from collections import defaultdict, deque, Counter
import heapq, math
import sys


def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    graph = defaultdict(list)
    for i in range(m):
        s, t, w = [int(e) for e in input().split()]
        graph[s].append((t, w))

    vis = set()
    res = float('inf')
    minHeap = [(0, 1, 0, 0)]
    while minHeap:
        weight, node, tar, tot = heapq.heappop(minHeap)
        tot += nums[node-1]
        vis.add(node)
        if node == n:
            res = min(res, tar)
        for nxt, wei in graph[node]:
            if nxt not in vis and tot >= wei:
                heapq.heappush(minHeap, (wei, nxt, max(wei, weight), tot))

    print(res if res != float('inf') else -1)




# dijkstra, didn't work
from collections import defaultdict, deque, Counter
import heapq, math
import sys


def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    graph = defaultdict(list)
    for i in range(m):
        s, t, w = [int(e) for e in input().split()]
        graph[s].append((t, w))

    vis = set()
    res = -1
    minHeap = [(0, 1, 0, 0)]
    while minHeap:
        weight, node, tar, tot = heapq.heappop(minHeap)
        tot += nums[node-1]
        vis.add(node)
        if node == n:
            res = tar
            break
        for nxt, wei in graph[node]:
            if nxt not in vis and tot >= wei:
                heapq.heappush(minHeap, (wei, nxt, max(wei, weight), tot))

    print(res)


t = int(input())
for i in range(t):
    solve()



# brute force dfs and 2D DP, TLE
def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    graph = defaultdict(list)
    for i in range(m):
        s, t, w = [int(e) for e in input().split()]
        graph[s].append((t, w))

    dp = {}
    def dfs(node, tot):
        if (node, tot) in dp:
            return dp[(node, tot)]
        if node == n:
            return 0
        res = float('inf')
        for nxt, wei in graph[node]:
            if wei <= tot+nums[node-1]:
                tmp = max(dfs(nxt, tot+nums[node-1]), wei)
                res = min(res, tmp)
        dp[(node, tot)] = res
        return res

    res = dfs(1, 0)
    print(res if res != float('inf') else -1)




t = int(input())
for i in range(t):
    solve()
