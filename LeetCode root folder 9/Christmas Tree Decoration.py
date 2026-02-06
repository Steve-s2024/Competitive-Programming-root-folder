# holy shit! I am such a DP expert now. I manage to solve this using knapsack totally because the DP instinct.
# otherwise it gonna be hellish to solve by combinatorics computation

# couldn't solve C but solved D instead
def solve():
    mod = 998244353
    n = int(input())
    nums = [int(e) for e in input().split()]
    mx = max(nums[1:])
    x = 0
    for v in nums[1:]:
        if v < mx-1: x += mx-1-v
    ct = Counter(nums[1:])[mx]
    # print(x, ct)
    if x+(n-ct) <= nums[0]: # all perm allowed
        res = 1
        for i in range(2, n+1):
            res *= i
            res %= mod
        print(res)
        return

    if x > nums[0]:
        print(0)
        return

    # print(ct, nums[0]-x)
    @cache
    def recursive(x, y, re):
        nonlocal n, mod
        if x == 0 and y == 0: return 1
        res = 0
        if y == 0: res += x*recursive(x-1, y, re)
        elif re and x: res += x*recursive(x-1, y, re-1)
        if y: res += y*recursive( x, y-1, re)
        return res%mod
    res = recursive(n-ct, ct, nums[0]-x)
    print(res)



