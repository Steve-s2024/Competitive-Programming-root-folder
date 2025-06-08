# very tricky question, and tricky approach I have, I have never tried this
# guessing approach before. No problem before requires such approach
# the guessing happens only with the first cut, I have to enumerate through
# both possibility (cut horizontally or vertically, you can think of it like two games with different way to start off)
# and simulate the rest greedily. and then pick the smaller outcome for both games
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n, m, a, b = [int(e) for e in input().split()]
    # a, b is the starting point
    ans = float('inf')
    for i in range(2):
        if i == 0:
            h, w = min(n-a+1, a), m
        else:
            h, w = n, min(b, m-b+1)
        res = 1
        # print(h, w)
        while h * w > 1:
            if h > w:
                h = (h+1)//2
            else:
                w = (w+1)//2
            # print(h, w)
            res += 1
        ans = min(ans, res)
    print(ans)



t = int(input())
for i in range(t):
    solve()


