# boring greedy question: 73%
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = []
        while a > b:
            if a > 1:
                res.append('aa')
                a -= 2
            else:
                res.append('a')
                a -= 1
            if b:
                res.append('b')
                b -= 1

        while b > a:
            if b > 1:
                res.append('bb')
                b -= 2
            else:
                res.append('b')
                b -= 1

            if a:
                res.append('a')
                a -= 1
        # print(a, b)
        # print(res)
        if not res or res[-1][-1] == 'a':
            res += ['ba'] * a
        else:
            res += ['ab'] * a
        return ''.join(res)