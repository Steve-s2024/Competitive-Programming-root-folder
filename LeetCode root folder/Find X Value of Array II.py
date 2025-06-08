# dp & segment tree solution, but didn't come up with the waay to
# do the update... today's contest is solid

class Node:
    def __init__(self, val=None, left=None, right=None): …

    class SumTree:
        def build(self, l, r, arr, k): …

        def query(self, l, r, L, R, node, k): …

        class Solution:
            def getDp(self, nums, k): …

            def printTree(self, node): …

            def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
                obj = SumTree()
                dp = self.getDp(nums, k)
                n = len(dp)
                tree = obj.build(0, n - 1, dp, k)
                # self.printTree(tree)
                # print(dp)
                q = len(queries)
                ans = [0] * q
                for i in range(q):
                    [idx, val, strt, x] = queries[i]
                    ans[i] = obj.query(0, n - 1, strt, n - 1, tree, k)[x]
                return ans©leetcode