# the debug is absolutely intense.
# I know nothing about why it fails, so I kept changing what I can, making the code even just a better and more
# reliable in structure. after around 40 min when I just want to give up, it worked!

# this is absolutely the type of question both hard on design and implementation, and it is very productive in
# writing good code. (implementation is hard because it's tricky though it's not long)

# personally feel like this is the hardest problem solved in live contest
def solve():
    n, m = [int(e) for e in input().split()]
    nums = [int(e) for e in input().split()]
    ar = [(e, i) for i, e in enumerate(nums)]
    ar.sort()

    if 2*m > n:
        print(-1)
        return


    # print(ar)
    if m == 0:
        ans = []
        h = ar[-1][0]
        idx = 0
        for i in range(n-1):
            if h <= ar[i][0]:
                idx = i
                break

            a, b = ar[i][1], ar[-1][1]
            ans.append((a, b))
            h -= ar[i][0]
        else:
            print(-1)
            return

        for j in range(idx+1, n):
            a, b = ar[j-1][1], ar[j][1]
            ans.append((a, b))
    else:
        ans = []
        l, r = n-m, n
        while r > 0:
            for i in range(max(m, l), r):
                a, b = ar[i][1], ar[i-m][1]
                ans.append((a, b))
            l, r = l-m, r-m
        ans = ans[::-1]

    # print(ans)
    print(len(ans))
    for a, b in ans: print(f'{a+1} {b+1}')



for _ in range(int(input())): solve()