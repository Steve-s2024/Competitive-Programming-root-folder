# further optimized solution with binary search, TLE
def solve():
    k, l1, r1, l2, r2 = [int(e) for e in input().split()]
    # k^0, k^1, k^2, k^3....
    res = 0
    tar = 1
    while l1*tar <= r2:
        left, right = -1, -1
        l, r = l1, r1
        while l <= r:
            m = (l+r)//2
            if m * tar > r2:
                r = m-1
            else:
                right = m
                l = m+1
        l, r = l1, r1
        while l <= r:
            m = (l+r)//2
            if m * tar < l2:
                l = m+1
            else:
                left = m
                r = m-1
        # print(left, right)
        tar *= k
        if left != -1 and right != -1:
            res += right - left + 1
    print(res)


t = int(input())
for tt in range(t):
    solve()


# optimized brute force
def solve():
    k, l1, r1, l2, r2 = [int(e) for e in input().split()]
    # k^0, k^1, k^2, k^3....
    res = 0
    for i in range(l1, r1+1):
        power = 1
        while i * power < l2:
            power *= k

        while i * power <= r2:
            print(i, i*power)
            res += 1
            power *= k
    print(res)

t = int(input())
for tt in range(t):
    solve()


# brute force TLE
def solve():
    k, l1, r1, l2, r2 = [int(e) for e in input().split()]
    # k^0, k^1, k^2, k^3....

    st = set()
    for i in range(3):
        st.add(pow(3, i))
    i = 0
    for i in range(l1, r1+1):
        for j in range(l2, r2+1):
            if j % i == 0 and j // i in st and i in range(l1, r1+1) and j in range(l2, r2+1):
                print(j, i)


t = int(input())
for tt in range(t):
    solve()