# it should work, don't know what's wrong

from collections import defaultdict, deque, Counter
import cmath, heapq

def recursive(size, k, MOD, extra):
    res = 0
    if k <= size:
        comb = 1
        # pick k-1 spot in size-1 spots
        i = 1
        j = size - 1
        while i <= k - 1:
            # print(j, i)
            comb *= j
            comb //= i
            i += 1
            j -= 1
        tot = ((1 << size) - 1)
        res += comb * tot
        res += comb * size * extra
        res %= MOD
    return res

def solve():
    n, k = [int(e) for e in input().split()]
    MOD = 998244353

    s = str(bin(n))[2:]
    res = recursive(len(s)-1, k, MOD, 0) if k <= len(s)-1 else 0
    idxs = []
    for i in range(len(s)):
        if s[i] == '1':
            idxs.append(i)

    # print(res)
    cnt = 0
    tot = 0
    for i in range(1, len(idxs)):
        a, b = idxs[i-1], idxs[i]
        cnt += 1
        tot += 1<<(len(s)-a-1)
        res += recursive(len(s)-1-b, k-cnt, MOD, tot)
    if Counter(s)['1'] == k:
        res += n
    print(res % MOD)


t = int(input())
for i in range(t):
    solve()

