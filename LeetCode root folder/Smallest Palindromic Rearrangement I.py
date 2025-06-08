# im the best~~~~
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        hashMap = Counter(s)
        letters = list(hashMap.keys())
        letters.sort(reverse = True)
        res = ''
        mid = ''
        for l in letters:
            cnt = hashMap[l]
            if cnt % 2 == 1:
                mid = l
            h = cnt // 2
            res = l*h + res + l*h
        n = len(res) // 2
        return res[:n] + mid + res[n:]