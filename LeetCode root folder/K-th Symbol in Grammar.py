# brute-force: TLE

'''class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        row = '0'
        for i in range(n):
            cur = ''
            for char in row:
                if char == '0':
                    cur += '01'
                else:
                    cur += '10'
            row = cur
        return int(row[k-1])'''


# fking stupid question kills all of my brain cells:0
# ms
# Beats
# 100.00%
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        bits = list(str(bin(k)))
        bits = bits[2:]

        cur1 = [0, 1]
        cur2 = [1, 0]
        res = 0
        for bit in bits:
            if bit == '1':
                res = cur2[0]
                cur1 = [0 ^ cur2[0], 1 ^ cur2[0]]
                cur2 = [0 ^ cur2[1], 1 ^ cur2[1]]
            else:
                res = cur1[1]
                cur1 = [0 ^ cur1[1], 1 ^ cur1[1]]
                cur2 = [0 ^ cur2[0], 1 ^ cur2[0]]
        return res ^ 1
