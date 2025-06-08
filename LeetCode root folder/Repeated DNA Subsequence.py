# an easy disguised as medium
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        idx = 0
        hashSet = set()
        visited = set()
        while idx <= len(s)-10:
            curSeq = s[idx:idx+10]
            if curSeq in hashSet and curSeq not in visited:
                res.append(curSeq)
                visited.add(curSeq)
            else:
                hashSet.add(curSeq)
            idx += 1
        return res