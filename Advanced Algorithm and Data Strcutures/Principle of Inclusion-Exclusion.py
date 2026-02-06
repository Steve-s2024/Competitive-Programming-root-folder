# a simpler version of PIE, finding number between 1 and n that are div by nums[i]
def PIE(m, nums):
    n = len(nums)
    @cache
    def recursive(i, LCM, x):
        nonlocal n, m
        if i >= n: return (m//LCM) if x%2 == 1 else -(m//LCM)
        return recursive(i+1, LCM, x) + recursive(i+1, lcm(LCM, nums[i]), x+1)
    return sum(recursive(i+1, nums[i], 1) for i in range(n))




# very interesting property of set theory, efficiently compute the size of the union of multiple sets
# time complexity: 2^m where m is the number of sets in the union operation.
# there could be an extra computation per each recursive call, such as the example below where we need to calculate the
# lcm of the stk array each time, which may affect the time complexity


# here is an implementation of the PIE in finding all number i between 1 and n inclusive that are divisible by either
# factors in ref
from math import lcm
def findMultipleOfNums(n: int) -> int:
    ref = [2,7,13,19]
    m = len(ref)
    stk = []
    def recursive(i):
        nonlocal m
        size = len(stk)
        res = 0
        if size:
            LCM = stk[0]
            for v in stk: LCM = lcm(LCM, v)
            if size % 2 == 1:
                res += n // LCM
            else:
                res -= n // LCM
        if size == m: return res
        for j in range(i, m):
            stk.append(ref[j])
            res += recursive(j + 1)
            stk.pop()
        return res

    return recursive(0)


print(findMultipleOfNums(12))