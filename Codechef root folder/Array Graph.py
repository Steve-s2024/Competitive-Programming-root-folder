# 2026-02-18 D, the description throws smoke try to trick participant into thinking that -1 (invalid) case exists, but it does not


def solve():
    n = int(input())
    nums = [int(e) - 1 for e in input().split()]
    mp = [0] * n
    for v in nums: mp[v] += 1

    ar = list(enumerate(mp))
    ar.sort(key=lambda i: i[1], reverse=True)

    res = []
    if ar[0][1] > 1:
        j = 0
    else:
        j = 1

    for k, v in ar:
        for _ in range(v):
            res.append((k, ar[j % n][0]))
            j += 1

    # print(res)
    ans = [-1] * n
    for u, v in res: ans[v] = u
    print(' '.join(str(e + 1) for e in ans))


for _ in range(int(input())): solve()