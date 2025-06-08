# hashing solution: TLE
from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    total = 0
    mp = defaultdict(int)
    mp[0] = 1
    prefix = deque([0])
    res = 0
    for num in nums:
        total += num

        if total in mp:
            # print(total)
            res += 1
            while prefix:
                cur = prefix.popleft()
                mp[cur] -= 1
                if mp[cur] == 0:
                    mp.pop(cur)
        mp[total] += 1
        prefix.append(total)

    print(res)

t = int(input())
for i in range(t):
    solve()


