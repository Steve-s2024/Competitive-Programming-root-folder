# greedy solution:43
# ms
# Beats
# 27.06%
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res1 = res2 = res3 = -float('inf')
        tar1, tar2, tar3 = target[0], target[1], target[2]
        for n1, n2, n3 in triplets:
            if (
                n1 > tar1 or
                n2 > tar2 or
                n3 > tar3
            ):
                continue

            res1 = max(res1, n1)
            res2 = max(res2, n2)
            res3 = max(res3, n3)
        return res1 == tar1 and res2 == tar2 and res3 == tar3