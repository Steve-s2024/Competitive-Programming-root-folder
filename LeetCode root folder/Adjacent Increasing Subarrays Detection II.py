class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        curLen = 1
        records = []
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curLen += 1
            else:
                records.append(curLen)
                curLen = 1
        records.append(curLen)
        # print(records)
        maxLen = records[0] // 2

        for idx in range(1, len(records)):
            maxLen = max(maxLen, records[idx] // 2, min(records[idx-1], records[idx]))
        return maxLen