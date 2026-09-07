# pretty easy, but with some pitfalls




def solve():
    n, c = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    ar = [((i+1)*c, nums[i]) for i in range(n)]

    sm, f = 0, 0
    tp = []
    for cst, v in ar[1:]:
        if ar[0][1]+v >= cst:
            sm += v
            f = 1
        else: tp.append((cst-v, v))

    if not f:
        print('No')
        return
    sm += ar[0][1]

    # print(tp)

    tp.sort()
    for cst, v in tp:
        # print(sm, cst)
        if sm < cst:
            print('No')
            return
        sm += v

    print('Yes')

for _ in range(int(input())): solve()

