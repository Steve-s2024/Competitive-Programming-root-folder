

# min heap solution TLE on tc.4
def solve():
    n, x = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    minHeap = []
    heapq.heapify(minHeap)
    for num in nums:
        heapq.heappush(minHeap, num)

    prev = -1
    st = set()
    while minHeap:
        cur = heapq.heappop(minHeap)
        if cur not in [prev, prev+1]:
            break
        prev = cur
        if cur in st:
            heapq.heappush(minHeap, cur+x)
        else:
            st.add(cur)

    print(prev+1)



t = int(input())
for i in range(t):
    solve()

