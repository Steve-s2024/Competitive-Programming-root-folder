# very boring implementation of if structures
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    [n, x] = [int(e) for e in input().split(' ')]

    if x == 1:
        if n % 2:
            print(n)
        elif n >= 2:
            print(5+n-2)
        else:
            print(-1)
        return
    elif x == 0:
        if n % 2 == 0:
            print(n)
        elif n>= 2:
            print(5+n-2)
        else:
            print(-1)
    else:

        bi = str(bin(x))[2:]
        res = 0
        m = len(bi)
        cnt = Counter(bi)['1']
        if cnt >= n:
            res = x
        else:
            ones = n-cnt
            for i in range(m):
                res += int(bi[i]) * pow(2, m - 1 - i)

            if ones % 2 == 0:
                res += ones
            elif ones % 2 == 1:
                if cnt >= 2:
                    res += ones+1
                elif cnt == 1:
                    res += 1
                    res += ones
                else:
                    res = -1


        print(res)

t = int(input())
for tt in range(t):
    solve()

