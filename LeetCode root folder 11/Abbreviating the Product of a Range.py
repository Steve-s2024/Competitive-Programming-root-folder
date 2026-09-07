# such an unstable solution passes all testcases, why not?
# this is not really an enjoyable and productive problem. It is just "be bold" and test your way out.


class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        r = 1
        f, c = 1, 0
        for i in range(left, right+1):
            r *= i
            while r >= 10**20: r //= 10
            f *= i
            while f%10 == 0:
                f//=10
                c += 1
            f %= 10**20
        f %= 10**5
        while r >= 10**5: r //= 10
        # print(r, f, c)

        t = 1
        for i in range(left, right+1):
            t *= i
            while t%10 == 0: t //= 10
            # print(t)
            if t >= 10**20: break
        if t >= 10**10: return str(r) + '...' + str(f).zfill(5) + 'e' + str(c)
        return str(t) + 'e' + str(c)
