# 87%
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        ans = []
        minDiff = float('inf')
        for i in range(1, n):
            diff = arr[i] - arr[i-1]
            if diff < minDiff:
                ans = [[arr[i-1], arr[i]]]
                minDiff = diff
            elif diff == minDiff:
                ans.append([arr[i-1], arr[i]])
        return ans