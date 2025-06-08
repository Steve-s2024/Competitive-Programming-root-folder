# I have to change the python recursion call limit to complete this
# good thing is I don't need to use c++ everytime trying to
# do heavy recursion

import sys
from collections import defaultdict, deque, Counter
import cmath, heapq
sys.setrecursionlimit(100000000)

def solve():
    n = int(input())
    s = input()
    rec = []
    zero, one = 0, 0
    for c in s:
        if c == '0':
            if one:
                rec.append((1, one))
                one = 0
            zero += 1
        else:
            if zero:
                rec.append((0, zero))
                zero = 0
            one += 1
    if zero:
        rec.append((0, zero))
    if one:
        rec.append((1, one))

    dp = {}
    def recursive(i, tp):
        if (i, tp) in dp:
            return dp[(i, tp)]
        if i >= len(rec):
            return 0
        if tp == 3:
            a = recursive(i+1, tp) + (rec[i][1] if rec[i][0] == 1 else 0)
        elif tp == 2:
            b, c = recursive(i+1, tp+1), recursive(i+1, tp)
            a = min(b, c) + (rec[i][1] if rec[i][0] == 0 else 0)
        else:
            b, c = recursive(i+1, tp+1), recursive(i+1, tp)
            a = min(b, c) + (rec[i][1] if rec[i][0] == 1 else 0)
        dp[(i, tp)] = a
        return a
    print(min(recursive(0, 1), recursive(0, 2)))

t = int(input())
for i in range(t):
    solve()