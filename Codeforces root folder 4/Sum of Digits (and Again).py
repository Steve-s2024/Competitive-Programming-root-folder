# a pretty funny question, how the brute force solution is constructed is even funnier
# 2026-03-16 div2 E


def solve():
    s = input()
    if len(s) == 1:
        print(s)
        return

    ar = [int(e) for e in s]
    mp = [0]*10
    for e in ar: mp[e] += 1
    sm = sum(ar)
    for i in range(1, sm+1):
        tsm = sm
        x = i
        ls = [int(e) for e in list(str(x))]
        res = []
        tmp = [0] * 10
        while 1:
            for v in ls:
                tmp[v] += 1
                tsm -= v
            res.append(x)

            if x < 10: break
            x = sum(ls)
            ls = [int(e) for e in list(str(x))]

        for j in range(10):
            if mp[j] < tmp[j]: break
        else:
            if tsm == i: # i is the number!
                ans = []
                for i in range(9, -1, -1): ans.append(str(i)*(mp[i]-tmp[i]))
                print(''.join(ans + [str(e) for e in res]))
                return



for _ in range(int(input())): solve()

