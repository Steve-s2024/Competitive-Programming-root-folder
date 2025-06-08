# turns out the description doesn't even make sense with the rules of
# defining integers and decimals, stupid shit wasted my time!

class Solution:
    @staticmethod
    def integerExponent(s):
        parts = [s]
        if Counter(s)['e'] + Counter(s)['E'] > 1:
            return False
        if 'e' in s:
            parts = s.split('e')
        if 'E' in s:
            parts = s.split('E')
        if len(parts) == 2:
            return Solution.integer(parts[0]) and Solution.integer(parts[1])
        elif len(parts) == 1:
            return Solution.integer(parts[0])
        else:
            return False

    @staticmethod
    def integer(s):
        nums = '1234567890'
        if len(s) == 0:
            return False
        if s[0] in '+-':
            s = s[1:]
        if len(s) == 0:
            return False
        for c in s:
            if c not in nums:
                return False
        return True

    def isNumber(self, s: str) -> bool:
        if '.' not in s:
            # integer
            return Solution.integerExponent(s)
        else:
            # floating point
            if s[0] in '+-':
                s = s[1:]
            if len(s) == 1:
                return False
            parts = s.split('.')
            if len(parts) == 2:
                return (
                    (parts[1] == '' or parts[1][0] not in '-+') and
                    (parts[1] == '' or Solution.integerExponent(parts[1])) and
                    (parts[0] == '' or Solution.integer(parts[0]))
                )
            else:
                return False


# the most boring shit ever, unbelievably tedious if structure
class Solution:
    def isNumber(self, s: str) -> bool:
        nums = '1234567890'
        if '.' not in s:
            # integer
            if s[0] in '+-':
                s = s[1:]
            if len(s) == 0:
                return False
            for c in s:
                if c not in nums and c not in 'eE':
                    return False
            if 'e' in s or 'E' in s:
                a, b = Counter(s)['e'], Counter(s)['E']
                if not (s[0] in nums and s[-1] in nums and a+b == 1):
                    return False

            return True
        else:
            # floating point
            parts = s.split('.')
            if len(parts) > 2:
                return False
            if 'e' in parts[0]:
                return False
            if 'E' in parts[0]:
                return False
            if len(parts[0]) == 0 and len(parts[1]) == 0:
                return False

            s = ''.join(parts)
            if s[0] in '+-':
                s = s[1:]
            if len(s) == 0:
                return False
            for c in s:
                if c not in nums and c not in 'eE':
                    return False
            if 'e' in s or 'E' in s:
                a, b = Counter(s)['e'], Counter(s)['E']
                if not (s[0] in nums and s[-1] in nums and a+b == 1):
                    return False

            return True