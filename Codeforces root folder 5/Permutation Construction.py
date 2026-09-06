# this is soooo guessing, man such a crapshoot haha

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    pre = [0]*n
    for i in range(n):
        pre[i] = pre[i-1] + nums[i]

    ar = sorted([(pre[i-1] if i else 0, i) for i in range(n)])

    P = [0]*n
    x = n
    for i in range(n):
        _, j = ar[i]
        P[j] = x

        x -= 1

    print(' '.join(str(e) for e in P))





for _ in range(int(input())): solve()

