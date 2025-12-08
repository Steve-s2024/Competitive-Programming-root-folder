# quite subtle of the solution, need to think extremely piercing, the observation is tough to get but once you see
# it you feel like it should be pretty basic observation...

def solve():
    x, n, m = [int(e) for e in input().split()]
    l = x.bit_length()
    if n >= l or x == 0: mi, mx = 0, 0
    elif n+m > l and n: mi, mx = 0, 1
    elif m > l: mi, mx = 1, 1
    else:
        a, b = x, x
        for i in range(n): a //= 2
        for j in range(m):
            a += a%2
            a //= 2

        for j in range(m):
            b += b%2
            b //= 2
        for i in range(n): b //= 2
        mi, mx = b, a
    print(mi, mx)


t = int(input())
for i in range(t):
    solve()



def solve():
    x, n, m = [int(e) for e in input().split()]

    l = x.bit_length()
    n = min(n, l)
    m = min(m, l)
    @cache
    def recursive(x, n, m):
        if n == m == 0: return x
        res = inf
        if n: res = min(res, recursive(x//2, n-1, m))
        if m: res = min(res, recursive((x+1)//2, n, m-1))
        return res

    @cache
    def mx(x, n, m):
        if n == m == 0: return x
        res = -inf
        if n: res = max(res, mx(x//2, n-1, m))
        if m: res = max(res, mx((x+1)//2, n, m-1))
        return res

    a = recursive(x, n, m)
    b = mx(x, n, m)
    print(str(a) + ' ' + str(b))
t = int(input())
for i in range(t):
    solve()