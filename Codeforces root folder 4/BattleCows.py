# first time ever solved F, though it is a div4. (div3E ~ div2D)

def build(nums):
    n = len(nums)
    sp = [nums[:]]
    pw = 2
    while pw < n:
        tmp = []
        for i in range(0, n, pw):
            x = 0
            for j in range(i, i+pw): x^=nums[j]
            tmp.append(x)
        sp.append(tmp)
        pw *= 2
    return sp

def solve():
    n, q = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    sp = build(A)
    ar = []
    # print(sp)
    for _ in range(q):
        b, c = [int(e) for e in input().split()]
        j = b-1
        i = 0
        x = 0
        cr = c
        # print('?', b, c)
        while i < len(sp):
            op = sp[i][j+1] if j%2 == 0 else sp[i][j-1]
            # print(sp[i])
            # print(cr, op)
            if op > cr or (op == cr and j%2 == 1): x += 1<<i
            cr ^= op
            i += 1
            j //= 2
        # print(x)
        ar.append(x)
    # print(' '.join(str(e) for e in ar))
    for v in ar: print(v)


for _ in range(int(input())): solve()
