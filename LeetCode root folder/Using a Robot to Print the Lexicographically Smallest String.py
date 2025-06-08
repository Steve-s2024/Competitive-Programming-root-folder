# dp is not the way, the complexity will not budge: TLE
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        dp = {}
        def recursive(i, string, stack):
            nonlocal n
            
            if i >= n:
                stack.reverse()
                string += ''.join(stack)
                return string
            stackS = ''.join(stack)
            if (i, string, stackS) in dp:
                return dp[(i, string, stackS)]
            stack.append(s[i])
            min_ = recursive(i+1, string, stack[:])
            while stack:
                string += stack.pop()
                min_ = min(min_, recursive(i+1, string, stack[:]))
            dp[(i, string, stackS)] = min_
            return min_
        return recursive(0, '', [])

# recursive solution incoporated with stack, template for dp: TLE
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        def recursive(i, string, stack):
            nonlocal n
            if i >= n:
                stack.reverse()
                string += ''.join(stack)
                return string

            stack.append(s[i])
            min_ = recursive(i+1, string, stack[:])
            while stack:
                string += stack.pop()
                min_ = min(min_, recursive(i+1, string, stack[:]))
            return min_
        return recursive(0, '', [])


# monotonic stack(not exactly) with suffix array, failed.
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        suffix = [False] * n
        min_ = chr(ord('z')+1)
        for i in range(n-1, -1, -1):
            if s[i] <= min_:
                suffix[i] = True
                min_ = s[i]

        # print(suffix)
        res = ''
        stack = []
        for i in range(n):
            if suffix[i]:
                while stack and stack[-1] <= s[i]:
                    res += stack.pop()
                res += s[i]
            else:
                stack.append(s[i])
        stack.reverse()
        res += ''.join(stack)
        return res

# monotonic stack approach, failed
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        res = ''
        stack = []
        for i in range(n):
            while stack and stack[0] < s[i]:
                res += stack.pop()
            stack.append(s[i])
        stack.reverse()
        res += ''.join(stack)
        return res
