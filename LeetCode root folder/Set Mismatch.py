class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        tar = nums[0]
        sum_ = sum(nums)
        for num in nums:
            hashMap[num] += 1
            if hashMap[num] == 2:
                tar = num
                break
        l = len(nums)
        area = int(l*(l+1)/2)
        diff = abs(sum_ - area)
        if sum_ > area:
            return [tar, tar - diff]
        else:
            return [tar, diff + tar]
