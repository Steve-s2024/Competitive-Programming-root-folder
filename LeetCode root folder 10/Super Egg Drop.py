# first time ever, solved a problem without even understanding why, not because taken idea from other
# but I just printed the pattern of optimal choice, and observe the pattern we either choose 1 or old+1
# each time for the new split. (no idea why this is true even after the solution is accepted)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        mp = defaultdict(int)
        @cache
        def recursive(N, K):
            if K < 1: return inf
            if K == 1: return N
            if N == 0: return 0
            res = max(recursive(0, K-1), recursive(N-1, K))
            x = mp[(N-1, K)] + 1
            mp[(N, K)] = 1
            if x <= N:
                a = max(recursive(x-1, K-1), recursive(N-x, K))
                if a < res:
                    res = a
                    mp[(N, K)] = x
            return res+1

        return recursive(n, k)





# rough DP (without optimization), TLE
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        @cache
        def recursive(N, K):
            if K < 1: return inf
            if K == 1: return N
            if N == 0: return 0
            res = inf
            for i in range(1, N + 1):
                a = max(recursive(i - 1, K - 1), recursive(N - i, K)) + 1
                res = min(res, a)
            return res

        return recursive(n, k)
