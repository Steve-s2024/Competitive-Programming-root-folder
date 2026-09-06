#
def solve():
    t = input()
    n = int(input())
    S = [input() for _ in range(n)]
    mp = [[0, -1] for _ in range(len(t))]
    for i in range(len(t)):
        x, c = 0, -1
        for j, s in enumerate(S):
            k = 0
            while k < min(len(s), len(t)-i) and s[k] == t[i+k]: k += 1
            if k == len(s):
                if k > x: x, c = k, j
        mp[i] = [x, c]
    # print(mp)
    i, j = 1, mp[0][0]
    res = [(0, mp[0][1])]
    while j < len(t):
        o = i
        x, c = 0, -1
        while i <= j and i < len(t):
            if mp[i][0] and i+mp[i][0] > x: o, x, c = i, mp[i][0]+i, mp[i][1]
            i += 1
        if not x:
            print(-1)
            return
        res.append((o, c))
        j = x

    print(len(res))
    # print(res)
    # print(mp)
    for a, b in res: print(b+1, a+1)





for _ in range(int(input())): solve()






