# nice!
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    obs = []
    for i in range(n):
        obs.append(([int(e) for e in input().split()]))

    flag = True
    cnt = 0
    idxs = []
    for i in range(n):
        if nums[i] == -1:
            idxs.append(i)
        if nums[i] in [1, -1]:
            nums[i] = 1
            cnt += 1


        l, r = obs[i]
        if cnt < l:
            flag = False
            break
        while idxs and cnt > r:
            idx = idxs.pop()
            nums[idx] = 0
            cnt -= 1
        if not idxs and cnt > r:
            flag = False
            break
    # print(nums, flag)

    if flag:
        h = 0
        for i in range(n):
            l, r = obs[i]
            h += nums[i]
            if h not in range(l, r+1):
                flag = False
                break
        if flag:
            print(' '.join(str(e) for e in nums))
        else:
            print(-1)
    else:
        print(-1)




t = int(input())
for i in range(t):
    solve()





#
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    obs = []
    for i in range(n):
        obs.append(([int(e) for e in input().split()]))

    l, r = 0, 0
    flag = True
    for i in range(n):
        if nums[i] == 1:
            l, r = l+1, r+1
        if nums[i] == -1:
            l, r = l, r+1
        L, R = obs[i]
        l, r = max(l, L), min(r, R)
        if l > r:
            flag = False
            break

    # print('Yes' if flag else 'No')