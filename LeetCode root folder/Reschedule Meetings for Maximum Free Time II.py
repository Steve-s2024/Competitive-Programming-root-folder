# contest3 question3 20250201
# good job on cracking 3 out of 4 in the contest!
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # frees = defaultdict(list)
        freesArr = []
        endTime.insert(0, 0)
        startTime.append(eventTime)
        for i in range(len(startTime)):
            # frees[startTime[i] - endTime[i]].append(i)
            freesArr.append(startTime[i] - endTime[i])
        # print(frees, freesArr)
        endTime.pop(0)
        startTime.pop()
        maxLen = 0
        sortedFrees = sorted(freesArr)
        for i in range(len(startTime)):
            dur = endTime[i] - startTime[i]
            if (freesArr[i] + freesArr[i + 1] + dur) <= maxLen:
                continue
            idx = len(sortedFrees) - 1
            if (max(freesArr[i], freesArr[i + 1]) == sortedFrees[idx]):
                idx -= 1
            if (min(freesArr[i], freesArr[i + 1]) == sortedFrees[idx]):
                idx -= 1

            if idx >= 0 and sortedFrees[idx] >= dur:
                maxLen = max(maxLen, freesArr[i] + freesArr[i + 1] + dur)
            else:
                maxLen = max(maxLen, freesArr[i] + freesArr[i + 1])
        return maxLen