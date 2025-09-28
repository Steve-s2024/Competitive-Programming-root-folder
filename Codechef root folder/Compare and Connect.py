# got me worried about for a sec, but it's a funny Q4

def solve():
    n, m = [int(e) for e in input().split()]
    if n and m:
        strarr = ['<<']*n + ['><']*(m-1) + ['>']
    elif n:
        strarr = ['<<']*(n-2) + ['<=<']
    else:
        strarr = ['><']*(m-2) + ['>=>']

    print(''.join(strarr))





t = int(input())
for i in range(t):
    solve()

