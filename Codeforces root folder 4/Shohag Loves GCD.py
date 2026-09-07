# I Loves THIS PROBLEM





def solve():
    n, m = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]

    vs = [m]*n
    res = [0]*n
    for i in range(n):
        idx = vs[i]-1
        if idx < 0:
            print(-1)
            return
        res[i] = nums[idx]

        for j in range(i+i+1, n, i+1):
            if vs[j] == idx+1: vs[j] = idx
    # print(vs)

    print(' '.join(str(e) for e in res))


for _ in range(int(input())): solve()