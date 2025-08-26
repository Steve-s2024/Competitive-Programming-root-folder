# fking letsgoo!!!!!!!, single-handedly the fking hardest question every solved in a codeforces contest!!!, I'm so
# exciting and also exhausted by the stress and brain-damage

from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    mp = defaultdict(int)
    for num in nums: mp[num] += 1
    # for each i, if mex can be i, then the size to pick must be in the range of [i-1, n-Cnt(i)]
    ans = []
    minheap = []
    mi = float('inf')
    for i in range(n+1):
        # print(minheap)
        # 'i' is the pick size
        x = i # possible that to make MEX up to x (i.e. 0, 1, 2... x) with the current pick size, but not any further
        if mp[x] == 0: mi = min(mi, x+1) # if the array don't have x, then not possible to go beyond x.
        if x < mi: heapq.heappush(minheap, (n-mp[x], x)) # the pick size must not exceed n-mp[x] inorder to get x
        while minheap and minheap[0][0] < i:  # if the pick size is too big that cannot get x
            heapq.heappop(minheap)

        ans.append(min(mi, len(minheap)))

    # print(ans)
    print(' '.join(str(e) for e in ans[::-1]))

t = int(input())
for i in range(t):
    solve()

