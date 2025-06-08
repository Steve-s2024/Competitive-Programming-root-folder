# minHeap solution, did thought it could work with first try!
import heapq, math
from collections import defaultdict, deque

# cook your dish here
t = int(input())
for tt in range(t):
    [n, k, d] = [int(e) for e in input().split(' ')]
    times = [int(e) for e in input().split(' ')]
    times.sort()

    minHeap = []
    heapq.heapify(minHeap)


    cnt = n
    used = set()
    res = 0
    for day in range(1, d+1):
        # print(day, minHeap)
        while minHeap and minHeap[0][0] <= day:
            used.remove(heapq.heappop(minHeap)[1])
            cnt+=1

        while cnt > k:
            for i in range(n):
                if i not in used:
                    heapq.heappush(minHeap, [day+times[i], i])
                    used.add(i)
                    cnt-=1
                    res+=1
                if cnt <= k:
                    break
    print(res)