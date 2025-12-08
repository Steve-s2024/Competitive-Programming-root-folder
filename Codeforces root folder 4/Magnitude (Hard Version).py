# not a bad problem, you need to really think hard and make observation until reduce the code to really short
# I didn't even think the code could be reduced to so simple before I did
from collections import deque, Counter, defaultdict

def solve():
    mod = 998244353
    n = int(input())
    nums = [int(e) for e in input().split()]
    lw, hi = nums[0], abs(nums[0])
    mp = defaultdict(int)
    mp[nums[0]] += 1
    mp[abs(nums[0])] += 1
    for i in range(1, n):
        lw += nums[i]
        hi += nums[i]
        tmp = defaultdict(int)
        tmp[lw] = (tmp[lw] + mp[lw - nums[i]]) % mod
        tmp[abs(lw)] = (tmp[abs(lw)] + mp[lw - nums[i]]) % mod
        if lw != hi:
            tmp[hi] = (tmp[hi] + mp[hi-nums[i]]) % mod
            tmp[abs(hi)] = (tmp[abs(hi)] + mp[hi-nums[i]]) % mod
        hi = max(hi, abs(lw))
        mp = tmp

    # print(mp)
    print(mp[max(mp.keys())])




t = int(input())
for i in range(t): solve()