# greedy solution
from collections import defaultdict, deque, Counter


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    mp = Counter(nums)
    if len(mp) == 1:
        print('No')
    else:
        max_ = max(nums)
        print('Yes')
        res = []
        for i in range(n):
            if nums[i] == max_:
                res.append('2')
            else:
                res.append('1')
        print(' '.join(res))

t = int(input())
for tt in range(t):
    solve()

