t = int(input())
for tt in range(t):
    [n, k, x] = [int(e) for e in input().split(' ')]
    nums = [int(e) for e in input().split(' ')]
    # [n, k, x] = [15, 97623,1300111]
    # nums = [105, 95, 108, 111, 118,101, 95, 118, 97, 108, 111, 114, 97, 110, 116]
    total = 0
    prefix = []
    for num in nums:
        total += num
        prefix.append(total)

    multiple = x // total
    remain = x % total
    # print(total, multiple, remain)
    if multiple > k:
        print(0)
    elif multiple == k:
        if remain == 0:
            print(1)
        else:
            print(0)
    else:
        extra = n * (k - multiple - 1)
        i = 0
        while i < len(prefix):
            if prefix[-1] - prefix[i] < remain:
                break
            i += 1
        print(i + 1 + extra)
