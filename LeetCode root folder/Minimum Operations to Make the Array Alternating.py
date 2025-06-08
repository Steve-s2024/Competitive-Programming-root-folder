#52%
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        map1, map2 = defaultdict(int), defaultdict(int)
        for i in range(len(nums)):
            if i % 2:
                map1[nums[i]] += 1
            else:
                map2[nums[i]] += 1

        max1, max2 = 0, 0
        key1, key2 = '', ''
        for key, val in map1.items():
            if val > max1:
                max1 = val
                key1 = key
        for key, val in map2.items():
            if val > max2:
                max2 = val
                key2 = key
        if key1 != key2:
            return len(nums) - max1 - max2

        sec1, sec2 = 0, 0
        for key, val in map1.items():
            if key != key1:
                if val > sec1:
                    sec1 = val
        for key, val in map2.items():
            if key != key2:
                if val > sec2:
                    sec2 = val

        return len(nums) - max(max1 + sec2, max2 + sec1)