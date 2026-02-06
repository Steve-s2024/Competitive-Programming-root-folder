# thank you codeforces to allow me solve this question at the last 5 mins
# at least I'm not entirely hopeless
def solve():
    [n, k] = [int(e) for e in input().split(' ')]
    bars = [int(e) for e in input().split(' ')]
    bars.sort()
    left, right = 0, n
    diffs = []
    l, r = 0, 0
    vals = []
    keys = []
    while r < n:
        while r < n and bars[r] == bars[l]:
            r += 1
        size = r-l
        keys.append(bars[l])
        vals.append(size)
        right -= size
        diff = right - left
        diffs.append(diff)
        left += size
        l = r

    m = len(keys)
    res = 0
    left, right = vals[0], n-vals[0]
    for i in range(1, m):
        # in between keys[i-1] and keys[1]
        if abs(right - left) <= k:
            res += keys[i] - keys[i-1] - 1
        left += vals[i]
        right -= vals[i]

    left, right = 0, n
    for i in range(m):
        right -= vals[i]
        diff = abs(left - right)
        if diff - min(diff, k) <= vals[i]:
            res += 1
        left += vals[i]
    print(res)




t = int(input())
for tt in range(t):
    solve()


# fking driving me mad!!!
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    [n, k] = [int(e) for e in input().split(' ')]
    bars = [int(e) for e in input().split(' ')]
    bars.sort()
    mp = Counter(bars)
    left, right = 0, n
    diffs = []
    l, r = 0, 0
    vals = []
    while r < n:
        while r < n and bars[r] == bars[l]:
            r += 1
        size = r-l
        vals.append(size)
        right -= size
        diff = right - left
        diffs.append(diff)
        left += size
        l = r

    # print(vals)
    # print(diffs)
    m = len(vals)
    left, right = 0, n
    res = 0
    for i in range(m):
        right -= vals[i]
        # print(left, right)
        b = diffs[i]
        a = diffs[i-1] if i > 0 else b
        c = diffs[i+1] if i < m-1 else b
        if b == 0:
            res += 1
        elif b > 0:
            b -= min(b, k, right)
            c -= min(b, k, right-(vals[i+1] if i < m-1 else 0))
            if abs(b) <= abs(c):
                res += 1
        elif b < 0:
            increase = min(-b, k)
            a += min(b, k, left-(vals[i-1] if i > 0 else 0))
            b += min(b, k, left)
            if abs(b) <= abs(a):
                res += 1
        left += vals[i]

    if len(diffs) == 1:
        print(1)
    elif len(diffs) == 2:
        print(2)
    else:
        print(res)

t = int(input())
for tt in range(t):
    solve()
