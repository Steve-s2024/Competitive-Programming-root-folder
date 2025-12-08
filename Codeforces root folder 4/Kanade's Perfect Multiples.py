# minheap question

def solve():
    n, k = [int(e) for e in input().split()]
    ar = [int(e) for e in input().split()]
    ar = list(set(ar))
    n = len(ar)
    ar.sort()
    hp = []
    res = []
    for i in range(n):
        x = ar[i]
        if hp and x == hp[0][0]:
            while hp and x == hp[0][0]:
                _, a, b = heappop(hp)
                if a*(b+1) <= k: heappush(hp, (a*(b+1), a, b+1))
        else:
            res.append(x)
            if x*2 <= k: heappush(hp, (x*2, x, 2))
        # print(hp)


    if hp: print(-1)
    else:
        print(len(res))
        print(' '.join(str(e) for e in res))

for _ in range(int(input())): solve()