# the problem name is <<The 67th Iteration of "Counting is Fun">>, but quotation mark cannot be in the file name

# fking baby lets go! 2026/04/04
# first ever div.4 all kill, first ever solved G, first ever cf all kill
# rank 550/21000

def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    M = 676767677

    mp = [[] for _ in range(m)]
    for i in range(n): mp[nums[i]].append(i)


    sm, res = len(mp[0]), 1
    ar = [0]
    for i in range(1, m):
        ar.append(sm)

        for j in mp[i]:
            f = 0
            mi = i-1
            for v in [j-1, j+1]:
                if v in range(n) and nums[v] < i: f, mi = 1, min(mi, nums[v])

            if not f:
                print(0)
                return

            if i-mi == 1: # all acceptable
                res = (res*sm) % M
            else: # only last increment
                # no more than sm
                # no less than prv sm?
                res = (res*(sm-ar[-2])) % M
        sm += len(mp[i])
    print(res)

for _ in range(int(input())): solve()