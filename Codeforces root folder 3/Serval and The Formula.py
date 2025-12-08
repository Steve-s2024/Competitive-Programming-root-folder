# 5 minute 1600 rated question. holy shit I dominate this shit
def solve():
    x, y = [int(e) for e in input().split()]
    if x == y:
        print(-1)
        return

    mx, mi = max(x, y), min(x, y)
    bg = 1<<32
    k = bg-mx
    print(k)

t = int(input())
for i in range(t):
    solve()