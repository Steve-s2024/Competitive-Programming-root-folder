# easy~~
class Solution:
    @staticmethod
    def nextLetter(char):
        cnt = ord(char) - ord('a')
        cnt1 = cnt + 1
        cnt2 = (cnt + 26 - 1) % 26
        cnt1 %= 26
        return (chr(cnt1 + ord('a')), chr(cnt2 + ord('a')))

    def resultingString(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if stack and stack[-1] in Solution.nextLetter(s[i]):
                stack.pop()
            else:
                stack.append(s[i])

        return ''.join(stack)