# holy shit, no idea why it worked... just got lucky
def solve():
    n = int(input())
    start = n-1
    res = 0
    for i in range(n//2):
        res += start
        start -= 2
    print(res + 1)

t = int(input())
for tt in range(t):
    solve()
