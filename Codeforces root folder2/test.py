from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    k = int(input())
    cnt = int(math.sqrt(k))
    # cnt * cnt >= k
    x = cnt-3
    while (x+2)*(x+1) < k:
        x += 1
    # now, it is guaranteed that x*(x+1) is the maximum x can be
    # print(x)
    totalLen = x*(x+1) + x
    remain = k - x*(x+1)
    if remain:
        totalLen += 1
        totalLen += remain

    print(totalLen)


t = int(input())
for i in range(t):
    solve()


