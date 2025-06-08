# absolutely boring as hell, all it need is to figure out
# n = 27, and that's it.
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    res = []
    if n % 2 == 0:
        for i in range(n//2):
            res.append(str(i+1))
            res.append(str(i+1))
        print(' '.join(res))
    elif n >= 27:
        res = list('13344556612778899') + '10 10 11 11 12 12 13 13 1 2'.split()
        cnt = 14
        i = 27
        while i < n:
            res.append(str(cnt))
            res.append(str(cnt))
            cnt += 1
            i += 2
        print(' '.join(res))

    else:
        print(-1)

t = int(input())
for i in range(t):
    solve()


