# hard question that solved by great observation
# I incoporated it with greedy: 94%
# the solution is very clean for a hard problem
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        idx = 0
        for a, b in queries:
            s1, s2 = bin(a)[2:], bin(b)[2:]
            n, m = len(s1), len(s2) 
            tmp = min(n, m)
            i = 0
            while i < tmp:
                if s1[i] != s2[i]:
                    break
                i += 1
            length = n-1-(i-1) + m-1-(i-1) + 1
            ans[idx] = length
            idx+=1
        return ans
