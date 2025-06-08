# boring question, though good for practicing problem solving
# skill for the simplifying branch. the key to solve it is to
# simplify the question to easier questions that points to the 
# same result (asking for the same thing, but in a different way)
from collections import defaultdict, deque, Counter
import heapq, math

def solve():
    [n, x] = [int(e) for e in input().split()]
    s = str(bin(x))[2:]
    m = len(s)
    cnt = 0
    i = m-1
    while i >= 0:
        if s[i] != '1':
            break
        cnt+=1
        i-=1
    res = []
    best = 1 << cnt
    for i in range(min(best, n)):
        res.append(str(i))
    if res and int(res[-1]) < (1 << (len(s)-1)) and best >= n:
        res.pop()
        res.append(str(x))
    for i in range(best, n):
        res.append(str(x))
    print(' '.join(res))





t = int(input())
for tt in range(t):
    solve()