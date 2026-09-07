# so boring... I am 90% confident that the solution is somehow gonna fail right before submit (because it is so brainless and tedious, not how a constructive problem shuold be)
# but it passed (first go)...
# did not learn anything wasting all that time, did learned the fact that "how stupid can codeforces problem be"


def helper(g: List[List[int]]) -> None:
    for r in g:
        ar = ['R' if e else 'B' for e in r]
        print(' '.join(ar))

def solve():
    n, m, k = [int(x) for x in input().split()]
    if k < n+m-2:
        print('No')
        return


    if (k-(n+m-2))%2:
        print('No')
        return

    print('Yes')

    ref = [
        [0, 1],
        [0, 1],
        [0, 1]
    ]
    g = [[0]*(m-1) for _ in range(n)]
    for i in range(3):
        for j in range(2): g[i][j] = ref[i][j]

    x = 0
    for j in range(2, m-1):
        g[2][j] = x
        x ^= 1


    helper(g)

    ref = [
        [1, 1, 0],
        [1, 0, 1]
    ]
    g = [[0]*m for _ in range(n-1)]
    for i in range(2):
        for j in range(3): g[i][j] = ref[i][j]

    for i in range(2, n-1):
        g[i][-1] = x
        x ^= 1

    helper(g)

for _ in range(int(input())): solve()

