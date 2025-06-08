# solution incomplete, the solution will work with non-duplicate input!
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        arr = [0]
        i = 0
        n = len(coins)
        while i < n:
            emptySpot = coins[i]-arr[-1] - 1
            if emptySpot != 0 and arr[-1]-1 < emptySpot:
                break
            arr.append(coins[i])
            print(arr, emptySpot)
            i+=1
        
        return arr[-1] + arr[-1]
    
    

# solution no.2 brute force: TLE
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        hashSet = set()
        hashSet.add(0)

        for c in coins:
            keys = list(hashSet)
            for ele in keys:
                hashSet.add(ele+c)
        # print(hashSet)
        nums = list(hashSet)
        nums.sort()
        # print(nums)
        n = len(nums)
        i = 1
        while i < n:
            if nums[i] != nums[i-1]+1:
                break
            i+=1 
        return i


# optimized brute force n^2 solution: I don't understand why 
# the testcase expected output is not correct.  turns out the
# description is confusing...
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        hashSet = set()
        hashSet.add(0)

        for c in coins:
            keys = list(hashSet)
            for ele in keys:
                hashSet.add(ele+c)
        # print(hashSet)
        nums = list(hashSet)
        nums.sort()
        # print(nums)
        res = 0
        n = len(nums)
        l, r = 0, 1
        while r < n:
            while r < n and nums[r] == nums[r-1] + 1:
                r+=1
            res = max(res, r-l)
            l = r
            r += 1
        return res