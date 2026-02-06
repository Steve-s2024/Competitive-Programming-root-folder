# it is the type of question where almost impossible to analyze the average time complexity accurately
# while the worst big-Oh is terrible
# I really need to run the code before knowing if it will pass the time constraint, and this one passed out of expectation
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        n = len(nums)
        sm = sum(nums)
        if sm % 4: return False

        ar = []

        def recursive(i, msk, SM):
            nonlocal n
            if i >= n:
                if SM * 2 == sm: ar.append(msk)
                return

            recursive(i + 1, msk, SM)
            recursive(i + 1, msk | 1 << i, SM + nums[i])

        recursive(0, 0, 0)

        # print(ar)
        @cache
        def dfs(i, x, msk):
            if i >= n: return x == 0
            if 1 << i & msk:
                return dfs(i + 1, x + nums[i], msk) or dfs(i + 1, x - nums[i], msk)
            else:
                return dfs(i + 1, x, msk)

        for msk in ar:
            if dfs(0, 0, msk) and dfs(0, 0, msk ^ ((1 << n) - 1)): return True
        return False



# MLE
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        n = len(matchsticks)
        sm = sum(matchsticks)
        if sm%4: return False
        @cache
        def recursive(a, b, c, d, i):
            nonlocal n
            if i >= n: return a == b == c == d
            x = matchsticks[i]
            return (
                recursive(a+x, b, c, d, i+1) or
                recursive(a, b+x, c, d, i+1) or
                recursive(a, b, c+x, d, i+1) or
                recursive(a, b, c, d+x, i+1)
            )
        return recursive(0, 0, 0, 0, 0)