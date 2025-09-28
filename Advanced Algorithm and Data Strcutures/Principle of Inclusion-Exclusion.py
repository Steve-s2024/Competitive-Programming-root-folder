# very interesting property of set theory, efficiently compute the size of the union of multiple sets
# time complexity: 2^n where n is the number of sets in the union operation.
# there could be an extra computation per each recursive call, such as the example below where we need to calculate the
# lcm of the stk array each time, which may affect the time complexity

# here is an implementation of the PIE in finding all number i between 1 and n inclusive that are divisible by either
# 3, 5, or 7
def findMultipleOfNums(self, n: int) -> int:
    ref = [3, 5, 7]
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
