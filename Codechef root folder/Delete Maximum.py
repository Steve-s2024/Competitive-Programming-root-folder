# Q5 is too hard for me
# fk!!!, wrong question, this is Q6!!! aahhhhhhhh. no time left for Q5 now fuck!!!!!🤬

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    MOD = 998244353

    pre = [0]*n
    suf = [0]*n
    mi = nums[0]
    for i in range(n):
        mi = min(mi, nums[i])
        pre[i] = mi
    mi = nums[-1]
    for i in range(n-1, -1, -1):
        mi = min(mi, nums[i])
        suf[i] = mi
    # print(pre, suf)

    res = 0
    sl = SortedList(nums)
    sl.remove(nums[-1])
    sl.remove(nums[0])
    for i in range(1, n-1):
        sl.remove(nums[i])
        if pre[i-1] > nums[i]:
            ofs = len(sl) - sl.bisect_left(pre[i-1])
            l = n-i - ofs
            # print(1, nums[i], ofs, l)
            res += l

    sl = SortedList(nums)
    sl.remove(nums[-1])
    sl.remove(nums[0])
    for i in range(n-2, 0, -1):
        sl.remove(nums[i])
        if suf[i+1] > nums[i]:
            ofs = len(sl) - sl.bisect_left(suf[i+1])
            l = i+1 - ofs
            # print(2, nums[i], ofs, l)
            res += l
    res = res + 2*(n+1)
    print(res//2)


t = int(input())
for i in range(t):
    solve()
