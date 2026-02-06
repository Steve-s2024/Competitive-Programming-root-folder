# took me thirty minutes to incorporate this jumping mechanism to the
# program, reduce the time complexity from n^2 to n
def solve():
    n = int(input())
    ranges = []
    for i in range(n):
        ranges.append([int(e) for e in input().split()])
    cands = []
    mp = defaultdict(int)
    for a, b in ranges:
        if a == b:
            cands.append(a)
            mp[a] += 1
    cands.sort()

    l, r = 0, 1
    intervals = []
    m = len(cands)
    while r < m:
        while r < m and cands[r] in [cands[r-1]+1, cands[r-1]]:
            r+=1
        intervals.append((cands[l], cands[r-1]))
        l = r
        r += 1

    jump = {}
    for a, b in intervals:
        for i in range(a, b+1):
            jump[i] = b+1
    res = []
    for a, b in ranges:
        if a == b:
            mp[a] -= 1
        i = a
        while i <= b:
            if i not in jump or mp[a] == 0:
                res.append('1')
                break
            i = jump[i]
        else:
            res.append('0')
        if a == b:
            mp[a] += 1
    print(''.join(res))
t = int(input())
for tt in range(t):
    solve()


# too slow, TLE
from collections import defaultdict, deque, Counter
import heapq, math

def solve():
    n = int(input())
    ranges = []
    for i in range(n):
        ranges.append([int(e) for e in input().split()])
    cands = []
    mp = defaultdict(int)
    for a, b in ranges:
        if a == b:
            cands.append(a)
            mp[a] += 1
    cands.sort()

    l, r = 0, 1
    intervals = []
    m = len(cands)
    while r < m:
        while r < m and cands[r] in [cands[r-1]+1, cands[r-1]]:
            r+=1
        intervals.append((cands[l], cands[r-1]))
        l = r
        r += 1

    jump = {}
    for a, b in intervals:
        for i in range(a, b+1):
            jump[i] = b+1
    res = []
    for a, b in ranges:
        if a == b:
            mp[a] -= 1
        i = a
        while i <= b:
            if i not in jump or mp[a] == 0:
                res.append('1')
                break
            i = jump[i]
        else:
            res.append('0')
        if a == b:
            mp[a] += 1
    print(''.join(res))
t = int(input())
for tt in range(t):
    solve()
