# from this question I learn that sum(1, 1/2, 1/3... 1/n) is less than logn (pretty crazy statement since we now know)
# algorithm of the form below actually work in > logn time, this is called the harmonic series
#   for i in range(n):
#         for j in range(0, n, i+1):
#             ...


# solution following the hint and editorial, cleaner than the old code, and this one is functioning
def solve():
    n, m = [int(e) for e in input().split()]
    par = [int(e) for e in input().split()]
    dif = [int(e) for e in input().split()]
    kevin = par[0]
    tmp = []
    for num in par:
        if num > kevin: tmp.append(num)
    par = tmp
    par.sort()
    dif.sort()

    arr = []
    for num in dif:
        if num <= kevin:
            arr.append(1)
            continue
        l, r = 0, len(par)-1
        res = len(par)
        while l <= r:
            mid = (l+r)//2
            if par[mid] >= num:
                res = mid
                r = mid-1
            else: l = mid+1
        rank = len(par)-res + 1
        arr.append(rank)

    arr.sort()
    # print(arr)
    ans = []
    for k in range(1, m+1):
        sm = 0
        for i in range(k-1, m, k):
            sm += arr[i]
        ans.append(sm)
    print(' '.join(str(e) for e in ans))


t = int(input())
for i in range(t): solve()



# the solution is under development
def solve():
    n, m = [int(e) for e in input().split()]
    par = [int(e) for e in input().split()]
    dif = [int(e) for e in input().split()]
    kevin = par[0]
    tmp = []
    for num in par:
        if num > kevin: tmp.append(num)
    par = tmp
    par.sort()
    dif.sort()

    mp = {}
    idx = 0
    for num in dif:
        if num <= kevin:
            mp[num] = 1
            idx += 1
            continue
        l, r = 0, len(par)-1
        res = len(par)
        while l <= r:
            mid = (l+r)//2
            if par[mid] >= num:
                res = mid
                r = mid-1
            else: l = mid+1
        rank = len(par)-res + 1
        mp[num] = rank

    # print(mp)
    ans = []
    for k in range(1, m+1):
        res = 0
        re = m%k
        # skip all the questions that are in dif[idx:idx+re]
        i = 0
        # print(f'k = {k}', idx)
        while i < m:
            if re and i <= idx+re-1 and i+k-1 >= idx: # the current contest include problem that suppose to be skipped
                if idx+re >= m: break
                res += mp[dif[idx+re]]
                i += re + k
            elif not re and i+k-1 >= idx > i: # the current include both easy and hard problems
                res += mp[dif[idx]]
                i += k
            else: # all easy problems in the contest
                res += mp[dif[i]]
                i += k
        # print(res)
        ans.append(res)
    print(' '.join(str(e) for e in ans))

t = int(input())
for i in range(t): solve()






