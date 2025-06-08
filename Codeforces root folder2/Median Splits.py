# can't figure out...
t = int(input())
for tt in range(t):
    [n, k] = [int(e) for e in input().split(' ')]
    nums = [int(e) for e in input().split(' ')]


    special = [0, 0]
    i = 0
    while i < n and nums[i] > k:
        i += 1
    special[0] = i
    i = n-1
    while i >= 0 and nums[i] > k:
        i -= 1
    special[1] = n-1-i
    i = 0
    while i < n and nums[i] <= k:
        i += 1
    special[0] = max(special[0], i)
    i = n-1
    while i >= 0 and nums[i] <= k:
        i -= 1
    special[1] = max(special[1], n-1-i)
    # now, we have new cnt1 and old cnt2, and we need to have two
    # subarrays that both have their cnt1 <= cnt2.

    prefix = [False] * n
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if nums[i] > k:
            cnt1 += 1
        else:
            cnt2 += 1
        prefix[i] = cnt1 <= cnt2


    suffix = [False] * n
    cnt1, cnt2 = 0, 0
    for i in range(n-1, -1, -1):
        if nums[i] > k:
            cnt1 += 1
        else:
            cnt2 += 1
        suffix[i] = cnt1 <= cnt2

    # print(prefix, suffix)
    # for two out of the three subarrays, they need to have cnt1 <= cnt2
    l, r = 0, 0
    maxSize = 0
    flag = False
    while r < n:
        while r < n and nums[r] > k:
            r += 1
        size = r-l
        if size >= maxSize:
            maxSize = size
            # print(l, r)
            if (
                (l == 0 or prefix[l - 1]) and
                (r >= n - 1 or suffix[r + 1]) and
                n-size > 1 and
                (l > 0 or special[1] != (n-size)/2) and
                (r < n-1 or special[0] != (n-size)/2)
            ):
                flag = True
        r+=1
        l=r

    if flag:
        print('YES')
    else:
        print('NO')