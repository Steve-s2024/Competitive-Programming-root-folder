# sliding window attempt, to be honest I don't fully understand why this
# work and didn't expect it to pass at the time of submission: 5%
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        a, b, c = arr[0], arr[1], int(''.join([str(e) for e in arr[2:]]), 2)
        # print(a, b, c)
        l, r = 1, 1
        while r < n-1:
            if a == b == c:
                return [l-1, r+1]
            if max(a, b, c) == a:
                return [-1, -1]
            while max(a, b) < c:
                r += 1
                b *= 2
                b += arr[r]
                c -= arr[r] * pow(2, n-1-r)
            while b > a:
                a *= 2
                a += arr[l]
                b -= arr[l] * pow(2, r-l)
                l += 1
            # print(a, b, c)
        return [-1, -1]


# brute force: TLE
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        arr = [str(e) for e in arr]
        n = len(arr)
        for i in range(n-2):
            a = int(''.join(arr[:i+1]), 2)
            for j in range(i+1, n-1):
                b, c = int(''.join(arr[i+1:j+1]), 2), int(''.join(arr[j+1:]), 2)
                if a == b == c:
                    return [i, j+1]
        return [-1, -1]

# deprecated
class Solution:
    @staticmethod
    def compare(arr1, arr2):
        print(arr1, arr2)
        a, b = int(''.join(arr1), 2), int(''.join(arr2), 2)
        if a < b:
            return 1
        elif a > b:
            return 2
        else:
            return 3
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        arr = [str(e) for e in arr]
        # nested binary search
        n = len(arr)
        l, r = 1, n-1
        res = None
        while l <= r:
            m = (r+l)//2
            L, R = m+1, r
            target = None
            while L < R:
                M = (R+L)//2
                part1, part2 = arr[m:M], arr[M:]
                tmp = Solution.compare(part1, part2)
                if tmp == 1: # less than
                    L = M+1
                elif tmp == 2: # greater than
                    R = M-1
                else: # equal
                    target = part1 # or arr[M:]
                    break
            tmp = Solution.compare(arr[:m], target)
            if tmp == 1: # less than
                l = m+1
            elif tmp == 2: # greater than
                r = m-1
            else: #equal
                res = target
                break
        print(res)