# row/col cyclic shift no matrix is a new field for me. took some time to realize that they are not as powerful as I thought
def solve():
    input()
    n = int(input())
    g = []
    for _ in range(n): g.append([int(e) for e in input()])
    ar = [sum(e) for e in g]

    ans = 1<<30
    for i in range(n):
        x = 0
        for j in range(n):
            if g[j][(i+j)%n] == 1: x += ar[j]-1
            else: x += ar[j]+1
        ans = min(ans, x)

    print(ans)



for _ in range(int(input())): solve()