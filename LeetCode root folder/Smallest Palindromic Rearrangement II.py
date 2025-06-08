class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        def swap(i, j, s):
            newS = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
            return newS
        hashMap = Counter(s)
        mid = ''
        for key in hashMap:
            if hashMap[key] % 2 == 1:
                mid = key
            hashMap[key] = hashMap[key] // 2
        # print(hashMap)
        letters = list(hashMap.keys())
        letters.sort()
        s = ''
        for l in letters:
            s += l*hashMap[l]
        # print(s)
        comb = [s]
        
        n = len(s)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                s = swap(j-1, j, s)
                comb.append(s)
        # print(comb)
        tmp = []
        hashSet = set()
        for s in comb:
            if s not in hashSet:
                hashSet.add(s)
                tmp.append(s)
        if k <= len(tmp):
            return tmp[k-1] + mid + tmp[k-1][::-1]
        return ""