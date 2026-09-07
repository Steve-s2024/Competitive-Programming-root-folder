# refresh on the old challenge


def solve():
    s = [int(e) for e in list(input())]

    if len(s) == 1:
        print(s[0])
        return

    sm = sum(s)
    frq = [0]*10
    for e in s: frq[e] += 1

    for i in range(1, sm+1):
        tp = [0]*10
        x = i
        ar = [x]
        while x >= 10:
            nx = 0
            while x:
                tp[x%10] += 1
                nx += x%10
                x //= 10
            x = nx
            ar.append(x)
        tp[x] += 1
        f = 1
        ofs = 0
        for j in range(10):
            ofs += tp[j]*j
            if tp[j] > frq[j]:
                f = 0
                break
        if not f: continue

        if sm-ofs == i: # bingo
            # print(i)
            ans = []
            for j in range(9, -1, -1):
                for _ in range(frq[j]-tp[j]): ans.append(j)
            ans += ar
            print(''.join(str(e) for e in ans))
            break




for _ in range(int(input())): solve()