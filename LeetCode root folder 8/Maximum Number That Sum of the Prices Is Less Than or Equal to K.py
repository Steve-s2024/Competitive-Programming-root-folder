# pretty combinatorics heavy question, the sample test give away the monotonic nature of the answer, so binary
# search is hard to think of. initially I thought i need digit dp for the body of the binary search, but turns out
# it can be cleaner with just combinatorics manipulation.

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def helper(n):
            s = str(bin(n))[2:]
            sz = len(s)
            res = 0
            # print(s)
            for i in range(sz - 1, -1, -1):
                if (sz - i) % x == 0:
                    a, b = 0, 0
                    for j in range(i + 1, sz):
                        b *= 2
                        b += int(s[j])
                    for j in range(i):
                        a *= 2
                        a += int(s[j])

                    # print(bin(a), bin(b))
                    if s[i] == '1':
                        if a: res += a * pow(2, sz - i - 1)
                        res += b + 1
                    else:
                        if a: res += a * pow(2, sz - i - 1)
            return res

        # for i in range(1, 10):
        #     print(helper(i))

        l, r = 0, 1 << 64
        ans = -1
        while l <= r:
            m = (l + r) // 2
            res = helper(m)
            if res <= k:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans

