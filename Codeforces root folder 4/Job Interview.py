# conclusion after 2 hours, very boring problem. did I overcomplicate things again?

def solve():
    n, m = [int(e) for e in input().split()]
    arr = [int(e) for e in input().split()]
    brr = [int(e) for e in input().split()]
    size = n + m + 1
    a, b = [size if n else -1, size if n else -1], [size if m else -1, size if m else -1]
    ct1, ct2 = 0, 0
    for i in range(size):
        if arr[i] > brr[i]: ct1 += 1
        else: ct2 += 1
        if ct1 == n: a[0] = min(a[0], i)
        if ct2 == m: b[0] = min(b[0], i)
        if ct1 == n + 1: a[1] = min(a[1], i)
        if ct2 == m + 1: b[1] = min(b[1], i)

    mxsm = []
    sm = 0
    for i in range(size):
        sm += max(arr[i], brr[i])
        mxsm.append(sm)

    psm, tsm = [0] * size, [0] * size
    x, y = 0, 0
    for i in range(size - 1, -1, -1):
        x += arr[i]
        y += brr[i]
        psm[i] = x
        tsm[i] = y
    # print(mxsm, psm, tsm)
    def helper(i):
        if arr[i] < brr[i]: res1 = a[0] # tester is excluded
        elif i <= a[0]: res1 = a[1]
        else: res1 = a[0]

        if arr[i] > brr[i]: res2 = b[0] # programmer is excluded
        elif i <= b[0]: res2 = b[1]
        else: res2 = b[0]

        return min(res1, res2), 1 if res1 < res2 else 2


    ans = []
    for i in range(size):
        idx, f = helper(i)
        # print(i, idx, f)
        res = mxsm[idx] if idx != -1 else 0
        if idx < size-1: res += psm[idx+1] if f == 2 else tsm[idx+1]
        if i < idx: res -= max(arr[i], brr[i])
        else: res -= arr[i] if f == 2 else brr[i]
        ans.append(res)
    print(' '.join(str(e) for e in ans))


t = int(input())
for i in range(t): solve()