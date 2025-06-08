# contest3 question1 20250201
class Solution:
    def findValidPair(self, s: str) -> str:
        hashMap = defaultdict(int)
        for c in s:
            hashMap[c] += 1
        for i in range(len(s) - 1):
            a = s[i]
            b = s[i + 1]

            if hashMap[a] == int(a) and hashMap[b] == int(b) and a != b:
                return a + b

        return ''