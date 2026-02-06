# I cannot believe what just happened! after stuck with C for an hour, I decide to give up and instead crack D, which
# has even less solve count. I just do an algorithm I didn't expect to work (because I don't fully understand my own
# code), but it worked in the first attempt! (I can't express how happen I am, confident regain!)
# btw, this is the second time ever I solved div2 D

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    ar = []
    for i in range(n):
        a, b, c = nums[i-1] if i else -inf, nums[i], nums[i+1] if i < n-1 else inf
        x = min(b-a, c-b)
        ar.append(x)

    # print(ar)
    mx = ar[0]
    prv = nums[0]
    res = 0
    for i in range(1, n):
        dst = nums[i]-prv
        MX = min(dst, ar[i])
        if nums[i]-MX < nums[i-1]+mx: # reachable to previous circle
            res += 1
            MI = nums[i] - (nums[i-1]+mx)
        else: MI = 0
        prv = nums[i] + MI
        mx = MX

    print(res)


for _ in range(int(input())): solve()