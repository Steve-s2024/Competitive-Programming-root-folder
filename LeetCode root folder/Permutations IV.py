# brute-force: doesn't work
class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        res = []

        def recursive(nums, perm):
            if len(res) == k:
                return
            if len(nums) == 0:
                res.append(perm)
                return
            for num in nums:
                if perm and num % 2 == perm[-1] % 2:
                    continue
                i = nums.index(num)
                nums.pop(i)
                recursive(nums, perm + [num])
                nums.insert(i, num)

        arr = [i for i in range(1, n + 1)]
        recursive(arr, [])
        return res[-1]

