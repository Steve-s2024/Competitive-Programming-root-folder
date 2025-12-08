# after solving the question realize it only allow kotlin sumbission
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    comps = []
    arr = []
    for i in range(n):
        if nums[i] == 0:
            if arr: comps.append(arr)
            arr = []
        else: arr.append(nums[i])
    if arr: comps.append(arr)
    # print(comps)

    res = 0
    for comp in comps:
        res += 2 * sum(comp)
        if len(comp)%2 == 0: continue
        mx = comp[0]
        for i in range(0, len(comp), 2): mx = max(mx, comp[i])
        res -= mx
    print(res)


t = int(input())
for i in range(t): solve()