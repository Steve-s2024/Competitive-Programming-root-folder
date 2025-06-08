# recursive solution, brain killer:231
# ms
# Beats
# 23.27%

'''class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        res = float('inf')
        def recursive(i1, previ1, i2, count):
            nonlocal res
            if i2 >= len(nums2):
                res = min(nums2[i2-1]-nums1[previ1], res)
                return
            diff1 = nums1[i1] - nums1[previ1]
            diff2 = nums2[i2] - nums2[i2-1]
            if diff1 != diff2:
                if count < 2:
                    recursive(i1+1, previ1, i2, count+1)
                return

            if count < 2:
                recursive(i1+1, previ1, i2, count+1)
            recursive(i1+1, i1, i2+1, count)
        recursive(1, 0, 1, 0)
        recursive(2, 1, 1, 1)
        recursive(3, 2, 1, 2)
        return res'''


# dp solution. although the state of the dp hash map consist of four variables, but the space complexity is only
# O(n^2) when you realize that previ1 and count only have 4 possibilities: 59
# ms
# Beats
# 52.20%

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        dp = {}
        def recursive(i1, previ1, i2, count):
            if (i1, previ1, i2, count) in dp:
                return dp[(i1, previ1, i2, count)]
            res = float('inf')
            if i2 >= len(nums2):
                return nums2[i2-1]-nums1[previ1]
            diff1 = nums1[i1] - nums1[previ1]
            diff2 = nums2[i2] - nums2[i2-1]
            if diff1 != diff2:
                if count < 2:
                    res = recursive(i1+1, previ1, i2, count+1)
                else:
                    res = float('inf')
            elif count < 2:
                res = min(
                    recursive(i1+1, previ1, i2, count+1),
                    recursive(i1+1, i1, i2+1, count)
                )
            else:
                res = recursive(i1+1, i1, i2+1, count)
            dp[(i1, previ1, i2, count)] = res
            return res
        return min(
            recursive(1, 0, 1, 0),
            recursive(2, 1, 1, 1),
            recursive(3, 2, 1, 2)
        )

# The supposed solution, sorting plus two pointer, hard to come up with:33
# ms
# Beats
# 100.00%

'''
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        arr = [
            nums2[0] - nums1[0],
            nums2[0] - nums1[1],
            nums2[0] - nums1[2]
        ]
        res = float('inf')
        for diff in arr:
            i, j = 0, 0
            count = 0

            while j < len(nums2):
                if nums1[i] + diff != nums2[j]:
                    count += 1
                    i += 1
                    if count > 2:
                        break
                else:
                    i += 1
                    j += 1
            else:
                res = min(res, diff)

        return res
'''