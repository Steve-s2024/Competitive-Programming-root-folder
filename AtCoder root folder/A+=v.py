# 2026-03-14 ABC, E
# one of the hardest problem solved in ABC
# passed 5 minutes before end

def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]

    mp = Counter(nums)
    for i in range(1, m+1):
        if i not in mp: mp[i] = 0
    ar = sorted(mp.items(), key = lambda i:(i[1], i[0]))

    q = int(input())
    ans = [0]*q

    qs = []
    for i in range(q): qs.append((int(input())-1, i))
    qs.sort()

    i = 0
    while i < q and qs[i][0] < n:
        x, j = qs[i]
        ans[j] = nums[x]
        i += 1

    sl = SortedList()
    j = 0
    while j < len(ar) and ar[j][1] == ar[0][1]:
        sl.add(ar[j][0])
        j += 1

    prv = n-1
    for x, idx in qs[i:]:
        dif = x-prv
        # print(dif, sl)

        if len(sl) < len(ar):
            # print(sl, j)
            fdif = ar[j][1] - ar[j-1][1]
            while fdif*len(sl) < dif:
                k = j
                dif -= fdif*len(sl)
                prv += fdif*len(sl)
                while k < len(ar) and ar[k][1] == ar[j][1]:
                    sl.add(ar[k][0])
                    k += 1
                j = k
                if j >= len(ar): break
                fdif = ar[j][1] - ar[j-1][1]

        ans[idx] = sl[(dif-1)%len(sl)]
        # print(sl)
    # print(ans)
    for e in ans:
        print(e)





solve()



