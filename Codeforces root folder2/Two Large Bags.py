# credit to editorial, it suggests the bottom to top solution, which
# need the coder to realize its greedy, is much easier than the top
# to bottom
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    mp1 = defaultdict(int)
    for num in nums:
        mp1[num] += 1

    max_, min_ = max(mp1.keys()), min(mp1.keys())
    flag = True
    for i in range(min_, max_, 1):
        if mp1[i] == 1:
            flag = False
            break
        if mp1[i] != 0:
            mp1[i+1] += mp1[i]-2

    if flag and mp1[max_] % 2 == 0:
        print('yes')
    else:
        print('no')

t = int(input())
for tt in range(t):
    solve()



# the way the solution goes form top to bottom can easier result in
# mistake, so I have to be very careful each line of code
from collections import defaultdict, deque, Counter
import heapq, math

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    mp1, mp2 = defaultdict(int), defaultdict(int)
    for num in nums:
        mp1[num] += 1

    max_, min_ = max(mp1.keys()), min(mp1.keys())
    base = mp1[min_]
    for i in range(max_, min_-1, -1):
        if mp2[i+1] != 0:
            if mp1[i] <= mp2[i+1]:
                diff = mp2[i + 1] - mp1[i]
                mp1[i] += diff+1
                mp2[i] += diff+1

        if (mp1[i]-mp2[i+1])%2 == 1:
            mp1[i] += 1
            mp2[i] += 1
    diff = mp1[min_] - mp2[min_+1]
    if mp1[min_] == base and diff >= 1 and diff%2 == 0:
        print('Yes')
    else:
        print('No')




t = int(input())
for tt in range(t):
    solve()