# a pretty crazy problem. I learned that you can actually compensate the modular operation if want to calculate the
# difference of two number after mod them by a number, here im forces to take the modular before taking the difference
# which is why this comes to play.

# the question itself is a very concise but challenging math heavy problem which is not trivial to come to this solution
# observation regarding the behaviour of digit sum is not straightforward (a+b = c have a carry will always make digit
# sum of c strictly less than DS(a) + DS(b))
def solve():
    l, r, k = [int(e) for e in input().split()]
    mod = 10**9 + 7
    mx = 9//k + 1
    # interesting/standard way to compensate for the mod operation: take mod on both side, add mod on LHS, then take
    # the difference before we take mod again
    res = pow(mx, r, mod) + mod - pow(mx, l, mod)
    print(res % mod)

t = int(input())
for i in range(t): solve()