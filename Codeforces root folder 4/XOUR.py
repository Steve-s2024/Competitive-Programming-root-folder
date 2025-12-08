# not bad sorting problem, the key is to recognize that if relation a R b being a xor b < 4 is transitive
# so we can always sort the element in the same group since every pair would be following the relation (a complete
# graph type of relation)

def solve():
    n, ns = int(input()), [int(e) for e in input().split()]
    mp = defaultdict(list)
    for i, v in enumerate(ns):
        a, b, c, d = v, v^1, v^2, v^3
        key = min((a, b, c, d))
        mp[key].append((v, i))


    ans = [0]*n
    for val in mp.values():
        m = len(val)
        a, b = [val[i][0] for i in range(m)], [val[i][1] for i in range(m)]
        a.sort()
        for i in range(m): ans[b[i]] = a[i]

    print(' '.join(str(e) for e in ans))


for _ in range(int(input())): solve()