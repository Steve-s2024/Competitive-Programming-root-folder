# haha, quite surprising as a question. unorthodox for sure.
# I tried to come up with a good greedy approach by studying the tree which provided for the first example test case
# but finally give up and do the recursive brute force, the code is quite short

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # 1. it has node from 1 to n
        # 2. the cost to search i is the path sum from root to parent of i
        # 3. max(cost(i)) is miminized
        # 4. it is a BST

        @cache
        def recursive(l, r):
            if l >= r: return 0
            res = inf
            for i in range(l, r):
                a = max(recursive(l, i - 1), recursive(i + 1, r))
                res = min(res, a + i)
            return res

        return recursive(1, n)


