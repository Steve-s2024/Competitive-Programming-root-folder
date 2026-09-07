# fking hard bro! such a catastrophe today's contest


def solve():
    x = int(input())

    cr = 600
    ar = ['A']*25 + ['C']*24
    i = 24
    while cr > x:
        if i == len(ar)-1 or ar[i+1] == 'A':
            i = 0
            while ar[i] == 'A': i += 1
            i -= 1
        ar[i], ar[i+1] = ar[i+1], ar[i]
        cr -= 1
        i += 1

    ans = []
    for i in range(len(ar)):
        ans.append(ar[i])
        ans.append('R')
    # print(ar)

    ans.pop()
    s = ''.join(ans)
    # print(len(s))
    print(s)



# for _ in range(int(input())): solve()
solve()