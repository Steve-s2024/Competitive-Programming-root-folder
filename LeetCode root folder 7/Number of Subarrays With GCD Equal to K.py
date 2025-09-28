# logtrick solution with binary search: 93%
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        arr = []
        for i in range(n):
            arr.append(nums[i])
            for j in range(i-1, -1, -1):
                GCD = gcd(arr[i], arr[j])
                if GCD == arr[j]: break
                arr[j] = GCD
            # print(arr)
            l, r = bisect_left(arr, k), bisect_right(arr, k)
            if l > i or arr[l] > k: continue
            res += r-l
        return res

