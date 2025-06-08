# basic sliding window: 265ms, 10 times faster than hashing
# while the time complexity is the same...
def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    nums.sort()
    l, r = 0, 0
    res = 0
    while r < n:

        st = set()
        prev = nums[r]
        l = r
        while r < n and nums[r] in [prev, prev+1]:
            prev = nums[r]
            st.add(nums[r])
            if len(st) > k:
                tmp = nums[l]
                st.remove(tmp)
                while nums[l] == tmp:
                    l += 1
            res = max(res, r-l+1)
            r += 1
    print(res)

t = int(input())
for i in range(t):
    solve()




# hashing: TLE
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    mp = Counter(nums)
    keys = list(mp.keys())
    keys.sort()
    total = 0
    q = deque()

    m = len(keys)
    res = 0
    for i in range(m):
        total += mp[keys[i]]
        q.append(mp[keys[i]])
        res = max(res, total)

        if i < m-1 and keys[i+1] != keys[i]+1:
            q.clear()
            total = 0
        if len(q) == k:
            total -= q.popleft()

    print(res)

t = int(input())
for i in range(t):
    solve()


