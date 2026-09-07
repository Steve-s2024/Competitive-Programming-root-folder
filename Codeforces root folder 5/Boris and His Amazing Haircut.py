# boring, move on to 1800 construct algo




def solve():
    n = int(input())
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]
    m = int(input())
    nums = [int(e) for e in input().split()]
    frq = Counter(nums)
    mp = defaultdict(list)
    for i in range(n):
        a, b = A[i], B[i]
        if a < b:
            print('No')
            return
        elif a > b: mp[b].append(i)

    mk = [n]*n
    stk = []
    for i in range(n):
        b = B[i]
        while stk and stk[-1][0] < b:
            mk[stk.pop()[1]] = i
        stk.append((b, i))


    for k in sorted(mp.keys()):
        ar = mp[k]
        x = 1
        for i in range(1, len(ar)):
            a, b = ar[i-1], ar[i]
            if mk[a] < b: x += 1

        if k not in frq or x > frq[k]:
            print('No')
            return

    print('Yes')





for _ in range(int(input())): solve()
