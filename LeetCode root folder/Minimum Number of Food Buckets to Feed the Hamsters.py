# greedy solution, the approach to this question is to simplify the condition by recognizing that each H need to have
# a food bucket either on its left or right hand-side, if both side is occupied, the hamster can't get feed and the
# algorithm should be terminated and return -1
# so now you only need to focus on how to add food bucket to either side of each hamster, the greedy solution should be
# straight forward by then:27
# ms
# Beats
# 82.68%
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        i = 0
        res = 0
        while i < len(hamsters):
            if hamsters[i] == 'H':
                if i < len(hamsters)-1 and hamsters[i+1] == '.':
                    # hamsters[i+1] = 'F'
                    res += 1
                    i += 3
                elif i > 0 and hamsters[i-1] == '.':
                    # hamsters[i-1] = 'F'
                    res += 1
                    i += 1
                else:
                    return -1
            else:
                i += 1
        # return Counter(hamsters)['F']
        return res