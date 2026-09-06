# this shouldn't be wrong in another thousand years...




def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    mx = max(nums)
    mi = min(30, m)
    ar = []
    for cut in range(1, mi+1):
        ans = 0
        x = 1
        while 1:
            res = 0
            for i in range(n):
                e = nums[i]
                if e//x <= 1<<cut: res += e//x
                else: res += (1<<cut)-1
            ans = max(ans, res)
            if x*(1<<cut) > mx: break
            x += 1
        ar.append(ans)

    sm = sum(nums)
    for _ in range(m-mi): ar.append(sm)
    print(' '.join(str(e) for e in ar))


for _ in range(int(input())): solve()
