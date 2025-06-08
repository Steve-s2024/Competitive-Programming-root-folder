# didn't even have faith when submitted, but I'm very lucky!
from collections import defaultdict, deque
import heapq, math


t = int(input())
for tt in range(t):
    n = int(input())
    s = input()
    cnt = 0
    for i in range(1, n):
        if s[i] != s[i-1]:
            cnt+=1


    if s[0] == '1':
        cnt += 1
    res = cnt + n
    # print(cnt, n, res)
    if cnt > 2:
        res -= 2
    if cnt == 2:
        res -= 1
    print(res)
