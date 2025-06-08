# TLE
from collections import defaultdict, deque, Counter

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    mp = Counter(nums)
    keys = list(mp.keys())
    keys.sort()
    m = len(keys)
    flag = 4
    prev = keys[0]-1
    for i in range(m):
        key, val = keys[i], mp[keys[i]]

        if prev+1 != key:
            flag = 4

        if val in range(2, 4):
            flag //= 2
        elif val >= 4:
            flag  = 1

        if flag == 1:
            break
        prev = key

    if flag == 1:
        print('Yes')
    else:
        print('No')



t = int(input())
for i in range(t):
    solve()


