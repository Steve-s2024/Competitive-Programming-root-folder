# new algorithm, trivial one. mostly math...
# 7
# ms
# Beats
# 69.51%
class Solution(object):
    def grayCode(self, n):

        seqs = [0, 1]
        for i in range(1, n):
            length = len(seqs)
            baseCase = 1 << i
            for i in range(length-1, -1, -1):
                seqs.append(baseCase + seqs[i])
        # print(seqs)
        return seqs