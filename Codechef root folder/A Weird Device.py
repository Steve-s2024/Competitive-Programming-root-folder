# a weird question
# cook your dish here
t = int(input())
for tt in range(t):
    [k, n] = [int(e) for e in input().split(' ')]
    # num = 13*11*7
    num = 1001
    # 1001 * abc --> abcabc

    s = str(k)
    hashSet = set(s)


    def recursive(a, b, c, i):
        if i >= 3:
            return 1
        res = 0
        if a:
            res += recursive(a - 1, b, c, i + 1)
        if b:
            res += recursive(a, b - 1, c, i + 1)
        if c:
            res += recursive(a, b, c - 1, i + 1)
        return res


    if len(hashSet) == 1:
        res = 1
    elif len(hashSet) == 2:
        if n == 1:
            res = recursive(4, 2, 0, 0)
        else:
            res = pow(2, 3)
    else:
        if n == 1:
            res = recursive(2, 2, 2, 0)
        else:
            res = pow(3, 3)

    print(res)