# not an easy one, but Im gaining fast that this is not so hard


def solve():
    n = int(input())
    a, b = input(), input()

    if '1' not in a:
        if '1' in b: print(-1)
        else: print(0)
        return

    t, s = [0, 0], [0, 0]
    for i in range(n):
        if a[i] == b[i]: t[int(a[i])] += 1
        else: s[int(a[i])] += 1

    res = 1<<30
    if sum(t)%2 and t[0] in [t[1], t[1]-1]: res = sum(t)
    if sum(s)%2 == 0 and s[0] in [s[1], s[1]-1]: res = min(res, sum(s))
    if res == 1<<30: print(-1)
    else: print(res)

for _ in range(int(input())): solve()
