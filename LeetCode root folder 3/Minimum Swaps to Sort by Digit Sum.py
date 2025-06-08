# made a stupid mistake, but everything else is smooth, and the simulation
# takes a bit brain power
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        idxMp = {}
        for i in range(n):
            sm = sum(int(e) for e in list(str(nums[i])))
            arr.append((sm, nums[i]))
            idxMp[nums[i]] = i

        arr.sort(key = lambda i : (i[0], i[1]))
        res = 0
        for i in range(n):
            sm, cur = arr[i]
            a, b = i, idxMp[cur]
            if a != b:
                A, B = nums[a], nums[b]
                idxMp[nums[a]] = b
                idxMp[nums[b]] = a
                nums[a], nums[b] = B, A

                res += 1
        return res