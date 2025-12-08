# feels so easy... although I only gambled with the approach and not proving anything.
# anyway without proving the solution, still the difficulty is 1600, so I guess I shouldn't feel bad about that

def solve():
    n, m = [int(e) for e in input().split()]
    a, b = [], []
    for i in range(n):
        a.append([int(e) for e in input().split()])
    for i in range(n):
        b.append([int(e) for e in input().split()])

    col, row = {}, {}
    for i in range(n):
        mi = min(a[i])
        row[mi] = set()
        for j in range(m): row[mi].add(a[i][j])

    for j in range(m):
        mi = a[0][j]
        for i in range(n): mi = min(mi, a[i][j])
        col[mi] = set()
        for i in range(n): col[mi].add(a[i][j])

    for i in range(n):
        mi = min(b[i])
        for j in range(m):
            if mi not in row or b[i][j] not in row[mi]:
                print('no')
                return


    for j in range(m):
        mi = b[0][j]
        for i in range(n): mi = min(mi, b[i][j])
        for i in range(n):
            if mi not in col or b[i][j] not in col[mi]:
                print('no')
                return

    print('yes')


t = int(input())
for i in range(t): solve()