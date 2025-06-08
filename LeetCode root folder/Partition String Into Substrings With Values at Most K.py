class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        if k < 10:
            for c in s:
                if int(c) > k:
                    return -1
            return len(s)
        cur = ''
        res = 0
        for i in range(len(s)):
            cur += s[i]
            if int(cur) > k:
                if len(cur) < 2:
                    return -1
                res += 1
                cur = s[i]
        return res + 1