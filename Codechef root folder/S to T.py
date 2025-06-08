# funny one
import heapq, math
from collections import defaultdict, deque

def solve():
    n = int(input())
    s = input()
    t = input()
    seq = []
    i1, i2 = 0, 0
    while i1 < n and s[i1] != '1':
        i1 += 1
    while i2 < n and t[i2] != '1':
        i2 += 1
    if i2 != i1:
        print(-1)
    else:
        for i in range(i1+1, n):
            if s[i] == '0':
                seq.append(str(i))
        for i in range(n-1, i1-1, -1):
            if t[i] == '0':
                seq.append(str(i))


        print(len(seq))
        if seq:
            print(' '.join(seq))

t = int(input())
for tt in range(t):
    solve()