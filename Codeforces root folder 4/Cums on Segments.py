# another 1600 squashed! let's go

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    idx = -1
    for i in range(n):
        if nums[i] not in [-1, 1]: idx = i

    st = set()
    mi, mx = 0, 0
    l, r = 0, 0
    for i in range(idx):
        l = min(nums[i]+l, nums[i])
        r = max(nums[i]+r, nums[i])
        mi, mx = min(mi, l), max(mx, r)

    if idx != -1:
        l, r = min(l, 0), max(r, 0)
        mi2, mx2 = inf, -inf
        for i in range(idx, n):
            l += nums[i]
            r += nums[i]
            mi2 = min(mi2, l)
            mx2 = max(mx2, r)
        for i in range(mi2, mx2+1): st.add(i)

    l, r = 0, 0
    for i in range(idx+1, n):
        l = min(nums[i]+l, nums[i])
        r = max(nums[i]+r, nums[i])
        mi, mx = min(mi, l), max(mx, r)

    # print(mi, mx)
    for i in range(mi, mx+1): st.add(i)
    # print(st)
    ans = list(st)
    ans.sort()
    print(len(ans))
    print(' '.join(str(e) for e in ans))

t = int(input())
for i in range(t): solve()


