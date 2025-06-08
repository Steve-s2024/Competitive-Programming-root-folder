# fking phyco question created for torture LeetCoders, should've use brute force for this stupid ass shit!!:0
# ms
# Beats
# 100.00%
class Solution:
    def equalFrequency(self, word: str) -> bool:
        arr = list(Counter(word).values())
        # print(arr)
        hashMap = Counter(arr)
        # print(hashMap)
        if len(hashMap) > 2:
            return False
        keys = hashMap.keys()
        max_, min_ = max(keys), min(keys)
        if len(hashMap) == 2 and (
            (max_ == min_+1 and hashMap[max_] == 1) or
            (max_ == min_ == 1) or
            (min_ == 1 and hashMap[min_] == 1)
        ):
            return True
        if len(hashMap) == 1:
            (key, val) = list(hashMap.items())[0]
            return key == 1 or val == 1
        return False