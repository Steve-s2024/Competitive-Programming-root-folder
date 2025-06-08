import heapq

# nlogn interval merging, split interval based on interval overlap
def merge(arr):
    arr = arr[:]
    arr.sort(key = lambda i : i[0])
    inf = float('inf')
    arr.append((inf, inf))
    minHeap = []
    heapq.heapify(minHeap)
    intervals = []
    L, R = arr[0]
    for l, r in arr:
        while minHeap and minHeap[0] < l:
            R = heapq.heappop(minHeap)
            if L <= R:
                intervals.append((L, R))
            L = R+1
        if l > L:
            intervals.append((L, l-1))
        L = l
        heapq.heappush(minHeap, r)

    intervals.pop()
    print(intervals)

merge([[0,1],[1,2],[0,2]])