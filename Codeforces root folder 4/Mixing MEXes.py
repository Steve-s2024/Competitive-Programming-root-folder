# very close to a solution (in progress) div4. G
def solve():
    n = int(input())
    mat = []
    lsm = 0
    for _ in range(n):
        ar = [int(e) for e in input().split()]
        lsm += ar[0]
        mat.append(sorted(set(ar[1:])))

    # mex(aj) will contribute len(ai)*(n-2) for each ai != aj
    # mex(aj)'s total contribution (n-1)*(contri per ai)

    # contribution for each ai, where ai is added by one element
    # ai contribution = sum(mex(ai+[aj[k]])) for all j != i, k in range(len(aj))

    mp = defaultdict(int)
    for ar in mat:
        for v in ar: mp[v] += 1

    res = 0
    for ar in mat:
        mex = 0
        for i in range(len(ar)):
            if i != ar[i]:
                mex = i
                break

        res += mex * (n - 1) * (lsm - len(ar)) * (n - 2)
        x = mp[mex]
        res += x*(mex+1)
        res += mex*(lsm-x-len(ar))
    print(res)


for _ in range(int(input())): solve()