# I'm pretty smart to even maintain this overcomplicated
# solution: 5%

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        mp1, mp2 = Counter(start), Counter(result)
        if (
            'L' in mp1 and 'L' not in mp2 or 'L' in mp2 and 'L' not in mp1 or
            'R' in mp1 and 'R' not in mp2 or 'R' in mp2 and 'R' not in mp1 or
            mp1['L'] != mp2['L'] or mp1['R'] != mp2['R']
        ):
            return False

        n = len(start)
        i1, i2 = 0, 0
        while i1 < n and i2 < n:
            while i1 < n and start[i1] == 'X':
                i1+=1
            while i2 < n and result[i2] == 'X':
                i2+=1
            if i1 >= n:
                break
            if start[i1] != result[i2]:
                return False
            i1+=1
            i2+=1
        
        pairs = []
        i1, i2 = 0, 0
        while i1 < n and i2 < n:
            while i1 < n and start[i1] != 'X':
                i1 += 1
            while i2 < n and result[i2] != 'X':
                i2 += 1
            if i1 >= n:
                break
            pairs.append((i1, i2))
            i1 += 1
            i2 += 1
        
        # print(pairs)
        for a, b in pairs:
            # print(a, b)
            if a >= b:
                cnt = a-b
                i = a-1
                while i >= 0 and cnt:
                    if start[i] == 'L':
                        return False
                    if start[i] == 'R':
                        cnt-=1
                    i-=1
            else:
                cnt = b-a
                i = a+1
                while i < n and cnt:
                    if start[i] == 'R':
                        return False
                    if start[i] == 'L':
                        cnt-=1
                    i+=1
            if cnt > 0:
                return False

        return True
        