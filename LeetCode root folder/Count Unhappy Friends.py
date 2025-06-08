# mark and match solution (simulation):61
# ms
# Beats
# 7.98%
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        hashMap = {}
        for p1, p2 in pairs:
            hashMap[p1] = p2
            hashMap[p2] = p1

        hashSet = set()
        unhappyFriends = set()
        for i in range(n):
            for p in preferences[i]:
                if p == hashMap[i]:
                    break
                preferredPair = (min(i, p), max(i, p))
                if preferredPair in hashSet:
                    # print(preferredPair)
                    unhappyFriends.add(i)
                    unhappyFriends.add(p)
                else:
                    hashSet.add(preferredPair)
        return len(unhappyFriends)