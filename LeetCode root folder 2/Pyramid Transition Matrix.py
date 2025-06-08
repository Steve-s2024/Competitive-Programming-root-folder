# with dp: 72%
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        hashMap = defaultdict(list)
        for tmp in allowed:
            hashMap[tmp[:2]].append(tmp[2])

        def getBases(arr, i, base, bases):
            n = len(arr)
            if i >= n:
                bases.append(base)
                return
            for char in arr[i]:
                getBases(arr, i + 1, base + char, bases)

        dp = set()
        def recursive(base):
            if base in dp:
                return False
            dp.add(base)
            if len(base) == 1:
                return True
            n = len(base)
            tmp = []
            for i in range(1, n):
                b = base[i - 1:i + 1]
                if b not in hashMap:
                    return False
                tmp.append(hashMap[b])

            newBases = []
            getBases(tmp, 0, '', newBases)
            for newBase in newBases:
                if recursive(newBase):
                    return True
            return False

        return recursive(bottom)


# brute force: 5%
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        hashMap = defaultdict(list)
        for tmp in allowed:
            hashMap[tmp[:2]].append(tmp[2])

        def getBases(arr, i, base, bases):
            n = len(arr)
            if i >= n:
                bases.append(base)
                return
            for char in arr[i]:
                getBases(arr, i + 1, base + char, bases)

        # print(hashMap)
        def recursive(base):
            # print(base)
            if len(base) == 1:
                return True
            n = len(base)
            tmp = []
            for i in range(1, n):
                b = base[i - 1:i + 1]
                # print(b)
                if b not in hashMap:
                    return False
                tmp.append(hashMap[b])

            newBases = []
            getBases(tmp, 0, '', newBases)
            for newBase in newBases:
                if recursive(newBase):
                    return True
            return False

        return recursive(bottom)