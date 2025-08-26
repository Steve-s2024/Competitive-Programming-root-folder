# uhm... not easy, and quite boring

from collections import defaultdict, deque, Counter
import heapq, math
from linecache import cache


def solve():
    n, k = [int(e) for e in input().split()]
    s = input()
    mp = Counter(s)
    if mp['1'] <= k:
        print('Alice')
        return

    if n < 2*k: print('Alice')
    else: print('Bob')


t = int(input())
for i in range(t):
    solve()

