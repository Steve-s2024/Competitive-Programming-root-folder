# will never forget this contest! hacked my e and f just because anti-hash testcases. miserable (i have replaced hashing in both
# problem with appropriate array logic, now they both pass all testcases
def solve():
    n, ax, ay, bx, by = [int(e) for e in input().split()]
    X = [int(e) for e in input().split()]
    Y = [int(e) for e in input().split()]
    ar = [(X[i], Y[i]) for i in range(n)]
    ar.sort()
    mp = [[ar[0][0], ar[0][1], ar[0][1]]]

    for i in range(1, n):
        x, y = ar[i]
        if x != ar[i-1][0]: mp.append([x, y, y])
        else:
            mp[-1][1] = min(mp[-1][1], y)
            mp[-1][2] = max(mp[-1][2], y)
    # print(mp)
    AR = sorted(mp[i][0] for i in range(len(mp)))
    dp = [[0, 0] for _ in range(len(AR))]
    dst = mp[-1][2] - mp[-1][1]
    cx, cy = AR[-1], mp[-1][2]
    dp[-1][0] = abs(cx-bx) + abs(cy-by) + dst
    cx, cy = AR[-1], mp[-1][1]
    dp[-1][1] = abs(cx-bx) + abs(cy-by) + dst

    for i in range(len(AR)-2, -1, -1):
        for f in range(2):
            cx, cy = AR[i], mp[i][(f+1)%2+1]
            dst = mp[i][2]-mp[i][1]

            nx, ny = AR[i+1], mp[i+1][1]
            a = dp[i+1][0] + abs(cx-nx) + abs(cy-ny)
            nx, ny = AR[i+1], mp[i+1][2]
            b = dp[i+1][1] + abs(cx-nx) + abs(cy-ny)
            dp[i][f] = min(a, b) + dst
    cx, cy = ax, ay
    nx, ny = AR[0], mp[0][1]
    a = dp[0][0] + abs(cx - nx) + abs(cy - ny)
    nx, ny = AR[0], mp[0][2]
    b = dp[0][1] + abs(cx - nx) + abs(cy - ny)
    print(min(a, b))


for _ in range(int(input())): solve()

# easier than E, still excited to solve 6 problem in div.3 (first time i think)
def solve():
    n, ax, ay, bx, by = [int(e) for e in input().split()]
    X = [int(e) for e in input().split()]
    Y = [int(e) for e in input().split()]
    ar = [(X[i], Y[i]) for i in range(n)]
    ar.sort()
    mp = {}
    for x, y in ar:
        if x not in mp: mp[x] = [y, y]
        else:
            mp[x][0] = min(mp[x][0], y)
            mp[x][1] = max(mp[x][1], y)

    AR = sorted(mp.keys())
    # print(mp)

    dp = [[0, 0] for _ in range(len(AR))]
    dst = mp[AR[-1]][1] - mp[AR[-1]][0]
    cx, cy = AR[-1], mp[AR[-1]][1]
    dp[-1][0] = abs(cx-bx) + abs(cy-by) + dst
    cx, cy = AR[-1], mp[AR[-1]][0]
    dp[-1][1] = abs(cx-bx) + abs(cy-by) + dst

    for i in range(len(AR)-2, -1, -1):
        for f in range(2):
            cx, cy = AR[i], mp[AR[i]][(f+1)%2]
            dst = mp[AR[i]][1]-mp[AR[i]][0]

            nx, ny = AR[i+1], mp[AR[i+1]][0]
            a = dp[i+1][0] + abs(cx-nx) + abs(cy-ny)
            nx, ny = AR[i+1], mp[AR[i+1]][1]
            b = dp[i+1][1] + abs(cx-nx) + abs(cy-ny)
            # print('?', a, b)
            dp[i][f] = min(a, b) + dst
    # print(dp)
    cx, cy = ax, ay
    nx, ny = AR[0], mp[AR[0]][0]
    a = dp[0][0] + abs(cx - nx) + abs(cy - ny)
    nx, ny = AR[0], mp[AR[0]][1]
    b = dp[0][1] + abs(cx - nx) + abs(cy - ny)
    print(min(a, b))

    # @cache
    # def fn(i, f):
    #     nonlocal bx, by
    #     cx, cy = AR[i], mp[AR[i]][(f+1)%2]
    #     dst = mp[AR[i]][1]-mp[AR[i]][0]
    #     if i >= len(AR)-1: return abs(cx-bx) + abs(cy-by) + dst
    #     nx, ny = AR[i+1], mp[AR[i+1]][0]
    #     a = fn(i+1, 0) + abs(cx-nx) + abs(cy-ny)
    #
    #     nx, ny = AR[i+1], mp[AR[i+1]][1]
    #     b = fn(i+1, 1) + abs(cx-nx) + abs(cy-ny)
    #     return min(a, b) + dst
    #
    # cx, cy = ax, ay
    # nx, ny = AR[0], mp[AR[0]][0]
    # a = fn(0, 0) + abs(cx - nx) + abs(cy - ny)
    # nx, ny = AR[0], mp[AR[0]][1]
    # b = fn(0, 1) + abs(cx - nx) + abs(cy - ny)
    # print(min(a, b))

for _ in range(int(input())): solve()