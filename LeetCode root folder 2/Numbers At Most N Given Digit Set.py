# not hard, as long as you know the combinatorics, it's a piece of cake: 100%
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        string = str(n)
        size = len(string)
        m = len(digits)
        res = 0
        for i in range(1, size):
            res += pow(m, i)

        # for digit in digits:
        #     if digit < string[0]:
        #         res += pow(m, size-1)
        #     elif digit == string[0]:
        #         for digit in digits:
        #             if digit < string[1]:
        #                 res += pow(m, size-2)
        #             elif digit == string[1]:
        #                 for digit in digits:
        #                     if digit == string[2]:
        #                         ......

        def recursive(pos):
            nonlocal res, size
            if pos >= size:
                res += 1
                return
            for digit in digits:
                if digit < string[pos]:
                    # print(digit, string[pos])
                    res += pow(m, size - pos - 1)
                    # print(res)
                elif digit == string[pos]:
                    recursive(pos + 1)
                else:
                    break

        recursive(0)
        return res