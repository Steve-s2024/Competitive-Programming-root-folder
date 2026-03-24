# div2 D 2026-02-23




def solve():
    n, k = [int(e) for e in input().split()]
    if k >= 2*n:
        print("NO")
        return


    x = k-n # where x guarantee < n
    if x < 0:
        print('NO')
        return

    res = []
    t = 1
    for i in range(x):
        res.append(t+1)
        res.append(t)
        t += 1
    if x:
        res.append(1)
        res.append(t)
        t += 1

    while len(res) < 2*n:
        res.append(t)
        res.append(t)
        t += 1
    if max(res) <= n:
        print('YES')
        print(' '.join(str(e) for e in res))
    else: print('NO')


for _ in range(int(input())): solve()