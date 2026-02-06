# by the simple greedy solution that is very obvious, I
# demand this to be ungraded to 1000 rating
from collections import defaultdict, deque, Counter
import heapq, math

def solve():
    a, b = [int(e) for e in input().split()]
    res = [0, 0, 0]
    res[1] = b
    if a >= b:
        res[0] = b
        res[2] = a*3
        res[2] -= 2*b
    else:
        res[2] = b
        res[0] = a * 3
        res[0] -= 2 * b
    # print(res)
    print(len(res))
    print(' '.join([str(e) for e in res]))

# t = int(input())
t = 1
for tt in range(t):
    solve()
