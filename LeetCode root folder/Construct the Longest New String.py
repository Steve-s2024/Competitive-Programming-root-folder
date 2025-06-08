# brute-force backtracking: tle
'''
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        def recursive(x, y, z, prev, length):
            if x + y + z == 0:
                return length
            a, b, c = 0, 0, 0
            if x and prev not in ['x']:
                a = recursive(x-1, y, z, 'x', length+2)
            if y and prev not in ['z', 'y']:
                b = recursive(x, y-1, z, 'y', length+2)
            if x and prev not in ['x']:
                c = recursive(x, y, z-1, 'z', length+2)
            return max(a, b, c)
        return recursive(x, y, z, '', 0)
'''

# unoptimized dp solution: tle
'''class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        dp = {}

        def recursive(x, y, z, prev):
            if x + y + z == 0:
                return 0
            if (x, y, z) in dp:
                return dp[(x, y, z, prev)]

            a, b, c = 0, 0, 0
            if x and prev not in ['x']:
                a = recursive(x - 1, y, z, 'x') + 2
            if y and prev not in ['z', 'y']:
                b = recursive(x, y - 1, z, 'y') + 2
            if z and prev not in ['x']:
                c = recursive(x, y, z - 1, 'z') + 2

            dp[(x, y, z, prev)] = max(a, b, c)
            return dp[(x, y, z, prev)]

        return recursive(x, y, z, '')'''

# so it is a greedy question...:2
# ms
# Beats
# 40.32%
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x == y:
            return (x + y + z) * 2
        # greedy solution
        min_ = min(x, y)
        return (min_ + min_ + 1 + z) * 2
