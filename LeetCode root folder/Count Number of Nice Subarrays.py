# relatively easy, greedy solution:65
# ms
# Beats
# 88.77%
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        indices = []
        for idx, num in enumerate(nums):
            if num % 2 == 1:
                indices.append(idx)
        # print(indices)
        l, r = 0, k-1
        res = 0
        while r < len(indices):
            n1, n2 = indices[l]+1, len(nums)-indices[r]
            if l > 0:
                n1 = indices[l] - indices[l-1]
            if r < len(indices)-1:
                n2 = indices[r+1] - indices[r]
            # print(n1, n2, (l, r))
            res += n1 * n2
            l += 1
            r += 1
        return res