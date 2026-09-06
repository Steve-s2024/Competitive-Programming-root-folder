# not a single WA for A to F in a div3 man! hard work finally paid off.
# this F is not even easy gosh! this is pretty freaking hard ngl
# it just flows somehow, the idea, lol



def cnt(ar):
    res, o = 0, 0
    for e in ar:
        if e == 1: o += 1
        else: res += o
    return res


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    s = input()
    ar = []
    i = 0
    while i < n:
        if nums[i] == 1:
            j = i+1
            while j < n and nums[j] == 0: j += 1
            ar.append(j-i-1)
            i = j
        else: i += 1

    if not ar:
        print(*([0]*(n+1)))
        return
    # print(ar)

    ct, z = cnt(nums), sum(ar)
    ans = [ct]

    l, r = 0, len(ar)-1
    while r >= 0 and ar[r] == 0: r -= 1

    for e in s:
        if r < l:
            ans.append(0)
            continue
        if e == '1':
            ct -= z
            z -= ar[l]
            l += 1
        else:
            ct -= r-l+1
            ar[r] -= 1
            z -= 1
            while r >= 0 and ar[r] == 0: r -= 1

        ans.append(ct)


    print(*ans)



for _ in range(int(input())): solve()

