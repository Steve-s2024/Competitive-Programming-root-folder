from collections import defaultdict


# contest4 question2
# I hate you so much manhattan!
# this worked, but I didn't finish during contest
# this freaking question is 100% hard LeetCode!
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        hashMap = defaultdict(int)
        maxManhattan = 0
        for c in s:
            hashMap[c] += 1
            manhattan = 0
            tmp = k

            min_ = min(tmp, hashMap['E'], hashMap['W'])
            tmp -= min_
            manhattan += abs(hashMap['E'] - hashMap['W']) + 2 * min_

            min_ = min(tmp, hashMap['N'], hashMap['S'])
            tmp -= min_
            manhattan += abs(hashMap['N'] - hashMap['S']) + 2 * min_

            maxManhattan = max(maxManhattan, manhattan)
        return maxManhattan







# freaking solution won't work!
# this question is driving me crazy
'''class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        hashMap = defaultdict(int)
        maxManhattan = 0
        for c in s:
            hashMap[c] += 1
            manhattan = 0
            tmp = k

            min_ = min(tmp, hashMap['E'], hashMap['W'])
            tmp -= min_
            manhattan += abs(hashMap['E'] - hashMap['W']) + 2 * min_

            min_ = min(tmp, hashMap['N'], hashMap['S'])
            tmp -= min_
            manhattan += abs(hashMap['N'] - hashMap['S']) + 2 * min_

            manhattan += tmp
            maxManhattan = max(maxManhattan, manhattan)
        return maxManhattan'''