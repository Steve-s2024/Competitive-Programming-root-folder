# solved it before, but good to solve it again



# ar = [998244353, 1000000000, 314159265, 676767677, 999999999, 987654321]
# cp = [998244353, 1000000000, 314159265, 676767677, 999999999, 987654321]
# for i, j in ((5, 2), (4, 3), (6, 4), (1, 6), (2, 1)):
#     i, j = i-1, j-1
#     print(ar[i], ar[j])
#     ar[i] -= cp[j]
#     ar[j] -= cp[i]
# print(ar)


def solve():
    n, m = [int(x) for x in input().split()]
    nums = [int(x) for x in input().split()]
    nums = [(x, i) for i, x in enumerate(nums)]
    nums.sort()

    if m == 0:
        sm = 0
        ar = []
        # print(nums)
        for i in range(n-2, -1, -1):
            sm += nums[i][0]

            if sm >= nums[-1][0]:
                for j in range(i):
                    ar.append((j+1, j))
                ar.append((n-1, i))
                print(len(ar))
                for x, y in ar: print(nums[x][1]+1, nums[y][1]+1)
                return
            ar.append((i, n-1))

        print(-1)
        return


    if 2*m > n:
        print(-1)
        return

    ar = []
    for i in range(m-1):
        ar.append((n-i-1, i))

    for i in range(m-1, n-m):
        ar.append((i+1, i))

    # print(ar)
    print(len(ar))
    for i, j in ar:
        print(nums[i][1]+1, nums[j][1]+1)






for _ in range(int(input())): solve()