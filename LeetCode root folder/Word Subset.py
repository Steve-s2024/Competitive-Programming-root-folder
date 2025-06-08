# hash table solution:350
# ms
# Beats
# 62.70%
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hashMap = defaultdict(int)
        total = 0
        for word in words2:
            tmp = Counter(word)
            for key, val in tmp.items():
                if val > hashMap[key]:
                    hashMap[key] = val
        # print(hashMap)
        total = sum(hashMap.values())
        res = []
        for word in words1:
            count = 0
            tmp = Counter(word)
            for key, val in tmp.items():
                if key in hashMap:
                    if val < hashMap[key]:
                        break
                    else:
                        count += hashMap[key]
            else:
                if count == total:
                    res.append(word)
        return res
