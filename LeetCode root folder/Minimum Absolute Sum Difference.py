# sorting and binary search solution, get crashed...:  5%
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        nums = nums1[:]
        nums.sort()
        def binarySearch(tar):
            nonlocal n
            l, r = 0, n-1
            res = float('inf')
            while l <= r:
                m = (l+r)//2
                diff = abs(tar - nums[m])
                res = min(res, diff)
                if tar > nums[m]:
                    l = m+1
                else:
                    r = m-1
            return res
                
        
        total = 0
        for i in range(n):
            total += abs(nums1[i]-nums2[i])
        # print(total)
        maxReduce = float('inf')
        for i in range(n):
            diff1 = abs(nums1[i]-nums2[i])
            diff2 = binarySearch(nums2[i])    
            # print(i, diff1, diff2)
            maxReduce = min(maxReduce, diff2-diff1)
        # print(maxReduce)
        return (total + maxReduce) % 1000000007   