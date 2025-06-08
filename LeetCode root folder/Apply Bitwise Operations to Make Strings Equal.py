# this problem is not about coding, instead it is about the ability to interpret question into categories that
# are easier to understand. for this one, you can hard code all the possibilities when doing the operation:
#   0 0 --> 0 0
#   0 1 (or 1 0) --> 1 1
#   1 1 --> 0 1 (or 1 0)
# form this point its easy to conclude that even with only one '1' in the string, the string can turn into any other
# string with any number of '1's (not zero number of '1's however) in any position given that you can do unlimited amount of operations.
# a string without any '1' can not change, and it will ever only contain '0's after no matter how many operations.
'''class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        def indexOf(string, tar):
            i = 0
            while i < len(string):
                if string[i] == tar:
                    return i
                i += 1
            return -1

        n1, n2 = indexOf(s, '1'), indexOf(target, '1')
        if n1 != -1 and n2 != -1:
            return True
        if n1 == -1 and n2 == -1:
            return True
        return False'''

# or a shorter solution
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        n1, n2 = Counter(s), Counter(target)
        return (
            (n1['1'] == 0 and n2['1'] == 0) or
            (n1['1'] > 0 and n2['1'] > 0)
        )


