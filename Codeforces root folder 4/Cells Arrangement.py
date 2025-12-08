# at the end, no fun doing the problem. I wasted so many times just to guess this answer without proving the key
# as why it works. but I am definitely forced to try out a lot of good but wrong approaches

def solve():
    n = int(input())
    ans = [[1, 1], [n, n]]
    if n > 2:
        ans.append([2, 1])
        r, c = n-1, n-1
        for _ in range(n-3):
            ans.append([r, c])
            r, c = r if r == c else r-1, c-1 if r == c else c

    for i in range(n): print(' '.join(str(e) for e in ans[i]))

t = int(input())
for i in range(t): solve()