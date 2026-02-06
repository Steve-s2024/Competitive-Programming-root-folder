# pretty interesting, don't know if I can solve it with less
# time then D (flower boy), I think I'm close to the answer
from collections import defaultdict, deque
import heapq, math
def solve():

    [n, q] = [int(e) for e in input().split(' ')]
    perm = [int(e) for e in input().split(' ')]
    hashMap = {}
    for i, p in enumerate(perm):
        hashMap[p] = i

    ans = []
    def getMinSwap(l, r, k):
        target = hashMap[k]
        if target not in range(l, r+1):
            ans.append('-1')
        else:
            lessCnt, greaterCnt = 0, 0
            while l <= r:
                m = (r+l)//2
                if m == target:
                    break
                if m < target:
                    # i want perm[m] to be less than k
                    if perm[m] > k:
                        lessCnt += 1
                    l = m+1
                elif m > target:
                    # i want perm[m] to be greater than k
                    if perm[m] < k:
                        greaterCnt += 1
                    r = m-1
            if lessCnt >= k or greaterCnt > n-k:
                ans.append('-1')
            else:
                ans.append(str(lessCnt+greaterCnt))


    for i in range(q):
        [l, r, k] = [int(e) for e in input().split(' ')]
        getMinSwap(l-1, r-1, k)
    print(' '.join(ans))

t = int(input())
for tt in range(t):
    solve()
