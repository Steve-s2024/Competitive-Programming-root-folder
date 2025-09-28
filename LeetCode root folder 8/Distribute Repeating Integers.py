# knap sack bitmask DP: TL....E? wait! it's AC!! 58%
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        arr = list(Counter(nums).values())
        # we know len(arr) <= 50
        n, m = len(arr), len(quantity)
        @cache
        def recursive(i, mask, tot):
            nonlocal n, m
            if mask == (1<<m)-1: return True
            if i >= n: return False
            for j in range(m):
                if (1<<j) & mask: continue
                if tot+quantity[j] <= arr[i] and recursive(i, mask|(1<<j), tot+quantity[j]): return True
            return recursive(i+1, mask, 0)
        return recursive(0, 0, 0)

