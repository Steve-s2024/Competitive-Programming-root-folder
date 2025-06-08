# I brute forced it, but maybe there's room for optimization
# no, the editorial suggests the same solution, and even more
# brute force than mine
def solve():
    x, m = [int(e) for e in input().split()]
    l1 = len(str(bin(x))[2:])
    m = min(m, (1<<l1)-1)
    l2 = len(str(bin(m))[2:])
    if l1 != l2:
        print(0)
    else:
        res = 0
        for i in range(1<<(l1-1), m+1):
            tmp = i ^ x
            if tmp != 0 and (x % tmp == 0 or i % tmp == 0):
                res += 1
        print(res)


t = int(input())
for tt in range(t):
    solve()