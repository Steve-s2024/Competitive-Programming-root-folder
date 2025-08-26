# this shit is so hard, got into a place of knap-sack I have never been before. I don't think it is the intended
# solution though: 6%
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        mp = Counter(nums)
        arr = []
        for key, val in mp.items():
            arr.append((key, val > 1))

        arr.sort(key=lambda i: i[0])
        n = len(arr)

        @cache
        def recursive(i, j, finc):
            if i >= n: return 0
            if arr[j][0] + finc < arr[i][0] - 1: return 0
            res = recursive(i + 1, j, finc)
            if arr[j][0] + finc + 1 == arr[i][0] + 1:
                if j != i or arr[i][1]:
                    a = recursive(i + 1, i, 1) + 1
                    res = max(a, res)
            if arr[j][0] + finc + 1 == arr[i][0]:
                a = recursive(i, i, 0) + 1
                res = max(a, res)
            return res

        res = 0
        for i in range(n):
            res = max(
                recursive(i, i, 0) + 1,
                recursive(i + 1, i, 1) + 1,
                res
            )
        return res


# here is the intended solution 😥
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        dp=defaultdict(int)
        nums.sort()
        for a in nums:
            dp[a+1]=dp[a]+1
            dp[a]=dp[a-1]+1
        return max(dp.values())