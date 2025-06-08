# contest3 question2 20250201
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        frees = []
        endTime.insert(0, 0)
        startTime.append(eventTime)
        for i in range(len(startTime)):
            frees.append(startTime[i] - endTime[i])
        # print(frees)
        # now the question is about how to find the subarray in frees that is
        # of length k + 1 and has the maximum sum
        # I need to find that subarray and return the sum
        l, r = 0, 0
        sum_ = 0
        for i in range(k + 1):
            sum_ += frees[r]
            r += 1

        maxSum = sum_
        while r < len(frees):
            sum_ -= frees[l]
            sum_ += frees[r]
            maxSum = max(maxSum, sum_)
            l += 1
            r += 1

        return maxSum