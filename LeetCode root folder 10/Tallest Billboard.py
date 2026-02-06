# I had a feeling that it might not work, but walla!
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        @cache
        def recursive(i, sm):
            nonlocal n
            if i >= n: return 0 if sm == 0 else -inf
            x = rods[i]
            a = recursive(i+1, sm+x) + rods[i]
            b = recursive(i+1, sm-x) + rods[i]
            c = recursive(i+1, sm)
            return max(a, b, c)
        res = recursive(0, 0)
        # print(res)
        return res//2