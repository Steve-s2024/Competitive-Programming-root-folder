# interesting contest style question:49%
# class Solution:
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        b1, b2 = str(bin(n-1))[2:], str(bin(x)[2:])
        i1, i2 = len(b1)-1, len(b2)-1
        # print(b1, b2)
        res = ''
        while i1 >= 0 and i2 >= 0:
            if b2[i2] == '0':
                res = b1[i1] + res
                i1-=1
                i2-=1
            else:
                res = '1' + res
                i2-=1
        if i1 >= 0:
            res = b1[:i1+1] + res
        if i2 >= 0:
            res = b2[:i2+1] + res
        res = '0b' + res
        # print(res)
        return int(res, 2)
