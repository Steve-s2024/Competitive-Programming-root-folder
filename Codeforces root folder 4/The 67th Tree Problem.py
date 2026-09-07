# after this div.4 F, I will be handling my first time G. also the first time ever reached last problem

def solve():
    x, y = [int(e) for e in input().split()]
    if x > y:
        print('NO')
        return

    if x == y:
        print('YES')
        for i in range(x+y-1): print(i+1, i+2)
        return
    else:
        if (x+y)%2: y -= 1
        else:
            if not x:
                print('NO')
                return
            x -= 1
        res = []
        i = 2
        for _ in range(x):
            res.append((1, i))
            res.append((i, i+1))
            i += 2
        while i <= x+y+1:
            res.append((1, i))
            i += 1
        print('YES')
        for u, v in res: print(u, v)