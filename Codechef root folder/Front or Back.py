
# fking question is hard to understand precise what it means

import heapq, math
from collections import defaultdict, deque, Counter

def solve():
    n = int(input())
    nums = [int(e) for e in input().split(' ')]
    nums.sort()
    MOD = 998244353
    flag = True
    mp = defaultdict(int)
    n1, n2 = 0, 0
    for i in range(n):
        a, b = nums[i], n-1-nums[i]
        mp[min(a, b)] += 1
        if nums[i] == n1:
            n1 += 1
        elif nums[i] == n2:
            n2 += 1
        else:
            flag = False
            break
    if flag:
        res = 1
        # print(mp)
        for val in mp.values():
            if val == 2:
                res *= 2
                res %= MOD
        print(res)
    else:
        print(0)



t = int(input())
for tt in range(t):
    solve()




# maximum recursion depth exceeded

def solve():
    n = int(input())
    nums = [int(e) for e in input().split(' ')]
    MOD = 998244353
    mp = Counter(nums)
    dp = {}
    def recursive(i):
        nonlocal n, MOD
        if i in dp:
            return dp[i]
        if i >= n:
            return 1
        a, b = i, n-1-i
        res = 0
        if a in mp and mp[a]:
            mp[a] -= 1
            res += (mp[a]+1) * recursive(i+1)
            mp[a] += 1
        if b != a and b in mp and mp[b]:
            mp[b] -= 1
            res += (mp[b]+1) * recursive(i+1)
            mp[b] += 1
        res %= MOD
        dp[i] = res
        return res
    res = recursive(0)
    res %= MOD
    print(res)



t = int(input())
for tt in range(t):
    solve()