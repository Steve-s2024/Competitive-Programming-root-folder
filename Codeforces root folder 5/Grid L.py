# pure guessing conclusion and some heuristics

def solve():
    p, q = [int(e) for e in input().split()]
    t = 2 * q + p
    mx = max(p, q)
    for n in range(int(sqrt(mx)) + 5000):
        l, r = 1, mx
        while l <= r:
            m = (l + r) // 2
            x = 2 * n * m + n + m
            if x == t and abs(n - m) <= p:
                print(n, m)
                return
            elif x < t:
                l = m + 1
            else:
                r = m - 1

    print(-1)


for _ in range(int(input())): solve()
