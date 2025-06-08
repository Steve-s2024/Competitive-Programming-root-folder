# deprecated


print('Yes')
i = n - 1
while i >= 0 and s[i] != '0':
    i -= 1

if dp[i] > k:
    dp[i] = 0
minDiff = float('inf')
offset = 0
for j in range(i, n):
    diff = k - dp[j]
    if dp[j] < 0:
        offset += -dp[j]
    minDiff = min(minDiff, diff + offset)

res = []
for j in range(n):
    if j == i:
        res.append(str(nums[j] + minDiff))
    else:
        res.append(str(nums[j]))
print(' '.join(res))

from collections import defaultdict, deque, Counter
import heapq, math


def solve():
    n, k = [int(e) for e in input().split()]
    s = input()
    nums = [int(e) for e in input().split()]
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = nums[i]
        if dp[i - 1] > 0:
            dp[i] += dp[i - 1]

    if max(nums) > k:
        print('No')
    elif max(dp) == k:
        print('Yes')
        print(' '.join([str(e) for e in nums]))
    else:
        cnt = Counter(s)['0']
        if cnt == 0:
            print('No')
        else:
            if cnt > 1:

            print('Yes')
            i = n - 1
            while i >= 0 and s[i] != '0':
                i -= 1

            minDiff = float('inf')
            offset = 0
            for j in range(i, n):
                diff = k - dp[j]
                if dp[j] < 0:
                    offset += -dp[j]
                minDiff = min(minDiff, diff + offset)
            # print(i, minDiff)
            res = []
            for j in range(n):
                if i == j:
                    res.append(str(nums[j] + minDiff))
                else:
                    res.append(str(nums[j]))
            print(' '.join(res))


t = int(input())
for tt in range(t):
    solve()

