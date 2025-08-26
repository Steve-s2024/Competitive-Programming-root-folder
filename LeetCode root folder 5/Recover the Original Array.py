# don't know why it is rated so high, it is barely a hard, kindda average medium: 20%
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = None
        for i in range(1, n):
            dif = nums[i]-nums[0]
            if dif == 0: continue
            mp = Counter(nums)
            for j in range(n):
                if mp[nums[j]] == 0: continue
                if nums[j] + dif not in mp or mp[nums[j]+dif] < mp[nums[j]]: break
                mp[nums[j]+dif] -= 1
                mp[nums[j]] -= 1
            else:
                if dif%2 == 0:
                    res = dif//2
                    break
        arr = []
        mp = Counter(nums)
        for i in range(n):
            if mp[nums[i]] == 0: continue
            mp[nums[i]+2*res] -= 1
            mp[nums[i]] -= 1
            arr.append(nums[i]+res)
        return arr
