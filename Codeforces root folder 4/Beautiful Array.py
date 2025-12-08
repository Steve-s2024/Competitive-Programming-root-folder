# funny that before I made a small change, the code TLE on tc21, but after do nums.sort() at the beginning instead
# of doing arr.sort() at every iteration, the time reduced by at least 10 times. this is really crazy since it should
# not make much difference in my opinion.

# matter of fact, I think my doing sorting separately on smaller array, it actually should speed up the process.
# imagine I break nums into 100 even array, then sort them is (n/100)*log(n/100) * 100 = n*log(n/100) < n*log(n)
# I guess the problem is within the heavy expense of initializing sort().

from collections import deque, Counter, defaultdict

def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    nums.sort()
    mp = defaultdict(list)
    for i in range(n): mp[nums[i]%k].append(nums[i])

    res = 0
    ct = 0
    # print(mp)
    for arr in mp.values():
        ct += len(arr)%2
        if ct >= 2:
            print(-1)
            return
        if len(arr) == 1: continue
        if len(arr)%2 == 0:
            for i in range(1, len(arr), 2): res += (arr[i]-arr[i-1])//k
        else:
            m = len(arr)
            pre = [0]*m
            suf = [0]*m
            for i in range(1, m, 2): pre[i] = pre[i-2]+(arr[i]-arr[i-1])//k
            for i in range(m-2, -1, -2): suf[i] = suf[(i+2)%m]+(arr[i+1]-arr[i])//k
            # print(pre, suf)
            cur = min(suf[1], pre[-2])
            for i in range(1, m-1):
                if i%2 == 1:
                    a, b = pre[i-2] if i-2 >= 0 else 0, suf[i+2] if i+2 < m else 0
                    tmp = (arr[i+1]-arr[i-1])//k + a + b
                    # print(arr[i+1], arr[i-1], a, b)
                else: tmp = pre[i-1] + suf[i+1]
                cur = min(cur, tmp)
            res += cur


    print(res)

t = int(input())
for i in range(t): solve()