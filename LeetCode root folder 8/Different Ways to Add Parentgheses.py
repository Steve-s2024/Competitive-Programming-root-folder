# stupid question, this is the code that does almost the same thing and give more than asked...
class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        arr = []
        x = ''
        for c in exp:
            if c not in '+-*/':
                x += c
            else:
                arr.append(int(x))
                arr.append(c)
                x = ''
        arr.append(int(x))

        def calc(x, op, y):
            if op == '+': return x + y
            if op == '-': return x - y
            if op == '*': return x * y
            if op == '/': return x / y

        def helper(seq, arr):
            cp = arr[:]
            i = seq[0]
            x = calc(cp[i - 1], cp[i], cp[i + 1])
            cp[i - 1] = x
            cp[i] = '_'
            cp[i + 1] = x
            for i in seq[1:]:
                # print(cp)
                # print(cp[i-1], cp[i], cp[i+1])
                x = calc(cp[i - 1], cp[i], cp[i + 1])
                l, r = i - 1, i + 1
                cp[i] = '_'
                while l >= 0 and cp[l + 1] == '_':
                    cp[l] = x
                    l -= 2
                while r < len(cp) and cp[r - 1] == '_':
                    cp[r] = x
                    r += 2

            return x

        ops = [i for i in range(1, len(arr), 2)]
        ans = []
        for seq in permutations(ops):
            x = helper(seq, arr)
            ans.append(x)
        return ans


