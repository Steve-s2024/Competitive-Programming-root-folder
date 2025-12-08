# this 1600 is actually brain-dead question, should be 1200~1300


def solve():
    n, m, k = [int(e) for e in input().split()]
    if abs(n-m) > k or max(n, m) < k:
        print(-1)
        return

    strarr = []
    if n >= m:
        strarr.append('0'*k)
        n -= k
        mi = min(n, m)
        strarr.append('10'*mi)
        n -= mi
        m -= mi
        strarr.append('0'*n)
        strarr.append('1'*m)

    else:
        strarr.append('1'*k)
        m -= k
        mi = min(n, m)
        strarr.append('01'*mi)
        n -= mi
        m -= mi
        strarr.append('0'*n)
        strarr.append('1'*m)

    print(''.join(strarr))

t = int(input())
for i in range(t):
    solve()