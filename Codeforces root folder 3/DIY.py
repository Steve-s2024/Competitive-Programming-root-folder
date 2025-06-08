# funniest solution I've never come up with, looks like an arc
# another question solved by greedy approach, only that it is greedy until you can't
# then brute force, this way it is easy to understand and also maintain the efficiency
# I also don't think it can be solved entirely by greedy, the brute force must be there.
from collections import defaultdict, deque, Counter

def sim(a, b, c, d):
    res = [(a, b), (a, d), (c, b), (c, d)]
    area = abs(a-c) * abs(b-d)
    return (res, area)

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    mp = Counter(nums)
    p = []
    for key, val in mp.items():
        if val >= 2:
            p.append([key, val])

    if not p or sum([e[1]//2 for e in p]) < 4:
        print('NO')
    elif len(p) == 1:
        print('YES')
        print(' '.join([str(p[0][0])]*8))
    else:
        keys = [e[0] for e in p]
        keys.sort()
        a, b, c, d = keys[0], keys[1], keys[-2], keys[-1]
        maxArea = -1
        ans = []
        for aa in [a, b]:
            mp[aa] -= 2
            for bb in [a, b]:
                mp[bb] -= 2
                for cc in [c, d]:
                    mp[cc] -= 2
                    for dd in [c, d]:
                        mp[dd] -= 2
                        if min(mp[aa], mp[bb], mp[cc], mp[dd]) >= 0:
                            res, area = sim(aa, bb, cc, dd)
                            if area > maxArea:
                                maxArea = area
                                ans = res
                        # ...
                        mp[dd] += 2
                    mp[cc] += 2
                mp[bb] += 2
            mp[aa] += 2

        print('YES')
        print(' '.join([str(e[0]) + ' ' + str(e[1]) for e in ans]))



t = int(input())
for i in range(t):
    solve()
