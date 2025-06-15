
def solve():
    n, q = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    for i in range(q):
        i, x = [int(e) for e in input().split()]
        nums[i-1] = x
        sm = sum(nums)
        incre = True
        i = 1
        while i < n:
            a, b = nums[i - 1], nums[i]
            if b - a > 0:
                incre = True
                l = i
            elif b - a < 0:
                if incre:
                    sm -= a
                    incre = False

            i += 1
        if incre:
            sm -= nums[-1]
        print(sm)



t = int(input())
for i in range(t):
    solve()