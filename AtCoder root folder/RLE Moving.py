# for the first time dealing with stupid collision detection, I did a jelly good job I'd say.

mp = {'U': (-1, 0), 'R': (0, 1), 'D': (1, 0), 'L': (0, -1)}

def getOverlap(r1, c1, r2, c2, d1, d2, dst):
    if r1 == r2 and c1 == c2: return dst if d1 == d2 else 0

    a, b = abs(r1 - r2), abs(c1 - c2)
    if (
        a == b and (r1 + mp[d1][0] * a, c1 + mp[d1][1] * a) == (r2 + mp[d2][0] * a, c2 + mp[d2][1] * a) and a <= dst or
        d1 in 'UD' and d2 in 'UD' and (r1 + mp[d1][0] * (a//2), c1 + mp[d1][1] * (a//2)) == (r2 + mp[d2][0] * (a//2), c2 + mp[d2][1] * (a//2)) and (a//2) <= dst or
        d1 in 'LR' and d2 in 'LR' and (r1 + mp[d1][0] * (b//2), c1 + mp[d1][1] * (b//2)) == (r2 + mp[d2][0] * (b//2), c2 + mp[d2][1] * (b//2)) and (b//2) <= dst
    ):
        return 1

    return 0

def solve():
    rt, ct, ra, ca = [int(e) for e in input().split()]
    n, m, l = [int(e) for e in input().split()]
    srr = []
    trr = []
    for i in range(m):
        srr.append([e for e in input().split()])
        srr[i][1] = int(srr[i][1])
    for i in range(l):
        trr.append([e for e in input().split()])
        trr[i][1] = int(trr[i][1])

    res = 0
    i1, i2 = 0, 0
    while  i1 < m and i2 < l:
        mi = min(srr[i1][1], trr[i2][1])
        # print(rt, ct, ra, ca, srr[i1][0], trr[i2][0], mi)
        res += getOverlap(rt, ct, ra, ca, srr[i1][0], trr[i2][0], mi)
        # print(getOverlap(rt, ct, ra, ca, srr[i1][0], trr[i2][0], mi))

        rt += mp[srr[i1][0]][0]*mi
        ct += mp[srr[i1][0]][1]*mi
        ra += mp[trr[i2][0]][0]*mi
        ca += mp[trr[i2][0]][1]*mi
        srr[i1][1] -= mi
        trr[i2][1] -= mi

        if srr[i1][1] == 0: i1 += 1
        if trr[i2][1] == 0: i2 += 1
    # print(rt, ct, ra, ca)

    print(res)




solve()