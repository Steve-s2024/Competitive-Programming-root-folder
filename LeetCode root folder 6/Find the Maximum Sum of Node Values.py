# a high rating tree problem, the solution has nothing to do with tree. it is pure greedy: 78%
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        sm = sum(nums)
        arr = [(e^k)-e for e in nums]
        arr.sort()
        for i in range(n):
            if arr[i] > 0:
                re = (n-i)%2
                return max(
                    sum(arr[i+re:]),
                    sum(arr[i-re:])
                ) + sm
        return sm