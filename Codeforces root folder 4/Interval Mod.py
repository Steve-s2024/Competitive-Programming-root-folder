# interesting idea of dominating first operation, followed by operations that can effect the array at will


def solve():
    n, k, p, q = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    ar = [min(e%q%p, e%p) for e in nums]
    sm = sum(ar)
    pre = [0]*n
    for i in range(n): pre[i] = pre[i-1] + ar[i]

    tp = nums[0:k]
    a = sum(e % p for e in tp)
    b = sum(e % q % p for e in tp)
    ans = min(a, b) + sm - pre[k-1]

    for i in range(k, n):
        a += (nums[i]%p) - (nums[i-k]%p)
        b += (nums[i]%q%p) - (nums[i-k]%q%p)
        x = min(a, b) + sm - (pre[i]-pre[i-k])

        ans = min(ans, x)

    print(ans)



for _ in range(int(input())): solve()