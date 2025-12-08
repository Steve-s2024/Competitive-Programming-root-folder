# damn!
# initially after I discovered the approach, I was having two times the code as now, but then I halved it
# by optimizing my approach and get rid-off the redundancy (which is not simple), it requires a lot of observation
# made. not to mention the initial approach is also observation heavy.
# I now feels that I can make good quality observation and often lead to much advance discovery I won't be
# able to do before

# this is the 4th 1700 problem solved.




def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    if k <= 2:
        print('Yes')
        return
    arr = sorted(nums)
    st = set(arr[:k-1])
    x = arr[k-2]

    idc = []
    for i in range(n):
        if nums[i] in st: idc.append(i)

    m = len(idc)
    l, r = 0, m-1
    ct = 0
    while l <= r:
        i, j = idc[l], idc[r]
        if nums[i] != nums[j]:
            ct += 1
            if nums[i] == x: l += 1
            elif nums[j] == x: r -= 1
            else:
                print('No')
                return
        else: l, r = l+1, r-1

    if m-ct >= k-1: print('Yes')
    else: print('No')





t = int(input())
for i in range(t): solve()

