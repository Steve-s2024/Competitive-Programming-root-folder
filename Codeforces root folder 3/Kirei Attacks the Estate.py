# holy shit it's not easy at all to come to this solution, even though all I did
# is to convert the recursive dfs to iterative dfs, and add another min and max heap.
# my god this could be the most complicated implementation I have ever completed in a
# contest, little time do I have but thank god I finished it after so many wrong answers
from collections import defaultdict, deque, Counter
import heapq, math
import sys

def solve():
    n = int(input())
    dang = [0] # 0 is the placeholder to make query 1-indexed
    dang.extend([int(e) for e in input().split()])
    tree = defaultdict(list)
    for i in range(n-1):
        a, b = [int(e) for e in input().split()]
        tree[a].append(b)
        tree[b].append(a)

    mp = {}
    vis = set()
    maxHeap = [0]
    minHeap = [0]
    arr = [0]
    stack = [(1, 0, dang[1])]
    cntMp = defaultdict(int)
    cntMp[0] = 1
    while stack:
        node, i, sm = stack[-1]
        vis.add(node)
        if i % 2 == 0:
            mp[node] = sm - minHeap[0]
        else:
            mp[node] = -maxHeap[0] - sm
        l = len(stack)
        for nxt in tree[node]:
            if nxt not in vis:
                arr.append(sm)
                cntMp[sm]+=1
                heapq.heappush(maxHeap, -sm)
                heapq.heappush(minHeap, sm)

                stack.append((nxt, i + 1, sm + (-dang[nxt] if i % 2 == 0 else dang[nxt])))
        if len(stack) == l:
            stack.pop()
            cntMp[arr.pop()] -= 1
            while minHeap and cntMp[minHeap[0]] == 0:
                heapq.heappop(minHeap)
            while maxHeap and cntMp[-maxHeap[0]] == 0:
                heapq.heappop(maxHeap)


    res = [0]*n
    for key, val in mp.items():
        res[key-1] = val
    print(' '.join(str(e) for e in res))

t = int(input())
for i in range(t):
    solve()






# stack overflow issue, fix at once

def solve():
    n = int(input())
    dang = [0] # 0 is the placeholder to make query 1-indexed
    dang.extend([int(e) for e in input().split()])
    tree = defaultdict(list)
    for i in range(n-1):
        a, b = [int(e) for e in input().split()]
        tree[a].append(b)
        tree[b].append(a)

    vis = set()
    arr = [0]
    mp = {}
    def dfs(node, i, sm):
        # print(node, i, sm, arr)
        vis.add(node)
        if i%2 == 0:
            mp[node] = sm-min(arr)
        else:
            mp[node] = max(arr)-sm
        for nxt in tree[node]:
            if nxt not in vis:
                arr.append(sm)
                dfs(nxt, i+1, sm+(-dang[nxt] if i%2 == 0 else dang[nxt]))
                arr.pop()

    dfs(1, 0, dang[1])
    # print(mp)
    res = [0]*n
    for key, val in mp.items():
        res[key-1] = val
    print(' '.join(str(e) for e in res))

t = int(input())
for i in range(t):
    solve()
