# annoying trivial mistakes that delayed me quit a bit in this contest (both in C and D)
def solve():
    n = int(input())
    s = input()
    if len(Counter(s)) == 1:
        print(0)
        return

    # case 1: transform to 00.....000
    cnt1, cnt2 = 0, 0
    x, y = 0, 0
    for i in range(n):
        if s[i] == '0': cnt1 += 1
        else:
            x += 2*cnt1+1
            cnt1 = 0

    res = x+y
    for i in range(n-1, -1, -1):
        if s[i] == '0': cnt2 += 1
        else:
            y += 2*cnt2 + 1
            cnt2 = 0
            x -= 1
            j = i-1
            while j >= 0 and s[j] == '0':
                j -= 1
                x -= 2
        res = min(x+y, res)


    # case 2: transform to 11.....111
    s = ''.join('1' if e == '0' else '0' for e in s)

    cnt1, cnt2 = 0, 0
    x, y = 0, 0
    for i in range(n):
        if s[i] == '0':
            cnt1 += 1
        else:
            x += 2 * cnt1 + 1
            cnt1 = 0

    res2 = x + y
    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            cnt2 += 1
        else:
            y += 2 * cnt2 + 1
            cnt2 = 0
            x -= 1
            j = i - 1
            while j >= 0 and s[j] == '0':
                j -= 1
                x -= 2
        res2 = min(x + y, res2)

    print(min(res, res2))

t = int(input())
for i in range(t): solve()