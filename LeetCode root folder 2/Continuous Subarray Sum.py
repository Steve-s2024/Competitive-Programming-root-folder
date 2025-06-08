# able to solve this almost 100% by myself is significant milestone
# of my journey to success --Stephen 2025/05/02
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # nums = [num % k for num in nums]
        n = len(nums)
        total = 0
        hashMap = {}
        hashMap[0] = -1
        for i in range(n):
            total += nums[i]
            remain = total % k
            # print(remain, i)
            if remain in hashMap and hashMap[remain]+2 <= i:
                return True
            if remain not in hashMap:
                hashMap[remain] = i
        # print(hashMap)
        return False

