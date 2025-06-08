# wrong method, but worth notice
class Solution:
    def baseNeg2(self, n: int) -> str:
        res = 0
        bits = list(str(bin(n)))[2:]
        print(bits)
        count = 0
        for bit in bits[::-1]:
            count += 1
            if bit == '0': # skip zero bits
                continue

            if count % 2 == 1: # odd, which means the base -2 == base 2
                res += pow(2, count-1)
            else: # even, which means the 2*(base -2) + base -2 == base 2
                res += pow(2, count-1) + pow(2, count)
        return str(bin(res))[2:]