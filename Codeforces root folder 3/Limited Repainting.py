# hard to think of binary search greedy question
def solve():
    n, k = [int(e) for e in input().split()]
    s = input()
    nums = [int(e) for e in input().split()]
    tmp = sorted(nums)
    tmp.insert(0, 0)

    l, r = 0, n
    res = 0
    while l <= r:
        m = (l+r)//2
        tar = tmp[m]
        paintCnt = 0
        prev = -1
        L, R = 0, 0
        for i in range(n):
            if s[i] == 'R' and nums[i] > tar:
                L = R = i+1
            else:
                if s[i] == 'B' and nums[i] > tar:
                    #paint the spot
                    if prev not in range(L, R):
                        paintCnt+=1
                        prev = i
                R+=1

        if paintCnt > k:
            l = m+1
        else:
            res = tmp[m]
            r = m-1
    print(res)



t = int(input())
for i in range(t):
    solve()