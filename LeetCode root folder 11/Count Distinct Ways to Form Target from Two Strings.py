# maybe will work, try after contest ended (didn't work)



class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        n1, n2, n3 = len(word1), len(word2), len(target)
        M = 10**7 + 9
        @cache
        def fn(i, j, k, f, ):
            if k == n3: return 1 if i!=0 and j!=0 else 0

            res = 0
            if f == 0: # use word1
                if i < n1: res += fn(i+1, j, k, f)
                if i < n1 and word1[i] == target[k]:
                    if k == n3-1: res += 1 if i!=0 and j!=0 else 0
                    else: res += fn(i+1, j, k+1, f) + fn(i+1, j, k+1, f^1)
            else: # use word2
                if j < n2: res += fn(i, j+1, k, f)
                if j < n2 and word2[j] == target[k]:
                    if k == n3-1: res += 1 if i!=0 and j!=0 else 0
                    else: res += fn(i, j+1, k+1, f) + fn(i, j+1, k+1, f^1)

            return res % M
        # print(fn(0, 0, 0, 0) , fn(0, 0, 0, 1))
        return fn(0, 0, 0, 0) + fn(0, 0, 0, 1)
