# definitely learning a lot by doing this, but still under progress. my approach is pretty above my level so it is
# not a terrible thing to fail it.
# still, able to even come up with the idea is pretty much a victory

# the code is being optimized to a point it cannot run faster. need another approach to solve the problem
# the reason why it is slow mainly because the two iterative DFS on half of the element, these two will add
# 2^13 + 2^13 each time to the time, and with a thousand cases it will exceed time limit easily

from collections import deque, Counter, defaultdict

mod = 998244353
glbArr = []
f = 1
for i in range(5*(10**5)):
    f *= i+1
    f %= mod
    glbArr.append(f)


def solve():
    nums = [int(e) for e in input().split()]
    tmp = []
    for val in nums:
        if val: tmp.append(val)
    nums = tmp
    sm = sum(nums)
    n = len(nums)
    if n == 1:
        if sm == 1: print(1)
        else: print(0)
        return

    mp = defaultdict(int)
    stk = [(0, 0, 0)]
    while stk:
        i, a, b = stk.pop()
        if i >= n//2:
            mp[(a, b)] += 1
            continue
        stk.append((i+1, a+nums[i], b))
        stk.append((i+1, a, b+nums[i]))

    ct = 0
    hf = sm//2
    stk = [(n//2, 0, 0)]
    while stk:
        i, a, b = stk.pop()
        if i >= n:
            if sm % 2 == 0: ct += mp[(hf - a, hf - b)]
            else: ct += mp[(hf + 1 - a, hf - b)]
            continue
        stk.append((i + 1, a + nums[i], b))
        stk.append((i + 1, a, b + nums[i]))

    arr = [glbArr[val-1] for val in nums]
    x = glbArr[hf-1]
    if sm%2 == 0: x *= x
    else: x *= x*(hf+1)

    for val in arr:
        x *= pow(val, mod-2, mod)
        x %= mod

    print((ct*x) % mod)



t = int(input())
for i in range(t): solve()


