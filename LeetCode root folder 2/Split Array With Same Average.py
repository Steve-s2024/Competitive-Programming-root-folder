

# dp solution, focus on only one array instead of two: MLE
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        avrg = sum(nums) / n
        dp = set()
        def recursive(i, total, size):
            nonlocal n, avrg
            if size != n and size != 0 and total / size == avrg:
                return True
            if (i, total, size) in dp:
                return False
            dp.add((i, total, size))
            if i >= n:
                return False
            if size and min(nums[i], total/size) > avrg:
                return False

            return (
                recursive(i+1, total+nums[i], size+1) or
                recursive(i+1, total, size)
            )
        return recursive(0, 0, 0)


# dp solution: MLE
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = set()
        def recursive(i, total1, total2, size1, size2):
            nonlocal n
            if (i, total1, total2, size1, size2) in dp:
                return False

            dp.add((i, total1, total2, size1, size2))

            if i >= n:
                if size1 == 0 or size2 == 0:
                    return False
                return total1 / size1 == total2 / size2

            return (
                    recursive(i + 1, total1+nums[i], total2, size1 + 1, size2) or
                    recursive(i + 1, total1, total2 + nums[i], size1, size2 + 1)
            )

        return recursive(0, 0, 0, 0, 0)
