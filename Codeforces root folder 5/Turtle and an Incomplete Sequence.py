# kindda hellish implementation


def solve():
    n = int(input())
    nums = [int(e) for e in input().split()]
    ans = [-1]*n
    ar = []
    for i in range(n):
        if nums[i] != -1: ar.append((nums[i], i))

    for i in range(1, len(ar)):
        v1, i1 = ar[i-1]
        v2, i2 = ar[i]
        l = abs(i1-i2)+1
        if v1 == v2:
            tp = [v1]
            f = 0
            while len(tp) < l:
                if not f: tp.append(v1*2)
                else: tp.append(v1)
                f ^= 1

        else:
            if v1 > v2: v2, i2, v1, i1 = v1, i1, v2, i2

            cp2 = v2
            ar1, ar2 = [], []
            while v1 != v2:
                if v2 > v1:
                    ar2.append(v2)
                    v2 >>= 1
                else:
                    ar1.append(v1)
                    v1 >>= 1

            tp = ar1 + [v1] + ar2[::-1]


            f = 0
            while len(tp) < l:
                if not f: tp.append(cp2*2)
                else: tp.append(cp2)
                f ^= 1

            if i1 > i2: tp = tp[::-1]

        if len(tp) != l:
            print(-1)
            return
        mi = min(i1, i2)
        for j in range(mi, max(i1, i2)+1): ans[j] = tp[j-mi]



    if not ar:
        print(' '.join(['1' if i%2 else '2' for i in range(n)]))
        return

    f = 0
    v, i = ar[0]
    while i>=0:
        if f: ans[i] = v*2
        else: ans[i] = v
        i -= 1
        f ^= 1

    v, i = ar[-1]
    f = 0
    while i < n:
        if f: ans[i] = v*2
        else: ans[i] = v
        i += 1
        f ^= 1

    for i in range(n):
        if ans[i] != nums[i] and nums[i] != -1:
            print(-1)
            return
    for i in range(1, n):
        if ans[i-1] not in [ans[i]//2, ans[i]*2, ans[i]*2+1]:
            print(-1)
            return


    print(' '.join(str(e) for e in ans))

for _ in range(int(input())): solve()
