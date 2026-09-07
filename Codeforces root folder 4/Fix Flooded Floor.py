# greedy, sad I can't see through it

def solve():
    n = int(input())
    g = [
        list(input()),
        list(input()),
    ]


    mf = 0
    for i in range(n):
        a, b = g[0][i], g[1][i]
        if a == b == '.':
            mf = i < n-1 and g[0][i+1] == g[1][i+1] == '.' or mf
        elif a == '.':
            if i == n-1 or g[0][i+1] != '.':
                print('None')
                return
            g[0][i+1] = '#'
        elif b == '.':
            if i == n-1 or g[1][i+1] != '.':
                print('None')
                return
            g[1][i+1] = '#'

    print('Multiple' if mf else 'Unique')


for _ in range(int(input())): solve()






# dp, clever but not enough


def solve():
    n = int(input())
    g = [
        list(input()),
        list(input()),
    ]

    dp = [[[0, 0] for _ in range(2)] for _ in range(n+1)]
    for a in range(2):
        for b in range(2):
            dp[-1][a][b] = 1 if a and b else 0

    for i in range(n-1, -1, -1):
        for a in range(2):
            for b in range(2):

                res = 0
                if not a and not b:
                    if g[0][i] == g[1][i] == '.':
                        res = dp[i+1][1][1]
                elif not a:
                    if g[0][i] == '.':
                        res = dp[i+1][1][1 if g[1][i] == '#' else 0]
                elif not b:
                    if g[1][i] == '.':
                        res = dp[i+1][1 if g[0][i] == '#' else 0][1]
                else:
                    res = dp[i+1][1 if g[0][i] == '#' else 0][1 if g[1][i] == '#' else 0]
                    if g[0][i] == g[1][i] == '.':
                        res += dp[i+1][1][1]
                dp[i][a][b] = res

    #
    # @cache
    # def fn(i, a, b):
    #     if i >= n: return 1 if a and b else 0
    #
    #     if not a and not b:
    #         if g[0][i] == g[1][i] == '.': return fn(i+1, 1, 1)
    #         else: return 0
    #     if not a:
    #         if g[0][i] == '.': return fn(i+1, 1, 1 if g[1][i] == '#' else 0)
    #         else: return 0
    #     if not b:
    #         if g[1][i] == '.': return fn(i+1, 1 if g[0][i] == '#' else 0, 1)
    #         else: return 0
    #
    #
    #     res = fn(i+1, 1 if g[0][i] == '#' else 0, 1 if g[1][i] == '#' else 0)
    #     if g[0][i] == g[1][i] == '.':
    #         res += fn(i+1, 1, 1)
    #
    #     return res
    #
    #
    # res = fn(0, 1, 1)

    res = dp[0][1][1]
    # print(res)

    if res == 1:
        print('Unique')
    elif res == 0: print('None')
    else: print('Multiple')


for _ in range(int(input())): solve()