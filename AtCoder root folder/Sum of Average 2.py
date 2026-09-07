# man!!!!!!! this is just nuts I submitted 6 seconds before the end and shit it worked lmao
# this fking contest man I couldn't solve any for 88 minutes and was so desperate, who would think I can
# solve through C... after 80 minutes in contest these brilliant ideas just keep popping up in my mind lol

def ct(ar):
    res = 0
    for i in range(len(ar) - 1):
        res += (ar[i] + ar[i + 1]) // 2
    return res


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    odd, even = [], []
    for i in range(n):
        e = nums[i]
        if e%2: odd.append(e)
        else: even.append(e)

    if not odd:
        even.sort()
        even = [even.pop()] + even
        # print(*even)
        print(ct(even))
        return
    if not even:
        odd.sort()
        odd = [odd.pop()] + odd
        # print(*odd)
        print(ct(odd))
        return

    odd.sort()
    even.sort()

    def helper(ar1, ar2):
        n, m = len(ar1), len(ar2)
        ar = []
        i, j = 0, 0
        f = 0
        for _ in range(n+m):
            if j >= m or (not f and i < n):
                ar.append(ar1[i])
                i += 1
            else:
                ar.append(ar2[j])
                j += 1
            f ^= 1

        return ar

    cads = []
    res = helper([odd[-1]] + odd[:-1], even)
    cads.append(res)
    res2 = helper([even[-1]] + even[:-1], odd)
    cads.append(res2)

    if len(odd) >=2 :
        a = odd.pop()
        b = odd.pop()
        res = [a] + helper(odd, even) + [b]
        res2 = [a] + helper(even, odd) + [b]
        cads.append(res)
        cads.append(res2)
        odd.append(b)
        odd.append(a)


    if len(even) >= 2:
        a = even.pop()
        b = even.pop()
        res = [a] + helper(odd, even) + [b]
        res2 = [a] + helper(even, odd) + [b]
        cads.append(res)
        cads.append(res2)


    ans, mi = [], 1<<50
    for ar in cads:
        c = ct(ar)
        if c < mi: ans, mi = ar, c

    # print(*ans)
    print(mi)

for _ in range(int(input())): solve()
