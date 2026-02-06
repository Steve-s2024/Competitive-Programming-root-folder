# 2026-02-01, an implementation from solving "Count Valid Paths in a Tree"
def sieve(n):
    if n < 1: return []
    P = [1] * (n + 1)
    P[0], P[1] = 0, 0
    for i in range(int(sqrt(n)) + 1):
        if P[i] == 0: continue
        for j in range(i * i, n + 1, i): P[j] = 0
    return P