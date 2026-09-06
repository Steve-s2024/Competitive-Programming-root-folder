# pretty obvious clue but lot to think about while implementing

def solve():
    n, k = [int(e) for e in input().split()]
    s = input()

    if '1' not in s or '0' not in s:
        print(1 if n == k else -1)
        return
    ar = []
    j = 0
    for i in range(1, n):
        if s[i] != s[i-1]:
            ar.append((i-j, s[i-1]))
            j = i
    ar.append((n-j, s[-1]))

    # print(ar)
    mk = [1]*(len(ar)+1)
    for i in range(len(ar)-2, -1, -1): mk[i] = mk[i+1] and ar[i][0] == k

    # print(mk)
    i = 0
    x = 0
    for ct, v in ar:
        j = 0
        for _ in range(ct):
            x += 1
            j += 1
            f1 = j+ar[-1][0] == k and v == ar[-1][1]
            f2 = j == k and ar[-1][0] == k and v != ar[-1][1]
            f3 = ct-j in [k, 0]
            if mk[i+1] and f3 and (f1 or f2):
                print(x)
                return
        if ct != k: break
        i += 1

    print(-1)





for _ in range(int(input())): solve()
