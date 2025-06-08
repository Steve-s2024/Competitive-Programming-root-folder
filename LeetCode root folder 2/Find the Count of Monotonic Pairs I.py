# dp solution, gambled a bit here, didn't expect it to pass: 11%
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        MOD = 10**9 + 7
        def recursive(i, a, b):
            nonlocal n, MOD
            if (i, a, b) in dp:
                return dp[(i, a, b)]
            if i >= n:
                return 1

            res = 0
            for j in range(nums[i] + 1):
                nextA, nextB = j, nums[i] - j
                if nextA >= a and nextB <= b:
                    res += recursive(i + 1, nextA, nextB)
            res %= MOD
            dp[(i, a, b)] = res
            return res

        return recursive(0, -float('inf'), float('inf'))


# brute force recursion: TLE
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        def recursive(i, a, b):
            nonlocal n
            if i >= n:
                return 1

            res = 0
            for j in range(nums[i] + 1):
                nextA, nextB = j, nums[i] - j
                if nextA >= a and nextB <= b:
                    res += recursive(i + 1, nextA, nextB)
            return res

        return recursive(0, -float('inf'), float('inf'))