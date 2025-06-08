# tried with dp, not fast enough
class Solution:
    @staticmethod
    def removeGCD(a, b):
        if a == 0 and b == 0:
            return (a, b)
        if a == 0:
            return (a, b // abs(b))
        if b == 0:
            return (a // abs(a), b)

        # print(a, b)
        s1, s2 = -1 if a < 0 else 1, -1 if b < 0 else 1
        p1, p2 = [], []
        a, b = abs(a), abs(b)
        l1, l2 = math.sqrt(a), math.sqrt(b)
        f = 2
        while f <= a and f <= l1:
            while a % f == 0:
                a /= f
                p1.append(f)
            f += 1
        if a > 1:
            p1.append(a)

        f = 2
        while f <= b and f <= l2:
            while b % f == 0:
                b /= f
                p2.append(f)
            f += 1
        if b > 1:
            p2.append(b)
        i1, i2 = 0, 0
        m, n = len(p1), len(p2)
        f1, f2 = [], []
        while i1 < m and i2 < n:
            if p1[i1] == p2[i2]:
                i1 += 1
                i2 += 1
            elif p1[i1] > p2[i2]:
                f2.append(p2[i2])
                i2 += 1
            else:
                f1.append(p1[i1])
                i1 += 1
        while i1 < m:
            f1.append(p1[i1])
            i1 += 1
        while i2 < n:
            f2.append(p2[i2])
            i2 += 1
        # print(f1, f2)
        a, b = 1, 1
        for f in f1:
            a *= f
        for f in f2:
            b *= f
        # print((s1*a, s2*b))
        return (s1 * a, s2 * b)

    @staticmethod
    def getSize(points):
        [x1, y1], [x2, y2] = points[0], points[1]
        width = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        [x1, y1], [x2, y2] = points[1], points[2]
        height = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        return width * height

    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        dp = set()
        res = float('inf')

        def recursive(x, y, slopeX, slopeY):
            nonlocal res
            if (x, y) in dp:
                return
            if len(arr) == 5:
                if arr[0] == arr[-1]:
                    res = min(res, Solution.getSize(arr))
                return

            for x1, y1 in points:
                if x1 == x and y1 == y:
                    continue
                diffX, diffY = x1 - x, y1 - y
                [diffX, diffY] = Solution().removeGCD(diffX, diffY)
                if diffX == -slopeY and diffY == slopeX:
                    arr.append((x1, y1))
                    recursive(x1, y1, diffX, diffY)
                    arr.pop()

        for x, y in points:
            for x1, y1 in points:
                if x1 == x and y1 == y:
                    continue
                arr = [(x, y), (x1, y1)]
                diffX, diffY = x1 - x, y1 - y
                [diffX, diffY] = Solution.removeGCD(diffX, diffY)
                recursive(x1, y1, diffX, diffY)
            dp.add((x, y))
        return res if res != float('inf') else 0


# fixed the accuracy issue with removeGCD method, but now
# it is not fast enough
class Solution:
    @staticmethod
    def removeGCD(a, b):
        if a == 0 and b == 0:
            return (a, b)
        if a == 0:
            return (a, b // abs(b))
        if b == 0:
            return (a // abs(a), b)

        # print(a, b)
        s1, s2 = -1 if a < 0 else 1, -1 if b < 0 else 1
        p1, p2 = [], []
        a, b = abs(a), abs(b)
        l1, l2 = math.sqrt(a), math.sqrt(b)
        f = 2
        while f <= a and f <= l1:
            while a % f == 0:
                a /= f
                p1.append(f)
            f += 1
        if a > 1:
            p1.append(a)

        f = 2
        while f <= b and f <= l2:
            while b % f == 0:
                b /= f
                p2.append(f)
            f += 1
        if b > 1:
            p2.append(b)
        i1, i2 = 0, 0
        m, n = len(p1), len(p2)
        f1, f2 = [], []
        while i1 < m and i2 < n:
            if p1[i1] == p2[i2]:
                i1 += 1
                i2 += 1
            elif p1[i1] > p2[i2]:
                f2.append(p2[i2])
                i2 += 1
            else:
                f1.append(p1[i1])
                i1 += 1
        while i1 < m:
            f1.append(p1[i1])
            i1 += 1
        while i2 < n:
            f2.append(p2[i2])
            i2 += 1
        # print(f1, f2)
        a, b = 1, 1
        for f in f1:
            a *= f
        for f in f2:
            b *= f
        # print((s1*a, s2*b))
        return (s1 * a, s2 * b)

    @staticmethod
    def getSize(points):
        [x1, y1], [x2, y2] = points[0], points[1]
        width = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        [x1, y1], [x2, y2] = points[1], points[2]
        height = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        return width * height

    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        res = float('inf')

        def recursive(x, y, slopeX, slopeY):
            nonlocal res
            if len(arr) == 5:
                if arr[0] == arr[-1]:
                    res = min(res, Solution.getSize(arr))
                return

            for x1, y1 in points:
                if x1 == x and y1 == y:
                    continue
                diffX, diffY = x1 - x, y1 - y
                # print(diffX, diffY)
                [diffX, diffY] = Solution().removeGCD(diffX, diffY)
                if diffX == -slopeY and diffY == slopeX:
                    arr.append((x1, y1))
                    recursive(x1, y1, diffX, diffY)
                    arr.pop()

        for x, y in points:
            for x1, y1 in points:
                if x1 == x and y1 == y:
                    continue
                arr = [(x, y), (x1, y1)]
                # print(arr)
                diffX, diffY = x1 - x, y1 - y
                [diffX, diffY] = Solution.removeGCD(diffX, diffY)
                recursive(x1, y1, diffX, diffY)

        return res if res != float('inf') else 0


# I guess there are some floating point inaccuracy issue, so it doesn't work.
class Solution:
    @staticmethod
    def getSize(points):
        [x1, y1], [x2, y2] = points[0], points[1]
        width = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        [x1, y1], [x2, y2] = points[1], points[2]
        height = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        return width * height

    @staticmethod
    def getNextSlope(slope):
        if slope == 0:
            return float('inf')
        return -1 / slope

    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        hashMap = {}
        for x1, y1 in points:
            hashMap[(x1, y1)] = defaultdict(list)
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                if x1 == x2:
                    slope = float('inf')
                else:
                    slope = (y1 - y2) / (x1 - x2)
                hashMap[(x1, y1)][slope].append((x2, y2))

        res = float('inf')

        def recursive(x, y, prevSlope):
            nonlocal res, points
            if len(points) == 5:
                if points[0] == points[-1]:
                    tmp = Solution().getSize(points)
                    res = min(res, tmp)
                    print(points, tmp)
                return
            nextSlope = Solution.getNextSlope(prevSlope)
            for x2, y2 in hashMap[(x, y)][nextSlope]:
                points.append((x2, y2))
                recursive(x2, y2, nextSlope)
                points.pop()

        for x, y in points:
            for slope in hashMap[(x, y)]:
                for x2, y2 in hashMap[(x, y)][slope]:
                    points = [(x, y), (x2, y2)]
                    recursive(x2, y2, slope)

        return res if res != float('inf') else 0
