# hard Q2 in codechef contest definitely
def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]

    pre = [0]*n
    pre[0] = nums[0]
    for i in range(1, n): pre[i] = nums[i] + pre[i-1]
    suf = [0]*n
    suf[-1] = nums[-1]
    for i in range(n-2, -1, -1): suf[i] = nums[i] + suf[i+1]
    # print(pre, suf)

    i = n-1
    while i >= 0 and pre[i]%3 != 0: i -= 1
    i += 1
    if i == 0:
        print('Yes')
        return
    elif i == n:
        print('No')
        return


    st = set()
    sm = sum(nums[i:])
    for j in range(i):
        st.add(suf[j]%3)

    flag = False
    while i < n:
        sm -= nums[i]
        st.add(suf[i]%3)
        if sm%3 not in st:
            flag = True
            break
        i += 1

    if flag: print('Yes')
    else: print('No')



t = int(input())
for i in range(t):
    solve()