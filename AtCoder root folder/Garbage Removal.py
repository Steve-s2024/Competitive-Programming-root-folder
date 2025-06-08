# almost thought it will fail, watched it pass all 40 tcs
# 1.7 second is very close to TLE
from collections import defaultdict, deque, Counter
import cmath, heapq



def solve():
    h, w, n = [int(e) for e in input().split()]

    rowMp = defaultdict(set)
    colMp = defaultdict(set)
    visited = set()
    st = set()
    for i in range(n):
        x, y = [int(e) for e in input().split()]
        st.add((x, y))
        rowMp[x].add(y)
        colMp[y].add(x)

    q = int(input())
    for i in range(q):
        a, b = [int(e) for e in input().split()]
        if (a, b) in visited:
            print(0)
            continue
        visited.add((a, b))

        if a == 1:
            print(len(rowMp[b]))
            for y in rowMp[b]:
                colMp[y].remove(b)
        elif a == 2:
            print(len(colMp[b]))
            for x in colMp[b]:
                rowMp[x].remove(b)


solve()

