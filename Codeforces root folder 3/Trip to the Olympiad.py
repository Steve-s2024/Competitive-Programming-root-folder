# kinda hard, specially the constructing part, need to have very
# good greedy thinking to get the solution to build the three numbers

def solve():
    l, r = [int(e) for e in input().split()]
    res = [-1, -1, -1]
    a, b = str(bin(l))[2:], str(bin(r))[2:]

    if len(a) == len(b):
        i = 0
        tmp = []
        while a[i] == b[i]:
            tmp.append(b[i])
            i+=1
        tmp.append('1')
        i+=1
        while i < len(b):
            tmp.append('0')
            i+=1

        res[0] = int(''.join(tmp), 2)
        res[1] = res[0]-1
        for i in range(l, r+1):
            if i not in res:
                res[2] = i
                break



    else:
        tmp = 1
        while tmp<<1 <= r:
            tmp <<= 1

        res[0] = tmp
        res[1] = tmp-1
        for i in range(l, r+1):
            if i not in res:
                res[2] = i
                break

    print(' '.join(str(e) for e in res))





t = int(input())
for i in range(t):
    solve()