def solve():
    n, m = [int(e) for e in input().split()]
    ran = []
    for i in range(m):
        l, r = [int(e) for e in input().split()]
        ran.append((l, r))



    ran.sort(key = lambda i:i[0])
    minHeap = []
    j = 0
    mi = float('inf')
    for i in range(1, n+1):
        while minHeap and i > minHeap[0]:
            heapq.heappop(minHeap)
        while j < m and i >= ran[j][0]:
            heapq.heappush(minHeap, ran[j][1])
            j += 1
        mi = min(mi, len(minHeap))
    print(mi)




# t = int(input())
t = 1
for i in range(t):
    solve()
