# a though problem, but the solution is very concise

def solve():
    n = int(input())
    ar = [(1<<n)-1]
    vs = [0]*(1<<n)
    vs[-1] = 1
    x = 2
    m = 1<<n-1
    while x <= 1<<n:
        for i in range(x):
            t = i*m + m-1
            if vs[t]: continue
            vs[t] = 1
            ar.append(t)
        x <<= 1
        m >>= 1
    # print(ar)

    print(' '.join(str(e) for e in ar))

for _ in range(int(input())): solve()

