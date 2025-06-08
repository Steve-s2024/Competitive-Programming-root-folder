# pathetic, wasted 20 mins just because one line
# the h*w should be >= n instead of just > n
def solve():
    n = int(input())
    row, col = [], []
    mons = []
    for i in range(n):
        x, y = [int(e) for e in input().split()]
        mons.append((x, y))
        row.append(y)
        col.append(x)

    if n == 1:
        print(1)
    else:

        row.sort()
        col.sort()


        res = float('inf')
        for i in range(n):
            x, y = mons[i]
            l = col[0] if col[0] != x else col[1]
            r = col[-1] if col[-1] != x else col[-2]
            t = row[0] if row[0] != y else row[1]
            b = row[-1] if row[-1] != y else row[-2]
            w, h = r-l+1, b-t+1

            if h*w >= n:
                res = min(res, h*w)
            else:
                res = min(res, h*w + min(h, w))

        print(res)


t = int(input())
for i in range(t):
    solve()
