# wow, a lot of people can solve the math heavy 
# question so fast, but they are weak on DSA 
# questions like this one...
def locate(x, y, n):
    tmp = pow(2, 2*n)
    l, r = 1, pow(2, n)
    t, b = 1, pow(2, n)
    def recursive(l, r, t, b, num):
        nonlocal x, y, tmp
        # print(l, r, t, b, tmp)
        if l == r and t == b:
            return num
        xMid = (l+r)//2
        yMid = (t+b)//2
        nextCoor = [
           (l, xMid, t, yMid),
           (xMid+1, r, yMid+1, b),
           (l, xMid, yMid+1, b),
           (xMid+1, r, t, yMid)
        ]

        i = 0
        tmp //= 4
        for L, R, T, B in nextCoor:
            if y in range(L, R+1) and x in range(T, B+1):
                return recursive(L, R, T, B, num+i*tmp)
            i+=1

    return recursive(l, r, t, b, 0)+1

def getCoor(tar, n):
    tmp = pow(2, 2 * n)
    l, r = 1, pow(2, n)
    t, b = 1, pow(2, n)

    def recursive(l, r, t, b, num):
        nonlocal tmp, tar
        # print(l, r, t, b, tmp)
        if l == r and t == b:
            return [t, l]
        xMid = (l + r) // 2
        yMid = (t + b) // 2
        nextCoor = [
            (l, xMid, t, yMid),
            (xMid + 1, r, yMid + 1, b),
            (l, xMid, yMid + 1, b),
            (xMid + 1, r, t, yMid)
        ]

        i = 0
        tmp //= 4
        for L, R, T, B in nextCoor:
            if tar in range(num + i*tmp, num + (i+1)*tmp+1):
                return recursive(L, R, T, B, num + i*tmp)
            i += 1
    return recursive(l, r, t, b, 0)

t = int(input())
for tt in range(t):
    n = int(input())
    q = int(input())
    for i in range(q):
        line = input().split(' ')
        if line[0] == '->':
            res = locate(int(line[1]), int(line[2]), n)
            print(res)
        else:
            res = getCoor(int(line[1]), n)
            print(res[0], ' ', res[1])
