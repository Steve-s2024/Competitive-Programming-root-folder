# how can a question be so hard and simple at the same time, the problem
# maker must want to showoff: 25%
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        nums = milestones
        mx = max(nums)
        sm = sum(nums)
        if mx <= sm-mx+1:
            return sm
        else:
            return 2*(sm-mx)+1