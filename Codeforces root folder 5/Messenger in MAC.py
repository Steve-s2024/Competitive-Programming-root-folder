# hard to get it straight haha but at least I've realized the subtle imperfection without much time


def solve():
    n, l = [int(e) for e in input().split()]
    ar = []
    for _ in range(n):
        a, b = [int(e) for e in input().split()]
        ar.append((a, b))

    if min(e[0] for e in ar) > l:
        print(0)
        return

    ar.sort(key = lambda i:i[1])

    ans = 1
    for i in range(n):
        hp = []
        sm = ar[i][0]
        for j in range(i+1, n):
            a, b = ar[j]
            if sm+a + b-ar[i][1] > l:
                if hp and -hp[0] > a:
                    sm += heappop(hp) + a
                    heappush(hp, -a)
                continue

            sm += a
            heappush(hp, -a)
            if sm+b-ar[i][1] <= l: ans = max(ans, len(hp)+1)

    print(ans)


for _ in range(int(input())): solve()