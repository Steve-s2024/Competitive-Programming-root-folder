# damn! damn

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    ar = [(v+i+1, v+1) for i, v in enumerate(nums)]

    ar.sort()
    hp = []
    res = []

    i = n-1
    x = ar[i][0]
    while i >= 0 and ar[i][0] >= x:
        heappush(hp, -ar[i][1])
        i -= 1

    while i >= 0 or hp:
        while hp:
            lw = -heappop(hp)
            if lw <= x:
                res.append(x)
                x -= 1
                while i >= 0 and ar[i][0] >= x:
                    heappush(hp, -ar[i][1])
                    i -= 1
        if i >= 0:
            x = ar[i][0]
            while i >= 0 and ar[i][0] >= x:
                heappush(hp, -ar[i][1])
                i -= 1
    # print(res)
    print(' '.join(map(str, res)))


for _ in range(int(input())): solve()