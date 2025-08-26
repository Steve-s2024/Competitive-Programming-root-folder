# I am actually not thinking straight, wasted so many times to come to this 'should be' intuitive solution
# the only concern that stopping me from thinking this way is that the number of offset can be huge,
# in that case my recursive function will TLE
import math
from functools import cache
from collections import Counter

def solve():
    MOD = 10**9 + 7
    n = int(input())
    mat = []
    for i in range(n):
        s = input()
        mat.append(s)

    h = n//2
    tot = 1
    for i in range(n):
        mp = Counter(mat[i])
        tot *= mp['1'] if '1' in mp else 0
        # tot %= MOD
    @cache
    def recursive(i):
        nonlocal h
        if i >= h: return 1
        res = 0
        for j in range(n):
            if mat[i][j] == '1' and mat[i+h][j] == '1':
                res += recursive(i+1)
                # res %= MOD
        return res

    print((tot - recursive(0))%MOD)



t = int(input())
for i in range(t):
    solve()





# this is the best I can do, and is not enough

def solve():
    MOD = 10**9 + 7
    n = int(input())
    mat = []
    for i in range(n):
        s = input()
        mat.append(s)

    h = n//2
    stk = []
    dp = {}
    def recursive(i, flag):
        nonlocal n, h
        state = tuple([i, flag] + stk)
        if state in dp: return dp[state]
        if i >= n: return 1 if flag else 0
        res = 0
        for j in range(n):
            if mat[i][j] == '1':
                stk.append(j)
                if len(stk) >= h+1 and stk[-h-1] != j: res += recursive(i+1, True)
                else: res += recursive(i+1, flag)
                res %= MOD
                stk.pop()
        dp[state] = res
        return res

    print(recursive(0, False))




t = int(input())
for i in range(t):
    solve()