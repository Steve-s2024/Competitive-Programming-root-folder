# funny problem, don't need much thinking just make the bruteforce a DP template, choose the state such that
# consider only the current position and the closest position to the left that is >= k: 5%

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = {}

        def recursive(i):
            nonlocal k, n
            idx = -1
            if i >= 3:
                for j in range(i - 1, i - 4, -1):
                    if nums[j] >= k:
                        idx = j
                        break
                else:
                    return float('inf')
            if (i, idx) in dp: return dp[(i, idx)]
            if i >= n: return 0

            if nums[i] >= k:
                res = recursive(i + 1)
            else:
                a = recursive(i + 1)
                tmp = nums[i]
                nums[i] = k
                b = recursive(i + 1) + k - tmp
                nums[i] = tmp
                res = min(a, b)
            if idx != -1: dp[(i, idx)] = res
            return res

        return recursive(0)


# bruteforce: TLE

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def recursive(i):
            nonlocal k, n
            if i >= 3:
                for j in range(i - 1, i - 4, -1):
                    if nums[j] >= k: break
                else:
                    return float('inf')
            if i >= n: return 0

            if nums[i] >= k:
                return recursive(i + 1)
            else:
                a = recursive(i + 1)
                tmp = nums[i]
                nums[i] = k
                b = recursive(i + 1) + k - tmp
                nums[i] = tmp
                return min(a, b)

        return recursive(0)
