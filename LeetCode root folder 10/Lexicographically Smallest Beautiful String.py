# beats 97% lets go winner!
# dug out some very interesting properties of string which contains no substring palindrome of size > 1
# the construction of such string is all about not reusing the previous two characters of the new character (proof is really neet, strong intuition)

class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:

        n = len(s)
        for i in range(n - 1, -1, -1):
            a, b = s[i - 2] if i > 1 else '', s[i - 1] if i else ''
            for j in range(ord(s[i]) + 1, ord('a') + k):
                c = chr(j)
                if c not in [a, b]:  # the position is here
                    ns = list(s)
                    ns[i] = c
                    for k in range(i + 1, n):
                        a, b = ns[k - 2] if k > 1 else '', ns[k - 1]
                        for x in 'abc':
                            if x not in [a, b]:
                                ns[k] = x
                                break
                    # print(ns)
                    return ''.join(ns)
        return ''
