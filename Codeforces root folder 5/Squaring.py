# squashed, wasn't that hard




def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]


    for i in range(1 ,n):
        if nums[i-1] > nums[i] and nums[i] == 1:
            print(-1)
            return

    prv = 0
    res = 0
    for i in range(1, n):
        x = 0
        if nums[i-1] >= nums[i]:
            t = nums[i]
            while nums[i-1] > t:
                t *= t
                x += 1
            x += prv
        else:
            t = nums[i-1]
            if t == 1: continue
            while nums[i] > t:
                t *= t
                x += 1
            if t == nums[i]: x = max(prv-x, 0)
            else: x = max(prv-x+1, 0)

        res += x
        prv = x

    print(res)


for _ in range(int(input())): solve()
