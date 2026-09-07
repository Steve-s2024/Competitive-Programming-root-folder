# oh boy I am just that confident . submit like ever before



def solve():
    n, x = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    l, r = 0, n
    ar = []
    while l+1 < r:
        m = (l+r)//2
        if nums[m] <= x:
            ar.append(m)
            l = m
        else: r = m
    if nums[l] <= x: ar.append(l)

    i = nums.index(x)
    res = []
    if not ar:
        res.append((i, 0))
    else:
        res.append((i, ar[-1]))

    # i, j = res[0]
    # nums[i], nums[j] = nums[j], nums[i]
    # l, r = 0, n
    # while l + 1 < r:
    #     m = (l + r) // 2
    #     if nums[m] <= x: l = m
    #     else: r = m
    # print(nums[l], x)


    print(len(res))
    for i, j in res:
        print(f'{i+1} {j+1}')

for _ in range(int(input())): solve()