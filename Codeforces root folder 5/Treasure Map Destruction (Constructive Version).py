# not so interesting E for a div3



def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    ar = [-1]*n
    j = 0
    for i in range(n):
        e = nums[i]
        if e == -1: continue
        j = max(j, i)
        while j < min(n, i+e):
            ar[j] = 0
            j += 1
    j = n-1
    for i in range(n-1, -1, -1):
        e = nums[i]
        if e == -1: continue
        j = min(j, i)
        while j > max(-1, i-e):
            ar[j] = 0
            j -= 1
    # print(ar)

    for i in range(n):
        if nums[i] == -1: continue
        e = nums[i]
        for j in [i-e, i+e]:
            if j in range(n) and ar[j] in [-1, 1]:
                ar[j] = 1
                break
        else:
            print(-1)
            return



    if 1 not in ar:
        if -1 in ar:
            ar[ar.index(-1)] = 1

        else:
            print(-1)
            return
    # print(ar)



    ans = [1<<50]*n
    j = -1
    for i in range(n):
        if ar[i]: j = i
        if j != -1: ans[i] = i-j

    j = n
    for i in range(n-1, -1 ,-1):
        if ar[i]: j = i
        if j != n: ans[i] = min(j-i, ans[i])

    # print(ans)

    for i in range(n):
        if ans[i] != nums[i] and nums[i] != -1:
            print(-1)
            return


    print(''.join(str(e if e != -1 else 0) for e in ar))



for _ in range(int(input())): solve()