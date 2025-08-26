# what a man can do under extreme condition? solve hard in a already hard leetcode contest!!
# first hard problem in live contest, hooray!
# I don't even believe the solution it proved me wrong, or right?
class Solution:
    def processStr(self, s: str, k: int) -> str:
        size = 0
        arr = []
        for c in s:
            if c == '#':
                size *= 2
            elif c == '*':
                size = max(0, size - 1)
            elif c != '%':
                size += 1
            arr.append(size)
        if k >= size: return '.'

        i = len(arr) - 1
        for c in s[::-1]:
            size = arr[i]
            if c == '#':
                if k >= size // 2: k -= size // 2
            elif c == '%':
                k = size - k - 1
            elif c != '*' and k == size - 1:
                return c
            i -= 1


