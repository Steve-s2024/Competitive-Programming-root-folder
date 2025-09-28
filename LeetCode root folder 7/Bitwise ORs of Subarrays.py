# logtrick is actually crazy, solved this 2100 rated question under 5 minutes: 7%
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        vis = set()
        for i in range(n):
            if arr[i] not in vis: vis.add(arr[i])
            for j in range(i-1, -1, -1):
                if arr[i]|arr[j] == arr[j]: break
                arr[j] |= arr[i]
                if arr[j] not in vis: vis.add(arr[j])
        # print(vis)
        return len(vis)