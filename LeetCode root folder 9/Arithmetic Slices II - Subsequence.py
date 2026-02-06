# solved via building from small array to big array, each time a new element is introduced, check with all the previous
# elements and use their difference as the search key to look up for arithmetic sequence end at old elements with the same difference

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        mp = [defaultdict(int) for _ in range(n)]
        res = 0
        for i in range(1, n):
            for j in range(i):
                x = nums[i] - nums[j]
                mp[i][x] += mp[j][x]
                res += mp[j][x]
                mp[i][x] += 1

        return res



# thought this is possible, so I wrote the same approach in general recursive form, runs the same time
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def recursive(i):
            if i >= n: return defaultdict(int)
            mp = defaultdict(int)
            for j in range(i+1, n):
                tmp = recursive(j)
                mp[nums[j]-nums[i]] += tmp[nums[j]-nums[i]]+1
            return mp
        ans = 0
        for i in range(n): ans += sum(recursive(i).values())
        return ans-n*(n-1)//2
