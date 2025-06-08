# fk man I crashed this question. confident lost from D is all back
from collections import defaultdict, deque, Counter
import heapq, math
import sys

sys.setrecursionlimit(100000000)

def check(l, r):
    return abs(r-l) != 1


def solve():
    n = int(input())
    arr = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]

    mp1, mp2 = {}, {}
    for i in range(n-1, -1, -1):
        a, b = arr[i], brr[i]
        if a not in mp1:
            mp1[a] = [i, i]
        else:
            mp1[a][0] = i
        if b not in mp2:
            mp2[b] = [i, i]
        else:
            mp2[b][0] = i

        if mp1[a][1] - mp1[a][0] > 0:
            print(i+1)
            return
        if mp2[b][1] - mp2[b][0] > 0:
            print(i+1)
            return
        if a in mp2:
            for l in mp1[a]:
                for r in mp2[a]:
                    if check(l, r):
                        print(i+1)
                        return
        if b in mp1:
            for l in mp1[b]:
                for r in mp2[b]:
                    if check(l, r):
                        print(i + 1)
                        return
    print(0)




t = int(input())
for i in range(t):
    solve()
