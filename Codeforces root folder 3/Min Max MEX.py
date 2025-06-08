# testing the non-set solution, avoid the huge constant in set operation
# only took half of the time and memory.
def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    res = 0
    l, r = 0, n
    while l <= r:
        m = (l+r)//2
        arr = [0] * m
        mex = 0
        cnt = 0
        for i in range(n):
            if nums[i] < m:
                arr[nums[i]] = 1
            while mex < m and arr[mex] == 1:
                mex += 1

            if mex == m:
                while mex > 0:
                    mex -= 1
                    arr[mex] = 0
                cnt += 1

        if cnt >= k:
            res = m
            l = m+1
        else:
            r = m-1
    print(res)


t = int(input())
for i in range(t):
    solve()




# classic binary search and greedy solution, almost TLE
def solve():
    n, k = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    res = 0
    l, r = 0, n
    while l <= r:
        m = (l+r)//2
        st = set(i for i in range(m))
        cnt = 0
        for i in range(n):
            if nums[i] in st:
                st.remove(nums[i])
            if len(st) == 0:
                st = set(i for i in range(m))
                cnt += 1

        if cnt >= k:
            res = m
            l = m+1
        else:
            r = m-1
    print(res)


t = int(input())
for i in range(t):
    solve()
