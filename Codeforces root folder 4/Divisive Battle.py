# darn!~ im good
def fac(n):
    res = []
    for f in range(2, int(sqrt(n))+1):
        while n%f == 0:
            n//=f
            res.append(f)
    if n > 1: res.append(n)
    return res

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    for i in range(n-1):
        if nums[i] > nums[i+1]: break
    else:
        print('Bob')
        return

    mx = 1
    for i in range(n):
        # if nums[i] == 1: continue
        fs = fac(nums[i])
        # print(nums[i], fs)
        if not fs: fs = [1]
        mx = max(mx, fs[-1])
        if fs[0] < mx:
            print('Alice')
            return
    print('Bob')



for _ in range(int(input())): solve()