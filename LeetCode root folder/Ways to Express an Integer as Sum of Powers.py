# dp solution: 26%
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = {}
        def recursive(remain, num):
            if (remain, num) in dp:
                return dp[(remain, num)]
            if remain == 0:
                return 1
            if remain < 0 or pow(num, x) > remain:
                return 0
            res = (
                recursive(remain-pow(num, x), num+1) +
                recursive(remain, num+1)
            )
            dp[(remain, num)] = res
            return res
        return recursive(n, 1) % 1000000007

# template for dp solution (recursion brute force):
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        def recursive(remain, num):
            if remain == 0:
                return 1
            if remain < 0 or pow(num, x) > remain:
                return 0
            return (
                recursive(remain-pow(num, x), num+1) +
                recursive(remain, num+1)
            )
        return recursive(n, 1)
