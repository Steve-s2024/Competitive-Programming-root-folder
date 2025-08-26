from collections import defaultdict, deque, Counter
import heapq, math
import sys

sys.setrecursionlimit(100000000)



def solve():
    n = int(input())
    s = input()

    mp = defaultdict(int)
    for i in range(n-1):
        a, b = s[i], s[i+1]
        cur = a+b
        mp[cur] += 1

    mx = 0
    res = ''
    for key, val in mp.items():
        if val > mx:
            mx = val
            res = key

    print(res)





solve()
