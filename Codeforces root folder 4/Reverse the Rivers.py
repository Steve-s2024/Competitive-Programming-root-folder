# after thinking about the 'or' operation, it reminds me of logtrick, then I just realize the monotonicity of each column
# so applied binary search.

def solve():
    n, k, q = [int(e) for e in input().split()]
    grid = []
    for i in range(n): grid.append([int(e) for e in input().split()])
    for j in range(k):
        for i in range(1, n):
            grid[i][j] |= grid[i-1][j]

    for i in range(q):
        m = int(input())
        le, ri = 0, n-1
        for j in range(m):
            r, o, c = [e for e in input().split()]
            r, c = int(r)-1, int(c)
            x, y = 0, n-1
            res = -1 if o == '<' else n
            while x <= y:
                z = (x+y)//2
                if o == '<':
                    if grid[z][r] < c:
                        res = z
                        x = z+1
                    else: y = z-1
                else:
                    if grid[z][r] > c:
                        res = z
                        y = z-1
                    else: x = z+1
            if o == '<': ri = min(res, ri)
            else: le = max(res, le)
        # print(le, ri)
        if ri >= le: print(le+1)
        else: print(-1)


solve()