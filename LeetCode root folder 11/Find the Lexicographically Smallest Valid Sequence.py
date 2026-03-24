# really? not hard as a usual 2470

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        ar = [0]*n
        j = n-1
        for i in range(m-1, -1, -1):
            while j >= 0 and word1[j] != word2[i]:
                ar[j] = m-i-1
                j -= 1
            if j >= 0:
                ar[j] = m-i
                j -= 1
        while j >= 0:
            ar[j] = m
            j -= 1
        # print(ar)
        ar.append(0)
        ans = []
        j = 0
        for i in range(m):
            while j < n and word1[j] != word2[i]:
                re = m-i-1
                if ar[j+1]>=re:
                    ans.append(j)
                    # print(j)
                    j += 1
                    for I in range(i+1, m):
                        while word1[j] != word2[I]: j += 1
                        ans.append(j)
                        j += 1
                    return ans
                j += 1
            if j >= n: return []
            ans.append(j)
            j += 1

        return [] if len(ans) != m else ans

