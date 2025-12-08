# a paradigm problem of solving by forcing/contradicting all answer except one. which is very common approach
# among the 1700s
# for each position we solve all the position to its right and forcing the current position to only able to
# take on one value. if followed proper logic and made non-trivial observation, this should be
# the solution come to mind and easiest to implement (one similar question I solved before is the
# LeetCode Jump Game X, which I definitely used a much more complicated algorithm and tricky to
# implement)

def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    pre, suf = [0]*n, [0]*n
    mx, mi = nums[0], nums[-1]
    for i in range(n):
        mx = max(nums[i], mx)
        pre[i] = mx
    for i in range(n-1, -1, -1):
        mi = min(nums[i], mi)
        suf[i] = mi

    arr = [0]*n
    i = n-1
    j = n
    while i >= 0:
        mx = pre[i]
        while i >= 0 and pre[i] == mx: i -= 1
        for k in range(j-1, i, -1):
            arr[k] = mx if j == n or suf[j] >= pre[i+1] else arr[j]
        j = i+1

    # print(arr)

    print(' '.join(str(e) for e in arr))
