# about the same level of toughness as C, better description and more interesting though

from bisect import bisect_left, bisect_right


def solve():
    n, q = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    nums.sort()
    pre = [0]*n
    for i in range(n): pre[i] = pre[i-1] + ((nums[i]-nums[i-1]-1) if i else 0)
    # print(nums)
    ans = []
    for i in range(q):
        x, y = [int(e) for e in input().split()]
        j = bisect_left(nums, x)
        if j >= n:
            ans.append(x+y-1)
            continue
        t = 0 if nums[j] == x else (nums[j]-x)
        if t >= y:
            ans.append(x+y-1)
            continue
        l, r = j, n-1
        res = -1
        while l <= r:
            m = (l+r)//2
            mis = pre[m]-pre[j] + t
            if mis < y:
                X = y - mis
                res = nums[m] + X
                l = m+1
            else: r = m-1
        ans.append(res)

    for v in ans: print(v)


solve()
