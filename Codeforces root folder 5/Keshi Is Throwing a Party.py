# real hard to see the greedy after Binary Search

def solve():
    n = int(input())
    ar = []
    for _ in range(n): ar.append([int(e) for e in input().split()])
    l, r = 1, n
    res = 0
    while l <= r:
        m = (l+r)//2
        x = 0
        for i in range(n):
            a, b = ar[i]
            if b >= x and a >= m-x-1: x += 1

        if x >= m:
            res = m
            l = m+1
        else: r = m-1


    print(res)






for _ in range(int(input())): solve()