# tried so many different ways (lazy seg tree, weighted interval merging... brute force...)
# finally! with my advance interval merging (weighted) saved the day
# this result does tell me about my inefficient lazy tree implementation (likely huge constant overhead)
from heapq import heapify, heappush, heappop
from math import gcd, lcm, inf, sqrt, floor, ceil, comb

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


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    ar = []
    for i in range(1, n): ar.append(abs(nums[i]-nums[i-1]))



    stk = []
    le = [-1]*(n-1)
    for i in range(n-2, -1, -1):
        while stk and stk[-1][0] > ar[i]: le[stk.pop()[1]] = i
        stk.append([ar[i], i])
    stk = []
    ri = [n-1]*(n-1)
    for i in range(n-1):
        while stk and stk[-1][0] > ar[i]: ri[stk.pop()[1]] = i
        stk.append([ar[i], i])

    # print(ar)
    # print(le, ri)

    itv = []
    # mp = [0]*n
    vs = [0]*n
    for i, v in enumerate(ar):
        if i < vs[v]: continue
        l, r = le[i], ri[i]
        a, b = ar[l] if l >= 0 else 0, ar[r] if r < n-1 else 0
        m = r - l - 1
        # for j in range(max(a, b)+1, v+1): mp[j] += m * (m + 1) // 2
        itv.append([max(a, b)+1, v, m*(m+1)//2])
        vs[v] = r

    # print(itv)
    # print(merge(itv))
    mp = [0]*n
    ar, wei = merge(itv)
    # print(ar, wei)
    for i in range(len(ar)):
        l, r = ar[i]
        w = wei[i]
        for j in range(l, r+1): mp[j] = w
    # print(mp)
    print(' '.join(str(e) for e in mp[1:]))

for _ in range(int(input())): solve()






