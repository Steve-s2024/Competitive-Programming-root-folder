# compact solution, hashing, counting, and greedy: bang! 83%
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        n = len(nums)
        ans = [-1] * n
        for i in range(n-1, -1, -1):
            bi = str(bin(nums[i]))[2:][::-1]
            for j in range(len(bi)):
                if bi[j] == '1':
                    hashMap[j] = i
            right = max(hashMap.values()) if hashMap else i
            left = i
            ans[i] = right-left+1

        return ans