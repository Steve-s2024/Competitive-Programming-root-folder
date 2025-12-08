# pretty neat trick on the first three lines to handle all the annoying edge cases and give the rest of the code
# an opportunity to shine

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        s = s.replace('(', '(0+')
        if s[0] == '(': s = '0+' + s
        # print(s)
        if '+' not in s and '-' not in s: return int(s)
        mp = {}
        stk = []
        for i, c in enumerate(s):
            if c == '(':
                stk.append(i)
            elif c == ')':
                mp[stk.pop()] = i

        def recursive(l, r):
            x = 0
            stk = []
            i = l
            while i <= r:
                if s[i] in '0123456789':
                    x *= 10
                    x += int(s[i])
                else:
                    if s[i] == '(':
                        x = recursive(i + 1, mp[i] - 1)
                        i = mp[i]
                    else:  # +-
                        # print(stk, i)
                        if stk:
                            # print(stk, i)
                            op, va = stk.pop(), stk.pop()
                            x = (va + x) if op == '+' else (va - x)
                        stk.append(x)
                        stk.append(s[i])
                        # print(stk)
                        x = 0
                i += 1
            return (stk[0] + x) if stk[1] == '+' else (stk[0] - x)

        return recursive(0, len(s) - 1)