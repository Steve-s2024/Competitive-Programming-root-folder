# hard one!

def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    if n == 1:
        print(nums[0] + k-1)
        return

    if n > k:
        pre = [0]*n
        for i in range(n): pre[i] = pre[i-1] + nums[i]
        res = 0
        for i in range(k-1, n):
            a = pre[i]-pre[i-k+1]+nums[i-k+1]
            res = max(res, k*(k-1)//2 + a)
        print(res)

    else:
        res = 0
        for i in range(k-1, k-n-1, -1): res += i
        print(res + sum(nums))





for _ in range(int(input())): solve()