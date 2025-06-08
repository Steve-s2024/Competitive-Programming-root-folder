# amazing question, at first it appears very hard and I have tried
# a few with no progress, but then this an eureka moment where
# I just realize the unordered characteristic of the columns, and
# the greedy solution is clear


def solve():
    n = int(input())
    row1 = [int(e) for e in input().split()]
    row2 = [int(e) for e in input().split()]
    res = 0
    leftOver = []
    for i in range(n):
        a, b = row1[i], row2[i]
        if a > b:
            res += a
            leftOver.append(b)
        else:
            res += b
            leftOver.append(a)
    res += max(leftOver)
    print(res)


t = int(input())

for tt in range(t):
    solve()