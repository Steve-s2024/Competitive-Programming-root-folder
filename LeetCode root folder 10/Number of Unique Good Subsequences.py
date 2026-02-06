# very innovative way of designing DP, with a spice of greedy
# constructing the tree of decision, the number of unique binary string is the number of node in the tree.
# the tree should be constructed greedily

class Solution:
    def numberOfUniqueGoodSubsequences(self, bi: str) -> int:
        if '1' not in bi: return 1
        mod = 10**9 + 7
        n = len(bi)
        zero, one = bi.rfind('0'), bi.rfind('1')
        @cache
        def fn(i, f):
            nonlocal mod, n, zero, one
            if i >= n: return 0

            if f and bi[i] == '1' or not f and bi[i] == '0':
                a = fn(i+1, 0) if i < zero else 0
                b = fn(i+1, 1) if i < one else 0
                res = a+b
            else: res = fn(i+1, f)-1
            return (res+1)%mod

        return fn(bi.index('1'), 1) + (1 if zero != -1 else 0)
