# it is true that understand the problem is harder than getting the answer
# this is by no mean 1400 rated, this is easy.

def solve():
    n, k = [int(e) for e in input().split()]
    bonus = [int(e) for e in input().split()]
    goals = [int(e) for e in input().split()]

    caps = [bonus[i]//goals[i] for i in range(n)] # the i-th engineer will never work more than caps[i] unit
    tot = sum(caps)
    if tot < k:
        print(' '.join(['0']*n))
    else:
        res = []
        for i in range(n):
            tot -= caps[i]
            cur = max(0, k-tot)
            k -= cur
            res.append(cur)

        print(' '.join([str(e) for e in res]))




# t = int(input())
t = 1
for i in range(t):
    solve()