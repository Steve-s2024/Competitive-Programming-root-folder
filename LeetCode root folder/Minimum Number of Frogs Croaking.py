# count overlapping interval:161
# ms
# Beats
# 21.64%
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        s = 'croak'
        iMap = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        hashMap = defaultdict(int)
        res = 0
        cnt = 0
        idx = 0
        hashMap[0] = float('inf')
        for i in range(len(croakOfFrogs)):
            c = croakOfFrogs[i]
            if c == 'c':
                cnt+=1
            if idx == 5:
                cnt-=1
                cnt = max(cnt, 1)
                idx = 0

            if s[idx] == c:
                idx += 1
            elif hashMap[iMap[c]]:
                hashMap[idx]+=1
                hashMap[iMap[c]]-=1
                idx = iMap[c]+1
            else:
                return -1
            # print(idx-1)
            res = max(res, cnt)
        # print(cnt)
        if idx == 5:
            cnt-=1
        if cnt != 0:
            return -1
        return res