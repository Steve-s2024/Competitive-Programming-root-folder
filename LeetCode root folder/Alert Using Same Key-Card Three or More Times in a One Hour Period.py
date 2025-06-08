class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        hashMap = defaultdict(list)
        res = []
        for idx, name in enumerate(keyName):
            hashMap[name].append(keyTime[idx])
        for name in hashMap:
            times = hashMap[name]
            times.sort()
            l, r = 0, 0
            n1 = int(times[l][:2]) * 60 + int(times[l][3:])
            while r < len(times):
                n2 = int(times[r][:2]) * 60 + int(times[r][3:])
                while n2 - n1 > 60:
                    l += 1
                    n1 = int(times[l][:2]) * 60 + int(times[l][3:])
                if r - l >= 2:
                    res.append(name)
                    break
                r += 1
        res.sort()
        return res


