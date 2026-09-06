# okay turns out 5 minutes ago can't solve A, B  now with 30 minutes left I'm actually looking good lmo



def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    if max(nums) == 0:
        print(0)
        return


    for i in range(1, n):
        if nums[i-1]//2 < nums[i]:
            print(-1)
            return


    ans = 1

    for i in range(1, n):
        dif = nums[i-1] - 2*nums[i]
        ans = max(ans, dif)


    print(ans)


for _ in range(int(input())): solve()
