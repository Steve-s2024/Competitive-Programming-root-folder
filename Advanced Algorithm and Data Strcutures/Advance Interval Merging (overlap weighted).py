from heapq import heappush, heappop
# 2026-01-12 first time ever save the day by this code (Codeforces Round 1072 (Div. 3) E), lazy tree could not beat it
# (with a few modification I changed it into interval with weight)

def merge(arr):
    arr = arr[:]
    arr.sort(key=lambda i: i[0])
    arr.append([inf, inf, inf])
    minHeap = []
    intervals = []
    weights = []
    L, R, _ = arr[0]
    sm = 0
    for l, r, w in arr:
        while minHeap and minHeap[0][0] < l:
            R, W = heappop(minHeap)
            sm -= W
            if L <= R:
                weights.append(sm + W)
                intervals.append((L, R))
            L = R + 1
        if l > L:
            weights.append(sm)
            intervals.append((L, l - 1))
        L = l
        heappush(minHeap, (r, w))
        sm += w

    intervals.pop()
    weights.pop()
    # print(intervals, weights)
    return intervals, weights


import heapq


# improved advance interval merging, new weights array stores the weight of each interval
def merge(arr):
    arr = arr[:]
    arr.sort(key=lambda i: i[0])
    inf = float('inf')
    arr.append((inf, inf))
    minHeap = []
    intervals = []
    weights = []
    L, R = arr[0]
    for l, r in arr:
        while minHeap and minHeap[0] < l:
            R = heapq.heappop(minHeap)
            if L <= R:
                weights.append(len(minHeap) + 1)
                intervals.append((L, R))
            L = R + 1
        if l > L:
            weights.append(len(minHeap))
            intervals.append((L, l - 1))
        L = l
        heapq.heappush(minHeap, r)

    intervals.pop()
    weights.pop()
    print(intervals, weights)



# nlogn interval merging, split interval based on interval overlap
'''def merge(arr):
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
    print(intervals)'''

merge([[0,1],[1,2],[0,2]])