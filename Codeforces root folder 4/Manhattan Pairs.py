# holy shit 3 hours, I don't feel very exhausted and it was very productive, which is definitely a good sign
# this problem is ultra hard for me as I don't have the heuristic for solving the maximize part
# everything must be built from scratch (I started off with thinking how to maximize the manhattan distance of points
# on a line (1D), then realize a neat way to expend it to 2D using Pigeonhole Principle

# I still feel like this is so far the hardest problem to solve (not tedious, just hard). or you can say it can be solved
# by either insanely tedious but less brain-damaging code (what I did at the beginning but eventually give up, or by the
# way I did it here, which is not tedious but extremely hard to conceptualize

# the commented part under the code is what I used to visualize my solution of the second testcase, and it definitely helped
# me figure out what is wrong with the code initially and build confident as to my solution is working

# for me, it definitely deserves an 1800 or higher
def solve():
    n = int(input())
    ps = []
    for i in range(n):
        x, y = [int(e) for e in input().split()]
        ps.append((x, y, i))

    xs, ys = [e[0] for e in ps], [e[1] for e in ps]
    xs.sort(), ys.sort()
    xm, ym = xs[n//2], ys[n//2]
    fk, u = [], []
    ps.sort()
    for x, y, i in ps:
        if x <= xm and len(fk) < n//2: fk.append((y, i))
        else: u.append((y, i))
    # print(xm, ym)
    # print(ps)
    fk.sort()
    u.sort(reverse = True)
    # print(fk, u)
    while fk:
        _, i = fk.pop()
        _, j = u.pop()
        print(f'{i+1} {j+1}')



t = int(input())
for i in range(t): solve()


# arr = [['*']*10 for _ in range(10)]
# pts = [(-1, -1), (-1, 2), (-2, -2), (-2, 0), (0, 2), (2, -3), (-4, -4), (-4, -2), (0, 1), (-4, -2)]
# pts = [(e[0]+4, e[1]+4) for e in pts]
# ct = 0
# for x, y in pts:
#     arr[y][x] = str(ct)
#     ct += 1
#
# for i in range(10):
#     if arr[3][i] == '*': arr[3][i] = '-'
# for i in range(10):
#     if arr[i][3] == '*': arr[i][3] = '|'
#
# for r in arr: print(''.join(r))