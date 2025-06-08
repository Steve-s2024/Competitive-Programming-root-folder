# trolling question?? rated 1300 but not even 800, got me worried for a sec fr.
def solve():
    arr = [int(e) for e in input().split()]
    [a, b, c, d] = arr
    for i in range(1, 6):
        if i not in arr:
            print(i)
            break


# t = int(input())
t = 1
for tt in range(t):
    solve()
