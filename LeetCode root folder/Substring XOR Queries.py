# brute force but with XOR and preprocess solution: 55%
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # if a ^ b = c, then a = b ^ c, and b = a ^ c
        targets = [str(bin(a ^ b))[2:] for a, b in queries]
        hashMap = {}

        n = len(s)
        for i in range(32):
            for j in range(n-i):
                cur = s[j:j+i+1]
                if cur not in hashMap:
                    hashMap[cur] = (j, j+i)
        # print(hashMap)
        ans = []
        for tar in targets:
            # print(tar)
            # find tar in s
            if tar in hashMap:
                ans.append(hashMap[tar])
            else:
                ans.append((-1, -1))
        return ans



# brute force and XOR soution: TLE
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        # if a ^ b = c, then a = b ^ c, and b = a ^ c
        n = len(s)
        ans = []
        for a, b in queries:
            tar = bin(a ^ b)[2:]
            # print(tar)
            # find tar in s
            size = len(tar)
            for i in range(n-size+1):
                if s[i:i+size] == tar:
                    ans.append((i, i+size-1))
                    break
            else:
                ans.append((-1, -1))
        return ans
