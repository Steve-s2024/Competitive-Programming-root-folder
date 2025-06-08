# ah.. I thought the time complexity won't let me pass
# but maybe I got the time complexity wrong, recursive
# & brute force solution: 100%
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        used = set()
        n = len(nums)
        def recursive(i):
            nonlocal n
            if len(used) == n:
                return 1
            res = 0
            hashSet = set()
            for j in range(n):
                if nums[j] in hashSet or j in used:
                    continue
                tar = math.sqrt(nums[i] + nums[j])
                if tar != int(tar):
                    continue
                # print(i, j)
                hashSet.add(nums[j])
                used.add(j)
                res += recursive(j)
                used.remove(j)
            return res
        
        res = 0
        hashSet = set()
        for i in range(n):
            if nums[i] in hashSet:
                continue
            hashSet.add(nums[i])
            used.add(i)
            res += recursive(i)
            used.remove(i)
        return res

                
                 