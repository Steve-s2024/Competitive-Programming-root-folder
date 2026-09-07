# damn! what is this name!



def solve():
    n = int(input())
    nums = [int(x) for x in input().split()]

    nums.sort()
    ar = [nums[0]]
    frq = [0]*n
    frq[nums[0]] += 1
    for i in range(1, n):
        frq[nums[i]] += 1
        if nums[i] > ar[-1]: ar.append(nums[i])

    # print(ar)
    if ar[0] != 0:
        print('No')
        return

    res = []
    rem = [[frq[0], 0]]
    for i in range(1, len(ar)):
        e = ar[i]

        while rem and len(res) < e:
            v = rem[-1][1]
            rem[-1][0] -= 1
            res.append(v)
            if not rem[-1][0]: rem.pop()

        if len(res) < e:
            print('No')
            return

        rem.append([frq[e], e])

    while rem:
        rep, v = rem[-1]
        for _ in range(rep): res.append(v)
        rem.pop()
    # print(res)

    print('Yes')
    print(' '.join(map(str, res)))


solve()