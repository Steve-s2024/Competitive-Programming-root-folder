# greedy solution with sorting:163
# ms
# Beats
# 44.27%

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = defaultdict(list)
        for i, n in enumerate(nums2):
            hashMap[n].append(i)
        nums1.sort()
        nums2.sort()
        res = [float('inf')] * len(nums1)
        while nums2:
            if nums1[-1] > nums2[-1]:
                res[hashMap[nums2[-1]].pop()] = nums1[-1]
                nums1.pop()
                nums2.pop()
            else:
                nums2.pop()
        # print(res)
        for i in range(len(res)):
            if res[i] == float('inf'):
                res[i] = nums1.pop()
        return res
