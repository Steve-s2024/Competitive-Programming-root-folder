# I like this, an easy transformation handles everything, but it's not ordinary
from collections import defaultdict, deque, Counter

def solve():
    n = int(input())
    arr = [int(e) for e in input().split()]
    res = 0
    mp = defaultdict(int)
    for i in range(n):
        res += mp[i-arr[i]]
        mp[arr[i]+i] += 1

    print(res)


solve()