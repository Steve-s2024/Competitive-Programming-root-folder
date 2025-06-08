# this is so not worth to be the third question
# hardly worth the second question...
# i even doubted if it is that simple for a while...
import heapq, math
from collections import defaultdict, deque


def solve():
    arr = [int(e) for e in input().strip().split(' ')]
    # print(arr)
    # x, y, z --> A, B, C
    arr.sort()
    if arr[0] % 2 == 1 and arr[1] % 2 == 1:
        print(arr[0] + arr[1] - 1)
    else:
        print(arr[0] + arr[1])

t = int(input())
for tt in range(t):
    solve()