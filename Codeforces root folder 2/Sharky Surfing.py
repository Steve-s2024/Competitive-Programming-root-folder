# MLE max heap solution
import heapq, math


def solve():
    n, m, L = [int(e) for e in input().split()]
    intervals = []
    for i in range(n):
        intervals.append([int(e) for e in input().split()])
    if n and intervals[0][0] == 1:
        print(-1)
        return

    arr = [[] for i in range(L+1)]
    for i in range(m):
        pos, bst = [int(e) for e in input().split()]
        arr[pos].append(bst)
    # print(arr)

    res = 0
    jump = 1
    maxHeap = []
    j = 0
    i = 1
    while i <= L:
        if j < len(intervals) and i == intervals[j][0]:
            gap = intervals[j][1]-intervals[j][0]+2
            while maxHeap and jump < gap:
                # print(maxHeap)
                res += 1
                jump += -heapq.heappop(maxHeap)
            if jump >= gap:
                i = intervals[j][1]+1
            else:
                print(-1)
                break
            j+=1
        for power in arr[i]:
            heapq.heappush(maxHeap, -power)
        i += 1
    else:
        print(res)

t = int(input())
for tt in range(t):
    solve()
