# greedy:2
# ms
# Beats
# 78.58%
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # brute-force
        res = []
        l = len(arr)
        count = 0
        while count < len(arr):
            idx = 0
            val = arr[0]
            for i in range(l-count):
                if arr[i] < val:
                    val = arr[i]
                    idx = i

            res.append(idx+1)
            res.append(l-count)
            first = arr[:idx+1]
            first.reverse()
            second = first + arr[idx+1:l-count]
            second.reverse()
            arr = second + arr[l-count:]
            count += 1
        res.append(l)
        return res