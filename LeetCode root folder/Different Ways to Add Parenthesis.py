# this is not a complete solution.
'''
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def simpleCalculator(a, b, op):
            a = int(a)
            b = int(b)
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                return a / b

        operands = []
        operators = []
        num = ''
        expression += '+' # add the delimiter for the last num
        for char in expression:
            if '0' <= char <= '9':
                num += char
            else:
                operands.append(num)
                operators.append(char)
                num = ''
        operators.pop() # get rid of the last delimiter
        # print(operands, operators)

        segments = []
        for i in range(len(operators)): # init the segments
            segments.append([operands[i], operands[i+1], operators[i]])


        # brute-force
        ans = []
        def dfs(segments):
            print(segments)
            if len(segments) == 1:
                cur = segments[0]
                ans.append(simpleCalculator(cur[0], cur[1], cur[2]))
                return

            length = len(segments)
            for idx in range(length):
                copy = segments[:]
                cur = copy.pop(idx)
                res = simpleCalculator(cur[0], cur[1], cur[2])
                if idx > 0:
                    copy[idx-1] = copy[idx-1][:]
                    copy[idx-1][1] = res
                if idx < len(copy):
                    copy[idx] = copy[idx][:]
                    copy[idx][0] = res
                dfs(copy)
        dfs(segments)
        return ans
'''


