# IDK if its because I am tired, but the problem is so stupidly easy and yet so hard to implement



def solve():
    n, k = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    prv = nums[0]
    frq = []
    ct = 1
    for e in nums[1:]:
        if e != prv:
            frq.append(ct)
            prv, ct = e, 1
        else: ct += 1
    frq.append(ct)

    nums = frq
    nums.sort()
    nums = [0] + nums


    # print(nums)
# [1, 1, 2, 3, 4] -> [1, 2, 3]
    sm = sum(nums)
    n = len(nums)
    sz = len(nums)-1
    res = 0
    i = 1
    if n == 1 and k%sz == 0: res = 1

    while i < n:
        d = nums[i]-nums[i-1]
        x = sm-d*sz
        # print(nums[i], sz)
        if k > x and (k-x)%sz == 0: res += 1
        sm = x
        i += 1
        sz -= 1
        while i < n and nums[i] == nums[i - 1]:
            sz -= 1
            i += 1


    print(res)




for _ in range(int(input())): solve()
